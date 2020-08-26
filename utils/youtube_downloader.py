from __future__ import unicode_literals
import youtube_dl
import os
import glob


def rename():
    return os.rename(glob.glob("*.mp4")[0], 'video.mp4')



def yt_download(url):
    #os.chdir(os.getcwd() + '/tmp')

    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        return rename()
