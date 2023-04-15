from pytube import YouTube
from tkinter import *
from tkinter import ttk
import mainguivplayer
import functionsys
from os import startfile
from functionsys import AGsearch,ytseng,end1
import time
import random


def download1low():
    ytseng()
    vname = ytseng.ytdatatitle1
    link2 = ytseng.ytdatalink1
    quality = '360p'
    downloadvid(vname,link2,quality)

def download2low():
    ytseng()
    vname = ytseng.ytdatatitle2
    link2 = ytseng.ytdatalink2
    quality = '360p'
    downloadvid(vname, link2, quality)

def download3low():
    ytseng()
    vname = ytseng.ytdatatitle3
    link2 = ytseng.ytdatalink3
    quality = '360p'
    downloadvid(vname, link2, quality)

def download4low():
    ytseng()
    vname = AGsearch.ytdatatitle4
    link2 = AGsearch.ytdatalink4
    quality = '360p'
    downloadvid(vname, link2, quality)

def download5low():
    ytseng()
    vname = AGsearch.ytdatatitle5
    link2 = AGsearch.ytdatalink5
    quality = '360p'
    downloadvid(vname, link2, quality)

def download6low():
    ytseng()
    vname = AGsearch.ytdatatitle6
    link2 = AGsearch.ytdatalink6
    quality = '360p'
    downloadvid(vname, link2, quality)


def download1high():
    ytseng()
    vname = ytseng.ytdatatitle1
    link2 = ytseng.ytdatalink1
    quality = '720p'
    downloadvid(vname,link2,quality)

def download2high():
    ytseng()
    vname = ytseng.ytdatatitle2
    link2 = ytseng.ytdatalink2
    quality = '720p'
    downloadvid(vname, link2, quality)

def download3high():
    ytseng()
    vname = ytseng.ytdatatitle3
    link2 = ytseng.ytdatalink3
    quality = '720p'
    downloadvid(vname, link2, quality)

def download4high():
    ytseng()
    vname = AGsearch.ytdatatitle4
    link2 = AGsearch.ytdatalink4
    quality = '720p'
    downloadvid(vname, link2, quality)

def download5high():
    ytseng()
    vname = AGsearch.ytdatatitle5
    link2 = AGsearch.ytdatalink5
    quality = '720p'
    downloadvid(vname, link2, quality)

def download6high():
    ytseng()
    vname = AGsearch.ytdatatitle6
    link2 = AGsearch.ytdatalink6
    quality = '720p'
    downloadvid(vname, link2, quality)


def downloadvid(vname,link2,quality):
    num = random.randint(0, 99999)
    ytdx = YouTube(link2)
    try:
        ytdx.streams.filter(progressive=True, res=quality,
                            file_extension="mp4").first().download(
            filename=str(num)+'agvideo.mp4')
    except:
        print("Some Error!")
    print('Task Completed!')

    startfile(str(num)+'agvideo.mp4')


if __name__ == '__main__':
    downloadvid()