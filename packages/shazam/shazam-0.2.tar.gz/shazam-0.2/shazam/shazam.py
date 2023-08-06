#!/usr/bin/env python3
import argparse
from db import Database
from file_io import FileIO
import logging
import math
import matplotlib.pyplot as plt
import numpy as np
import pickle
import psycopg2
import os
from scipy import signal
from scipy.io import wavfile
import skimage.util
import sys

# try/except statement exists in the event of the server not being able to test
# my test cases due to not found packages
try:
    import db_cred
except ModuleNotFoundError:
    print("db_cred not found!")


class Error(Exception):
    """Base class for other exceptions"""
    pass


class InvalidCLIError(Error):
    """Raised when the CLI is invalid"""
    pass


logger = logging.getLogger(__name__)


class Spectrogram:
    # add/delete spectrograms by unique id
    def __init__(self, unique_id=-1, title="", artist="", filename="",
                 external_source=""):
        self.unique_id = unique_id
        self.spec_frequencies = None
        self.spec_times = None
        self.spec = None


class Shazam:

    # Define a global variable that is a set of songs that has been initialized
    song_db = []
    spec_db = []

    global_unique_song_index = 0

    def wav_to_spectrogram(wav_file, h=10, window_shift=1, window="blackman"):
        """
        Create a spectrogram from a .wav file

        Params:

        wav_file File path of wav file
        Returns:
        Read-in wav file in a format we can use to create spectrograms
        """
        logger.info("Converting wav file to spectrogram")
        # read in wav file and convert to spectrogram based on read params
        sample_rate, data = wavfile.read(wav_file)
        if(data.ndim == 2):
            data = data.mean(axis=1)

        # frequencies, times, spectrogram: window_size = ncol(samples)
        custom_window = signal.get_window(window, h*sample_rate)
        f, t, s = signal.spectrogram(x=data, fs=sample_rate,
                                     window=custom_window)
        logger.info("Done converting wav file to spectrogram")
        return (f, t, s)

    def wav_to_periodogram(wav_file, h=10, window_shift=1, window="blackman"):
        """
        Plot a spectrogram with matplotlib

        Params:

        freq Frequencies associated with
        times Time stamps associated with a spectrogram
        spec Spectrogram data

        Returns:
        A plot of our spectrogram with matplotlib
        """
        logger.info("Converting wav file to periodogram")
        sample_rate, data = wavfile.read(wav_file)

        if(data.ndim == 2):
            data = data.mean(axis=1)

        # transform the data into smaller time windows
        int_size = h * sample_rate
        shift_interval = window_shift*sample_rate
        dt = skimage.util.view_as_windows(data,
                                          window_shape=(int_size,),
                                          step=(shift_interval))

        freq, _ = signal.periodogram(x=dt[0],
                                     fs=sample_rate,
                                     window=window,
                                     nfft=48000,
                                     scaling="spectrum")

        # for each window of our data, calculate a periodogram from that window
        power = [(signal.periodogram(x=row,
                                     fs=sample_rate,
                                     window=window,
                                     nfft=48000,
                                     scaling="spectrum")[1])
                 for row in dt]
        power = np.array(power)
        logger.info("Done converting wav file to periodogram")
        return (sample_rate, power)

    def plot_spectrogram_from_song_contents(title, artist):
        """
        Look up a song in the database and plot its spectrogram by
        calling plot_spectrogram()

        Params:

        freq Frequencies associated with
        times Time stamps associated with a spectrogram
        spec Spectrogram data

        Returns:
        A plot of our spectrogram with matplotlib
        """
        logger.info("Plotting spectrogram of " + title + " by " + artist)
        conn = psycopg2.connect(host="sculptor.stat.cmu.edu",
                                database=db_cred.db_dbuser,
                                user=db_cred.db_user,
                                password=db_cred.db_pass,
                                sslmode='disable')

        cur = conn.cursor()

        cur.execute("SELECT spec_filepath from spec_db where spec_Database.artist =" +
                    " '%s' and spec_Database.title = '%s';" %
                    (artist, title))

        row = cur.fetchone()

        conn.commit()
        with open(row[0], 'rb') as f:
            spec = pickle.load(f)

        plt.pcolormesh(spec.spec_times, spec.spec_frequencies, np.log(spec.spec))
        plt.ylabel('Frequency [Hz]')
        plt.xlabel('Time [sec]')
        plt.colorbar()
        plt.show()
        logger.info("Done plotting spectrogram")

    def octave_signatures(sampling_rate, periodogram, k=16):
        """
        Computes signatures using method 5
        a vector (p_k) where each p_k is the maximum POWER in the local periodogram
        within the kth among m pre-specified, non-overlapping frequency intervals
        (such as successive octaves, frequency bands doubling/halving in width,
        down to some minimum frequency 2^(−(m+1)f_Nyq)).
        i.e lower bounds of octaves are 1,2,4,...
        By default, we will calculate k intervals, starting at frequency 1Hz, and
        doubling to obtain new octave intervals from there.

        Params:
        periodogram The local periodogram calculated from wav_to_periodogram

        Returns:
        2-D Numpy array containing octave signatures associated with a periodogram
        peak frequencies associated with each signature
        """
        logger.info("Computing signatures with the octave power method")
        signatures = []
        freq_peaks = []
        for per_row in periodogram:
            sig = []
            for i in range(0, k-1):
                # if 2^k is larger than our sampling rate, then add 0's as fillers
                # for our signatures
                if(2**i > sampling_rate):
                    for i in range(k-len(sig)):
                        sig.append(0)
                    break
                # slice array to find max power based on, as well as frequency
                # associated with it
                octave_powers = per_row[2**i:2**(i+1)]
                max_octave_power = max(per_row[2**i:2**(i+1)])
                max_octave_freq = np.argmax(octave_powers) + 2**i

                # append (max power, max freq) to sig array
                # normalize frequency to make euc dist calculation easier
                sig.append([max_octave_power,
                            max_octave_freq,
                            max_octave_freq / (2 ** (i+1))])

            # add frequencies sorted by descending power to signatures
            # eliminate two highest and lowest octave bands due to high noise
            signatures.append([row[2] for row in sig[2:14]])
            freq_peaks.append([row[1] for row in sig[2:14]])
        logger.info("Done computing signatures with octave power method")
        return (np.array(signatures), np.array(freq_peaks))

    def identify_song(filename, match_threshold=0.5, euc_dist_threshold=0.9,
                      search="sig_psql_euclidean"):
        """
        Identifies a song based on a wav file. Will iterate through signature of
        files in the database and return a song if it exists; else will add
        the song to the db

        Params:
        filename Filename of snippet
        match_threshold Threshold of proportion of signature matches to identify
                        song
        euc_dist_threshold Threshold of euclidean distance beteween signatures to
                        call the sginatures approximately equal
        search Search algorithm (depending on hashed/not hashed and SQL db/pickle
                                db)

        Returns:
        title, song, match percentage if there was a matching song
        """

        logger.info("Identifying song from " + filename + " with " + search)

        assert os.path.exists(filename)
        wav_name = filename
        if filename.lower().endswith('.mp3'):
            FileIO.mp3_to_wav(filename)
            wav_name = filename[:-4] + ".wav"

        logger.info("Calculating singatures for snippet")
        # first compute periodograms of our
        sampling_rate, power = Shazam.wav_to_periodogram(wav_name)

        oct_sig, freq_peaks = Shazam.octave_signatures(sampling_rate, power)
        list_range = np.array(range(1, 13))
        list_range_weights = np.power(1.5, list_range)
        freq_peaks_hash = np.sum(freq_peaks * list_range_weights, axis=1)

        logger.info("Done caculating signatures for snippet")

        if search == "hash_pow_2":
            conn = psycopg2.connect(host="sculptor.stat.cmu.edu",
                                    database=db_cred.db_dbuser,
                                    user=db_cred.db_user,
                                    password=db_cred.db_pass,
                                    sslmode='disable')
            cur = conn.cursor()

            cur.execute("SELECT DISTINCT id from spec_db;")

            ids = cur.fetchall()
            conn.commit()

            id_list = [i[0] for i in ids]
            max_num_match = 0
            max_title = ""
            max_artist = ""
            for unique_id in id_list:
                # get full song signatures from sql query
                cur.execute("SELECT (signature) from song_db where id = '%d';" %
                            (unique_id))
                sigs = cur.fetchall()
                conn.commit()

                song_hashes = [(i[0]) for i in sigs]
                num_match = 0

                for sample in freq_peaks_hash:
                    best_dist = float("inf")
                    match_found = False

                    for i, song_sig in enumerate(song_hashes):
                        diff = abs(song_sig - sample)

                        if diff < best_dist:
                            best_dist = diff
                        if diff < 500 and not match_found:
                            match_found = True
                            num_match += 1

                # if we have a new max match, change max match by querying for
                # title and artist of song with id
                if num_match > max_num_match:
                    cur.execute("SELECT (title, artist) from spec_db where id = " +
                                "'%d';" % (unique_id))
                    row = cur.fetchone()[0]
                    conn.commit()
                    # remove outer parentheses from string
                    title_artist_split = row[1:-1]
                    title_artist_splits = title_artist_split.rsplit(",", 1)

                    max_title = title_artist_splits[0]
                    max_artist = title_artist_splits[1]
                    max_num_match = num_match

            match_percentage = max_num_match / len(oct_sig)

            if match_percentage >= match_threshold:
                logger.info("Closest Song: " + max_title + " by " + max_artist +
                            "; Match Percentage: " + str(match_percentage*100) +
                            "%")
            else:
                logger.info("No match for snippet")
            return (max_title, max_artist, match_percentage)

        elif search == "sig_psql_euclidean":
            conn = psycopg2.connect(host="sculptor.stat.cmu.edu",
                                    database=db_cred.db_dbuser,
                                    user=db_cred.db_user,
                                    password=db_cred.db_pass,
                                    sslmode='disable')
            cur = conn.cursor()

            cur.execute("SELECT DISTINCT id from spec_db;")

            ids = cur.fetchall()
            conn.commit()

            id_list = [i[0] for i in ids]
            max_num_match = 0
            max_title = ""
            max_artist = ""
            for unique_id in id_list:
                # get full song signatures from sql query
                cur.execute("SELECT (peak2, peak3, peak4, peak5, peak6, peak7," +
                            " peak8, peak9, peak10, peak11, peak12, peak13) " +
                            "from song_db where id = '%d';" % (unique_id))
                sigs = cur.fetchall()
                conn.commit()

                song_signatures = [np.array(eval(i[0])) for i in sigs]

                num_match = 0
                for sample in oct_sig:
                    best_euc_dist = float("inf")

                    match_found = False
                    sample_2 = sample ** 2
                    for i, song_sig in enumerate(song_signatures):
                        song_sig_2 = song_sig ** 2
                        euc_dist = math.sqrt(np.sum(np.abs(song_sig_2 - sample_2)))
                        if euc_dist < best_euc_dist:
                            best_euc_dist = euc_dist
                        if euc_dist < euc_dist_threshold and not match_found:
                            match_found = True
                            num_match += 1

                # if we have a new max match, change max match by querying title
                # and artist of song with id
                if num_match > max_num_match:
                    cur.execute("SELECT (title, artist) from spec_db where id = " +
                                "'%d';" % (unique_id))
                    row = cur.fetchone()[0]
                    conn.commit()
                    # remove outer parentheses from string
                    title_artist_split = row[1:-1]
                    title_artist_splits = title_artist_split.rsplit(",", 1)

                    max_title = title_artist_splits[0]
                    max_artist = title_artist_splits[1]
                    max_num_match = num_match

            match_percentage = max_num_match / len(oct_sig)

            if match_percentage >= match_threshold:
                logger.info("Closest Song: " + max_title + " by " + max_artist +
                            "; Match Percentage: " + str(match_percentage*100) +
                            "%")
            else:
                logger.info("No match for snippet")
            return (max_title, max_artist, match_percentage)

        # perform slow search to get match percentage by song, if db is a pickle
        elif search == "sig_pickle_euclidean_dist":
            for song in Shazam.song_db:
                num_match = 0
                for sample in oct_sig:
                    best_euc_dist = float("inf")
                    match_found = False
                    sample_2 = sample ** 2
                    for i, song_sig in enumerate(song.signature):
                        song_sig_2 = song_sig ** 2
                        euc_dist = math.sqrt(np.sum(np.abs(song_sig_2 - sample_2)))
                        if euc_dist < best_euc_dist:
                            best_euc_dist = euc_dist
                        if euc_dist < 0.9 and not match_found:
                            match_found = True
                            num_match += 1
                match_percentage = num_match / len(oct_sig)

                if match_percentage >= match_threshold:
                    logger.info("Closest Song: " + max_title + " by " + max_artist
                                + "; Match Percentage: " +
                                str(match_percentage*100) + "%")
                else:
                    logger.info("No match for snippet")
                return (song.title, song.artist, match_percentage)

        elif search == "list_slow":
            snippet_periodogram_len = oct_sig.shape[0]

            for song in Shazam.song_db:
                num_match = 0
                song_per_set = {tuple(row) for row in song.signature}
                for samp_per in oct_sig:
                    if tuple(samp_per) in song_per_set:
                        num_match += 1
                if(num_match / snippet_periodogram_len > match_threshold):
                    match_percentage = num_match / snippet_periodogram_len * 100
                    logger.info("Closest Song: " + max_title + " by " + max_artist
                                + "; Match Percentage: " +
                                str(match_percentage*100) + "%")
                else:
                    logger.info("No match for snippet")
                return (song.title, song.artist, match_percentage)

        else:
            logger.error("Signature search method invalid!")

    def add_song(title, artist, filename, external_source=""):
        """
        Adds a song with listed input params as a song in the database.

        Params:
        title Title of a song (string)
        artist Song artist (string)
        filename File name (string)

        Returns:
        A Song object that contains relevant information about a song
        """
        logger.info("Adding song " + title + " by " + artist)
        assert os.path.exists(filename)
        wav_name = filename
        if filename.lower().endswith('.mp3'):
            FileIO.mp3_to_wav(filename)
            ending_splits = filename.rsplit('.', 1)
            wav_name = ending_splits[0] + ".wav"

        # assume wav_name ends with .wav if not .mp3
        frequencies, times, spectrogram = Shazam.wav_to_spectrogram(wav_name)
        sampling_rate, power = Shazam.wav_to_periodogram(wav_name)
        oct_sig, freq_peaks = Shazam.octave_signatures(sampling_rate, power)

        # transform freq_peaks to signature with weighted hash
        list_range = np.array(range(1, 13))
        list_range_weights = np.power(1.5, list_range)
        freq_peaks_hash = freq_peaks * list_range_weights

        # add song to both db's
        Database.add_spec_db(title, artist, "")
        Database.add_song_db(title, artist, oct_sig,
                             signatures=np.sum(freq_peaks_hash, axis=1))

        new_spec = Spectrogram(Shazam.global_unique_song_index, title, artist,
                               filename, external_source)
        new_spec.spec_frequencies = frequencies
        new_spec.spec_times = times
        new_spec.spec = spectrogram
        logger.info("Song successfully added to db")


