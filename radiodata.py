#!/usr/bin/python3

import subprocess
from time import sleep

def updateInfo():
    print("new Song!") 
    artist = newString.split(": ")[1].split(" - ")[0]    
    title = newString.split(" - ")[1].split("\n")[0]
    # Generates the new html page
    f = open("template.html", "r")
    html = f.read()
    edited = html.replace("title", title)
    edited = edited.replace("artist", artist)
    n = open("page.html", "w")
    n.write(edited)
    f.close
    n.close

def refreshBrowser():
    


currentString = ""
while True:
    name = subprocess.check_output("mpc | head -1", shell=True)
    newString = name.decode("utf-8")
    # The song's name is changed
    if currentString != newString:
        currentString = newString
        updateInfo()
    sleep(2)

