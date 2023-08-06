#!/usr/bin/env python3
import logging
import psycopg2

# try/except statement exists in the event of the server not being able to test
# my test cases due to not found packages
try:
    import db_cred
except ModuleNotFoundError:
    print("db_cred not found!")

logger = logging.getLogger(__name__)


class Database:
    def create_db():
        """
        Create database with credentials if it doesn't already exist
        """
        logger.info("Creating db if it doesn't already exist")
        conn = psycopg2.connect(host="sculptor.stat.cmu.edu",
                                database=db_cred.db_dbuser,
                                user=db_cred.db_user,
                                password=db_cred.db_pass,
                                sslmode='disable')

        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS spec_db (id SERIAL PRIMARY KEY," +
                    "title varchar(255)," +
                    "artist varchar(255)," +
                    "spec_filepath varchar(255));")

        cur.execute("CREATE TABLE IF NOT EXISTS song_db (id int, \
                    title varchar(255), artist varchar(255),\
                    peak2 float(10), peak3 float(10), peak4 float(10), \
                    peak5 float(10), peak6 float(10), peak7 float(10), \
                    peak8 float(10), peak9 float(10), peak10 float(10), \
                    peak11 float(10), peak12 float(10), peak13 float(10),\
                    signature float(10));")

        conn.commit()
        logger.info("Done creating db")

    def add_song_db(title, artist, peaks, signatures):
        """
        Adds song/signature data to song database

        Params:
        title Title of song
        artist Song artist
        peaks List of peaks associated with signatures
        signatures List of signatures
        """
        logger.info("Adding song to song_db")
        conn = psycopg2.connect(host="sculptor.stat.cmu.edu",
                                database=db_cred.db_dbuser,
                                user=db_cred.db_user,
                                password=db_cred.db_pass,
                                sslmode='disable')

        cur = conn.cursor()

        assert(len(peaks) > 0)
        assert(len(peaks[0]) == 12)

        # get id from spec_db table

        cur.execute("SELECT id from spec_db where spec_db.artist = '%s'\
                    and spec_db.title = '%s';" %
                    (artist, title))
        conn.commit()
        row = cur.fetchone()

        for i, peak in enumerate(peaks):
            cur.execute("INSERT INTO song_db (id, title, artist, peak2, peak3, " +
                        "peak4, peak5, peak6, peak7, peak8, peak9, peak10, " +
                        "peak11, peak12, peak13, signature)" +
                        "VALUES ('%d', '%s', '%s', '%f', '%f', '%f', \
                        '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', \
                        '%f', '%s');" %
                        (row[0], title, artist, peak[0], peak[1], peak[2], peak[3],
                            peak[4], peak[5], peak[6], peak[7], peak[8], peak[9],
                            peak[10], peak[11], signatures[i]))

        cur.execute("SELECT * FROM song_db")

        conn.commit()
        logger.info("Done adding song to song_db")

    def add_spec_db(title, artist, spec_filepath=""):
        """
        Adds spectrogram data to spectrogram database

        Params:
        title Title of song
        artist Song artist
        spec_filepath Relative filepath containing spec. (ie. "db/spec/spec1")
        """
        logger.info("Adding song to spec_db")
        conn = psycopg2.connect(host="sculptor.stat.cmu.edu",
                                database=db_cred.db_dbuser,
                                user=db_cred.db_user,
                                password=db_cred.db_pass,
                                sslmode='disable')

        cur = conn.cursor()

        cur.execute("INSERT INTO spec_db (title, artist, spec_filepath) "
                    "VALUES (%s, %s, %s)", (title, artist, spec_filepath))

        conn.commit()
        logger.info("Done adding song to spec_db")

    def remove_song_db(title, artist):
        """
        Removes song/signatures data from song/spec database

        Params:
        title Title of song
        artist Song artist
        """
        logger.info("Removing song " + title + " by " + artist + " from db")
        conn = psycopg2.connect(host="sculptor.stat.cmu.edu",
                                database=db_cred.db_dbuser,
                                user=db_cred.db_user,
                                password=db_cred.db_pass,
                                sslmode='disable')

        cur = conn.cursor()

        # get id from spec_db table

        cur.execute("DELETE from song_db where song_db.artist =" +
                    " '%s' and song_db.title = '%s';" %
                    (artist, title))

        cur.execute("DELETE from spec_db where spec_db.artist =" +
                    " '%s' and spec_db.title = '%s';" %
                    (artist, title))

        conn.commit()
        logger.info("Done removing song")

    def list_songs_db():
        """
        Lists current songs in database
        """
        logger.info("Listing songs in database:")

        conn = psycopg2.connect(host="sculptor.stat.cmu.edu",
                                database=db_cred.db_dbuser,
                                user=db_cred.db_user,
                                password=db_cred.db_pass,
                                sslmode='disable')
        cur = conn.cursor()

        cur.execute("SELECT * from spec_db;")

        all_songs = cur.fetchall()

        for song_tuple in all_songs:
            logger.info(song_tuple[1], " by ", song_tuple[2])
        conn.commit()
        logger.info("Done listing songs in database")

    def update_artist_db(title, artist, new_artist):
        """
        Updates artist of a song in the databases

        Params:
        title Title of song
        artist Song artist
        new_artist New song artist
        """
        logger.info("Updating song artist associated with title " + title)
        conn = psycopg2.connect(host="sculptor.stat.cmu.edu",
                                database=db_cred.db_dbuser,
                                user=db_cred.db_user,
                                password=db_cred.db_pass,
                                sslmode='disable')
        cur = conn.cursor()
        cur.execute("UPDATE spec_db SET artist = %s where title = " +
                    "%s and artist = %s;", (new_artist, title, artist))
        cur.execute("UPDATE song_db SET artist = %s where title = " +
                    "%s and artist = %s;", (new_artist, title, artist))
        conn.commit()
        logger.info("Done updating song artist info")

    def update_title_db(title, artist, new_title):
        """
        Updates title of a song in the databases

        Params:
        title Title of song
        artist Song artist
        new_title New song title
        """
        logger.info("Updating song artist associated with old title " + title
                    + "and artist name " + artist)
        conn = psycopg2.connect(host="sculptor.stat.cmu.edu",
                                database=db_cred.db_dbuser,
                                user=db_cred.db_user,
                                password=db_cred.db_pass,
                                sslmode='disable')
        cur = conn.cursor()
        cur.execute("UPDATE spec_db SET title = %s where title = %s " +
                    "and artist = %s;", (new_title, title, artist))
        cur.execute("UPDATE song_db SET title = %s where title = %s " +
                    "and artist = %s;", (new_title, title, artist))
        conn.commit()
        logger.info("Done updating song title info")
