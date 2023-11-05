import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import ftplib
import os
import ntpath #This is used to extract filename from path

from tkinter import filedialog
from pathlib import Path


from playsound import playsound
import pygame
from pygame import mixer


IP_ADDRESS = '127.0.0.1'
PORT = 8050
SERVER = None
BUFFER_SIZE = 4096
SONG_COUNTER = 0

window=Tk()
window.title('music Window')
window.geoetry("300x3000")
window.configure("bg='lightSkyBlue")

def setup():
    print("\n\t\t\t\t\t\tIP MESSENGER\n")

    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    musicWindow()
setup()

selectlabel = Label(window, text="Select Bong",bg="LightSkyBlue", font=("Calibri",8))
selectlabel.place(x=2, y=1)

listbox = Listbox(window,height=10,width=39,activestyle= 'dotbox',bg="LightSkyBlue",borderwidth=2 font=("Calibri",10))
listbox.place(x=10, y=10)

scrollbar1 = Scrollbar(listbox)
scrollbar1.place(relheight=1, relx=1)
scrollbar1.config(command = listbox.yview)

PlayButton=Button(window,text="Play", width=10,bd=1,bg="SkyBlue",font=("Calibri",10))
PlayButton.place(x=30,y=200)

Stop=Button(window,text="Stop",bd=1,width=10,bg="SkyBlue", font=("Calibri",10))
Stop.place(x=200,y=200)

Upload=Button(window,text="Upload",width=10,bd=1,bg="SkyBlue",font=("Calibri",10))
Upload.place(x=30,y=250)

Download=Button(window,text="Download",width=10,bd=1,bg='SkyBlue',font=("Calibri",10))
Download.place(x=200,y=250)

infoLabel = Label(window,text="",fg="blue",font=("Calibri",8))
infoLabel.place(x=6, y=200)

RasumeButton = Button(window,text="Resume", width=10,bd=1,bg='SkyBlue', font=("Calibri",10), command=rasume)
RasumeButton = place(x=30,y=250)

PauseButton= Button(window,text="Pause", width=10,bd=1,bg='SkyBlue',font= ("Calibri",10), command=pause)
PauseButton=place(x=200,y=250)

window.mainloop()

for file in os.listdir("shared_files"):
    filename = os.fsdecode(file)
    listbox.insert(SONG_COUNTER, filename)
    SONG_COUNTER = SONG_COUNTER + 1

def play():
    global song_selected
    song_selected = listbox.get(ANCHOR)

    pygame
    mixer.init()
    mixer.music.load("shared_files/"+song_selected)
    mixer.music.play()
    if(song_selected 1=""):
        infoLabel.configure(text="Now Playing:" + song_selected)
    else:
        infoLabel.configure(text="")
    Stop=Button(window,text="Stop",bd=1,width=10,bg='SkyBlue', font=("Calibri",10), command = stop)
    Stop.place(x=200,y=200)

def resume():
    global song_selected
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()

def pause():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_filer/'+song_selected)
    mixer.music.pause()