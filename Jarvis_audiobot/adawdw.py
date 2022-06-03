import os
import pafy
import time
import random
import re,requests,subprocess,urllib.parse,urllib.request
import vlc

def play(name,n):
    query_string = urllib.parse.urlencode({'search_query': name})
    fromalUrl = urllib.request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall(r"watch\?v=(\S*{11})", fromalUrl.read().decode())
    clip2= "https://www.youtube.com/watch?v="+"{}".format(search_results[0])
    video=pafy.new(clip2)
    if n==1:
        videolink=video.getbest()
        print("video is playing")
    else:
        
        videolink=video.getbestaudio()
        print("audio is playing")
    media=vlc.MediaPlayer(videolink.url)
    media.play()
    time.sleep(30)
    media.stop
while 1!=0:
    print("Enter 1 for video or 2 for aduio")
    n=int(input())
    print("enter de name of the song")
    play(input(),n)
    
    