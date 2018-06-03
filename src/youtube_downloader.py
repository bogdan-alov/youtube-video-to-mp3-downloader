from __future__ import unicode_literals
import youtube_dl
import argparse

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
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([video_url])