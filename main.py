from pytube import YouTube
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry('400x500')

label = Label(text="Youtube video installer")
label.pack()

link = StringVar()
link_enter = Entry(root, textvariable=link)
link_enter.pack()


# https://youtu.be/lyh2kAjcmSY - test link

def download():
    try:
        yt = YouTube(str(link.get()))
        yt.streams.get_highest_resolution().download()
        label_ = Label(text="Downloaded")
        label_.pack()
    except Exception as err:
        err_label = Label(text=str(err), width=350)
        err_label.pack()


button = Button(text="Download", command=download)
button.pack()
root.mainloop()
