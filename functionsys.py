import json
import time

from youtubesearchpython import SearchVideos
from youtubesearchpython import *
import re
import requests
import mainguivplayer
import random



age = '16-58'
gender = 'Female'
ytsearched2 = ""

def ytseng():
    agecontra = ''
    if age == '1-15':
        agecontra = ["Youtube Kids ","#kids ", "For Kids "]
        agecontra = random.choice(agecontra)

    search = SearchVideos(agecontra+ytsearched2, VideoUploadDateFilter.lastHour, mode="json", max_results=3)
    r = search.result()
    sourcex = json.loads(r)
    source1 = sourcex['search_result']
    data1 = source1[0]
    data2 = source1[1]
    data3 = source1[2]
    ytitle1 = data1['title']
    ytitle1 = (ytitle1[:30] + '...') if len(ytitle1) > 30 else ytitle1
    ytitle2 = data2['title']
    ytitle2 = (ytitle2[:30] + '...') if len(ytitle2) > 30 else ytitle2
    ytitle3 = data3['title']
    ytitle3 = (ytitle3[:30] + '...') if len(ytitle3) > 30 else ytitle3
    ytseng.ytdatalink1 = data1['link']
    ytseng.ytdatatitle1 = ytitle1
    ytseng.ytdatalink2 = data2['link']
    ytseng.ytdatatitle2 = ytitle2
    ytseng.ytdatalink3 = data3['link']
    ytseng.ytdatatitle3 = ytitle3

    mainguivplayer.vtitle1 = ytitle1
    mainguivplayer.vtitle2 = ytitle2
    mainguivplayer.vtitle3 = ytitle3


def AGsearch():
    agecontra = ''
    if age == '1-15':
        agecontra = ["Youtube Kids ", "LittleBabyBum ", "Ryan's World ", "El Reino Infantil ", "Masha and the Bear ", "Disney Junior ", "Nick Jr. "]
        agecontra = random.choice(agecontra)
    if age == '59-70+':
        agecontra = ["Cyber-Seniors Corner ", "2nd Act TV ", "#elderly ", "#seniors "]
        agecontra = random.choice(agecontra)

    if gender == 'Male':
        gendercontra = 'for male '
    if gender == 'Female':
        gendercontra = 'for female '

    search = SearchVideos(gendercontra+agecontra+ytsearched2, VideoUploadDateFilter.lastHour, mode="json", max_results=3)
    r = search.result()
    sourcey = json.loads(r)
    source2 = sourcey['search_result']
    data4 = source2[0]
    data5 = source2[1]
    data6 = source2[2]


    #truncate title words
    ytitle1 = data4['title']
    ytitle1 = (ytitle1[:30] + '...') if len(ytitle1) > 30 else ytitle1
    ytitle2 = data5['title']
    ytitle2 = (ytitle2[:30] + '...') if len(ytitle2) > 30 else ytitle2
    ytitle3 = data6['title']
    ytitle3 = (ytitle3[:30] + '...') if len(ytitle3) > 30 else ytitle3
    AGsearch.ytdatalink4 = data4['link']
    AGsearch.ytdatatitle4 = ytitle1
    AGsearch.ytdatalink5 = data5['link']
    AGsearch.ytdatatitle5 = ytitle2
    AGsearch.ytdatalink6 = data6['link']
    AGsearch.ytdatatitle6 = ytitle3

    mainguivplayer.vtitle4 = ytitle1
    mainguivplayer.vtitle5 = ytitle2
    mainguivplayer.vtitle6 = ytitle3


def get_thumbnail():
    url1 = ytseng.ytdatalink1
    url2 = ytseng.ytdatalink2
    url3 = ytseng.ytdatalink3
    url4 = AGsearch.ytdatalink4
    url5 = AGsearch.ytdatalink5
    url6 = AGsearch.ytdatalink6
    exp = "^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*"
    s1 = re.findall(exp, url1)[0][-1]
    thumbnail1 = f"https://i.ytimg.com/vi/{s1}/0.jpg"
    s2 = re.findall(exp, url2)[0][-1]
    thumbnail2 = f"https://i.ytimg.com/vi/{s2}/0.jpg"
    s3 = re.findall(exp, url3)[0][-1]
    thumbnail3 = f"https://i.ytimg.com/vi/{s3}/0.jpg"
    s4 = re.findall(exp, url4)[0][-1]
    thumbnail4 = f"https://i.ytimg.com/vi/{s4}/0.jpg"
    s5 = re.findall(exp, url5)[0][-1]
    thumbnail5 = f"https://i.ytimg.com/vi/{s5}/0.jpg"
    s6 = re.findall(exp, url6)[0][-1]
    thumbnail6 = f"https://i.ytimg.com/vi/{s6}/0.jpg"

    response1 = requests.get(thumbnail1)
    response2 = requests.get(thumbnail2)
    response3 = requests.get(thumbnail3)
    response4 = requests.get(thumbnail4)
    response5 = requests.get(thumbnail5)
    response6 = requests.get(thumbnail6)
    with open('./thumb1.png', 'wb') as f:
        f.write(response1.content)
    with open('./thumb2.png', 'wb') as f:
        f.write(response2.content)
    with open('./thumb3.png', 'wb') as f:
        f.write(response3.content)
    with open('./thumb4.png', 'wb') as f:
        f.write(response4.content)
    with open('./thumb5.png', 'wb') as f:
        f.write(response5.content)
    with open('./thumb6.png', 'wb') as f:
        f.write(response6.content)


def end1():
    import threading
    from mainguivplayer import mainguivplay
    from mainguivplayer import loadingscreen
    import newtest
    dltime = 5000
    loadingscreen(dltime)
    ytseng()
    AGsearch()
    get_thumbnail()
    loadingscreen(dltime)
    mainguivplay()

if __name__ == '__main__':
    end1()