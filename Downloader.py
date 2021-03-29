import pytube
import os
import tkinter as tk
from tkinter import *
root = Tk()
root.title("Youtube-Downloader")

credits= Label(root,text="Made by Error_404#3059")
credits.pack()

space2 = Label(root,height=3,width=50,text="")
space2.pack()

link_info = Label(root,text="Youtube Link:")
link_info.pack()
link = Entry(root,width=50,bg="grey",fg="black")
link.pack()

def Download():
    url = link.get()
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    location = video.download()
    os.rename(location, "downloaded.mp3")
    quit()

myButton = Button(root, text="Start Downloading mp3!", command=Download)
myButton.pack()

root.mainloop()