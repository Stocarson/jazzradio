#!/usr/bin/python3

from html.parser import HTMLParser
from urllib.request import urlopen

title = False
readTitle = False
readArtist = False
artistReady = False

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        global title
        global readTitle
        global readArtist
        global artistReady
        if tag == "img" and attrs[2] == ("height", "50"):
            swiss = "http://www.radioswissjazz.ch"
            url = swiss + attrs[3][1]
            print("The image url is '{}'".format(url))
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
        if readTitle == True:
            print("The title is '{}'".format(data))
            readTitle = False 
            readArtist = True
        if artistReady == True:
            print("The artist is '{}'".format(data))
            artistReady = False

parser = MyHTMLParser()

with urlopen("http://www.radioswissjazz.ch/it") as response:
   html = response.read()

parser.feed(html.decode("utf-8"))
