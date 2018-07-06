from __future__ import unicode_literals
import youtube_dl
import argparse
import os,sys
from datetime import datetime

parser = argparse.ArgumentParser(description='Downloads a selected youtube video or playlist')
parser.add_argument('--url', nargs='?', help='Video url');

#Mp3 format options
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


while True:
	video_url = raw_input("Paste link here: ")
	try:
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			ydl.download([video_url])
	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' Type:{} Filename:{} Line:{} ERROR: {}'.format(exc_type, fname, exc_tb.tb_lineno,e))