if __name__ == "__main__":
    # set up logger
    logging.basicConfig(
        filename='shazam.log',
        level=logging.DEBUG,
        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - \
               %(funcName)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )
    logger = logging.getLogger(__name__)

    logger.info("Logger set up")

    Database.create_db()
    # argparse implemented here
    parser = argparse.ArgumentParser(
            description='Freezam: Bootleg Shazam with Audio Fingerprinting.',
            usage="Usage: freezam subcommand [OPTIONS] [ARGUMENTS]")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="activates verbose logging")

    # add subparsers
    subparser = parser.add_subparsers()
    subparser_add = subparser.add_parser("add")

    subparser_add.add_argument("--title",
                               type=str, help="Song Title", default="")
    subparser_add.add_argument("--artist",
                               type=str, help="Artist Name", default="")
    subparser_add.add_argument("filepath",
                               type=str, help="Song Filepath")
    subparser_add.add_argument("-v", "--verbose", action="store_true",
                               help="activates verbose logging")
    subparser_add.set_defaults(subcommand=Shazam.add_song)

    subparser_remove = subparser.add_parser("remove")

    subparser_remove.add_argument("--title",
                                  type=str, help="Song Title", default="")
    subparser_remove.add_argument("--artist",
                                  type=str, help="Artist Name", default="")
    subparser_remove.add_argument("-v", "--verbose", action="store_true",
                                  help="activates verbose logging")
    subparser_remove.set_defaults(subcommand=Database.remove_song_db)

    subparser_update_artist = subparser.add_parser("update-artist")

    subparser_update_artist.add_argument("--title", type=str,
                                         help="Song Title", default="")
    subparser_update_artist.add_argument("--artist", type=str,
                                         help="Artist Name", default="")
    subparser_update_artist.add_argument("--new-artist", type=str,
                                         help="New Artist Name", default="")
    subparser_update_artist.add_argument("-v", "--verbose",
                                         action="store_true",
                                         help="activates verbose logging")

    subparser_update_artist.set_defaults(subcommand=Database.update_artist_db)

    subparser_update_title = subparser.add_parser("update-title")

    subparser_update_title.add_argument("--title", type=str,
                                        help="Song Title", default="")
    subparser_update_title.add_argument("--artist", type=str,
                                        help="Artist Name", default="")
    subparser_update_title.add_argument("--new-title", type=str,
                                        help="New Song Title", default="")
    subparser_update_title.add_argument("-v", "--verbose",
                                        action="store_true",
                                        help="activates verbose logging")
    subparser_update_title.set_defaults(subcommand=Database.update_title_db)

    subparser_identify = subparser.add_parser("identify")
    subparser_identify.add_argument("filepath", type=str, help="Song Filepath")
    subparser_identify.add_argument("-v", "--verbose",
                                    action="store_true",
                                    help="activates verbose logging")
    subparser_identify.set_defaults(subcommand=Shazam.identify_song)

    subparser_list = subparser.add_parser("list")
    subparser_list.add_argument("-v", "--verbose",
                                action="store_true",
                                help="activates verbose logging")
    subparser_list.set_defaults(subcommand=Database.list_songs_db)

    args = parser.parse_args(sys.argv[1:])

    # add verbose logging if args.verbose is true
    if args.verbose:
        logging.getLogger().addHandler(logging.StreamHandler())

    # check for base command if one is provided
    if(len(sys.argv) >= 2):
        try:
            if(sys.argv[1] == "add"):
                dst_filepath = args.filepath
                # check whether filepath is a URL
                # if so download the song; else, process as filepath
                if(len(dst_filepath) >= 4 and dst_filepath[:4] == "http"):
                    dst_filepath = FileIO.url_to_wav(dst_filepath)
                Shazam.add_song(args.title, args.artist, dst_filepath)
            elif(sys.argv[1] == "remove"):
                Database.remove_song_db(args.title, args.artist)
            elif(sys.argv[1] == "update-artist"):
                Database.update_artist_db(args.title, args.artist, args.new_artist)
            elif(sys.argv[1] == "update-title"):
                Database.update_title_db(args.title, args.artist, args.new_title)
            elif(sys.argv[1] == "identify"):
                Shazam.identify_song(args.filepath)
            elif(sys.argv[1] == "list"):
                Database.list_songs_db()
            else:
                raise InvalidCLIError
        except InvalidCLIError:
            logger.error("Invalid Command Line input: ", sys.argv[1])
