from db import Database
from file_io import FileIO
import logging
import numpy as np
import os
import pytest
from scipy.io import wavfile
from shazam import Shazam
try:
    import db_cred
    import psycopg2
    db_cred_not_found = False
except ModuleNotFoundError:
    db_cred_not_found = True


logger = logging.getLogger(__name__)


@pytest.mark.skipif(db_cred_not_found, reason="Requires DB Credentials")
def create_sample_audio_snippets():
    # generate small 1s wav file
    sampling_rate = 44100
    freq = 440
    samples = 441000
    x1 = np.arange(samples)
    y1 = 100*np.sin(2 * np.pi * x1 * freq / sampling_rate)
    x2 = np.arange(samples)
    y2 = 50*np.cos(2 * np.pi * x2 * freq / sampling_rate) + 50

    # write wave to file
    wavfile.write("db/sample_wav_1.wav", sampling_rate, y1)
    wavfile.write("db/sample_wav_2.wav", sampling_rate, y2)


@pytest.mark.skipif(db_cred_not_found, reason="Requires DB Credentials")
def test_add_song():
    """
    Test adding a song and checking its existence in the db
    """
    # insert song into db
    assert os.path.exists("db/sample_wav_1.wav")

    conn = psycopg2.connect(host="sculptor.stat.cmu.edu",
                            database=db_cred.db_dbuser,
                            user=db_cred.db_user,
                            password=db_cred.db_pass,
                            sslmode='disable')
    cur = conn.cursor()
    cur.execute("SELECT * from spec_db where spec_db.artist = 'test_artist3'\
                and spec_db.title = 'test_song3';")

    conn.commit()
    song_list_start = cur.fetchall()
    song_db_len_start = len(song_list_start)

    fake_peaks = np.array([0.0] * 12)
    fake_sigs = np.array([0.0] * 12)
    Database.add_spec_db("test_song3", "test_artist3", "")

    Database.add_song_db("test_song3", "test_artist3",
                         np.array([fake_peaks]), np.array(fake_sigs))

    cur.execute("SELECT * from spec_db where spec_db.artist = 'test_artist3'\
                and spec_db.title = 'test_song3';")
    conn.commit()
    song_list_end = cur.fetchall()
    song_db_len_end = len(song_list_end)
    assert(song_db_len_end - song_db_len_start == 1)


@pytest.mark.skipif(db_cred_not_found, reason="Requires DB Credentials")
def test_remove_song():
    """
    Test remove a song and checking its existence in the db
    """
    conn = psycopg2.connect(host="sculptor.stat.cmu.edu",
                            database=db_cred.db_dbuser,
                            user=db_cred.db_user,
                            password=db_cred.db_pass,
                            sslmode='disable')
    cur = conn.cursor()
    # add a song with test_add_song() and remove the song once added
    test_add_song()

    Database.remove_song_db("test_song3", "test_artist3")

    cur.execute("SELECT count(*) FROM spec_db where artist = 'test_artist3'\
                and title = 'test_song3'")
    row = cur.fetchone()
    assert(row[0] == 0)

    cur.execute("SELECT count(*) FROM song_db where artist = 'test_artist3'\
                and title = 'test_song3'")
    row = cur.fetchone()
    assert(row[0] == 0)
    conn.commit()


@pytest.mark.skipif(db_cred_not_found, reason="Requires DB Credentials")
def test_identify_song():
    """
    Test identifying a song
    """
    # insert sample snippet into db
    Shazam.add_song("test_song1", "test_artist1", "db/sample_wav_1.wav")

    # test that exact song will match 100%
    title1, artist1, match_pct1 = Shazam.identify_song("db/sample_wav_1.wav")
    assert(title1 == "test_song1" and artist1 == "test_artist1")

    Shazam.add_song("test_song2", "test_artist2", "db/sample_wav_2.wav")
    title2, artist2, match_pct2 = Shazam.identify_song("db/sample_wav_2.wav")
    assert(title2 == "test_song2" and artist2 == "test_artist2")


@pytest.mark.skipif(db_cred_not_found, reason="Requires DB Credentials")
def test_update_song_title():
    """
    Test updating a song's title
    """
    # insert song into db
    assert os.path.exists("db/sample_wav_1.wav")
    test_add_song()
    conn = psycopg2.connect(host="sculptor.stat.cmu.edu",
                            database=db_cred.db_dbuser,
                            user=db_cred.db_user,
                            password=db_cred.db_pass,
                            sslmode='disable')
    cur = conn.cursor()
    cur.execute("SELECT * from spec_db where spec_db.artist = 'test_artist3'\
                and spec_db.title = 'new_song_title';")

    conn.commit()
    song_list_start = cur.fetchall()
    song_db_len_start = len(song_list_start)

    Database.update_title_db("test_song3", "test_artist3", "new_song_title")

    cur.execute("SELECT * from spec_db where spec_db.artist = 'test_artist3'\
                and spec_db.title = 'new_song_title';")
    conn.commit()
    song_list_end = cur.fetchall()
    song_db_len_end = len(song_list_end)
    assert(song_db_len_end - song_db_len_start == 1)


@pytest.mark.skipif(db_cred_not_found, reason="Requires DB Credentials")
def test_update_song_artist():
    """
    Test updating a song's artist name
    """
    # insert song into db
    assert os.path.exists("db/sample_wav_1.wav")
    test_add_song()
    conn = psycopg2.connect(host="sculptor.stat.cmu.edu",
                            database=db_cred.db_dbuser,
                            user=db_cred.db_user,
                            password=db_cred.db_pass,
                            sslmode='disable')
    cur = conn.cursor()
    cur.execute("SELECT * from spec_db where artist = 'new_song_artist'\
                and title = 'test_song3';")

    conn.commit()
    song_list_start = cur.fetchall()
    song_db_len_start = len(song_list_start)

    Database.update_artist_db("test_song3", "test_artist3", "new_song_artist")

    cur.execute("SELECT * from spec_db where artist = 'new_song_artist'\
                and title = 'test_song3';")
    conn.commit()
    song_list_end = cur.fetchall()
    song_db_len_end = len(song_list_end)
    assert(song_db_len_end - song_db_len_start == 1)


def test_mp3_to_wav():
    """
    Test conversion of mp3 to wav
    """
    # get list of mp3 files in a directory (ie. "db/")
    mp3_files = []
    for root, dirs, files in os.walk("db/"):
        for file in files:
            if file.endswith(".mp3"):
                mp3_path = os.path.join(root, file)
                mp3_files.append(mp3_path)
                FileIO.mp3_to_wav(mp3_path)

    # check that the .wav file corresponding to an mp3 is in our directory
    for f in mp3_files:
        wav_name = f[:-4] + ".wav"
        assert os.path.exists(wav_name)


if __name__ == "__main__":
    create_sample_audio_snippets()
    test_add_song()
    test_remove_song()
    test_identify_song()
    test_update_song_title()
    test_update_song_artist()
    test_mp3_to_wav()
    logger.info("Ran all automated tests and succeeded!")
