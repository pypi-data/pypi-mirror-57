#!/usr/bin/env python3
import logging
from pydub import AudioSegment
import os
import requests
import sys
from urllib.request import urlopen


logger = logging.getLogger(__name__)


class FileIO:
    def mp3_to_wav(mp3_file):
        """
        Converts mp3 file to wav file; writes wav file to disk at same location
        and then make call to read_wav() to read file into format we care about

        Params:
        mp3_file File path (string) that contains file in .mp3 format
        """
        logger.info("Converting mp3 file to wav")
        # check that file exists and ending is .mp3
        assert os.path.exists(mp3_file)
        assert mp3_file.lower().endswith('.mp3')

        # convert wav to mp3
        sound = AudioSegment.from_mp3(mp3_file)

        # we know that our filepath now ends with ".mp3" so we can replace with
        # ".wav" and export file as wav
        dst = mp3_file[:-4] + ".wav"
        sound.export(dst, format="wav")

        logger.info("Done mp3 file to wav")

    def url_to_wav(url):
        """
        Converts url file to wav file; writes wav file to disk at same location
        and then make call to read_wav() to read file into format we care about

        Params:
        url URL to wav file to be downloaded and converted to .wav
        """
        logger.info("Converting .wav url to wav")
        # if ending is wav, read data from url, write to file
        # and then add song
        # else, print failure
        request = requests.get(url)
        # to check URL existing, we should get request status 200
        if(request.status_code == 200 and url[-4:] == ".wav"):
            u = urlopen(url)
            data = u.read()
            print(data)
            dst_filepath = "db/" + url.split('/')[-1]
            with open(dst_filepath, 'wb+') as f:
                f.write(data)
            return dst_filepath

        else:
            print("Error: can't read URL file that isn't .wav")
            sys.exit()

        logger.info("Done converting .wav url to wav")
