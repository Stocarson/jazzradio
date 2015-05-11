#!/usr/bin/python3

from html.parser import HTMLParser
from urllib.request import urlopen

title = False
readTitle = False
readArtist = False
artistReady = False
imgurl = ""
artist = ""
title = ""

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        global title
        global readTitle
        global readArtist
        global artistReady
        global imgurl
        if tag == "img" and attrs[2] == ("height", "50"):
            swiss = "http://www.radioswissjazz.ch"
            imgurl = swiss + attrs[3][1]
            title = True
        if title == True and tag == "span" and attrs[0] == ("class", "titletag"):
            title = False
            readTitle = True
        if readArtist == True and tag == "span" and attrs[0] == ("class", "artist"):
            readArtist = False
            artistReady = True
    def handle_data(self, data):
        global readTitle
        global readArtist
        global artistReady
        global title
        global artist
        if readTitle == True:
            title = data
            readTitle = False 
            readArtist = True
        if artistReady == True:
            artist = data
            artistReady = False

parser = MyHTMLParser()

with urlopen("http://www.radioswissjazz.ch/it") as response:
   html = response.read()

parser.feed(html.decode("utf-8"))

def update():
    parser = MyHTMLParser()
    with urlopen("http://www.radioswissjazz.ch/it") as response:
           html = response.read()
    parser.feed(html.decode("utf-8"))

def getImg():
    with urlopen(imgurl) as response:
        image = response.read()
        return image

def getArtist():
    return artist

def getTitle():
    return title

if __name__ == "__main__":
    update()
    print('The title is {}'.format(getTitle()))
    print('The artist is {}'.format(getArtist()))
