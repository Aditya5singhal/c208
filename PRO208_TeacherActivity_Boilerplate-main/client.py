#-----------Bolierplate Code Start -----
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

name = None
listbox = None
textarea=None
labelchat=None
text_message=None

def openChatWindow():
    window=Tk()
    window.title("messenger")
    window.geometry("500x350")
    namelabel=Label(window,text="enter your name",font=("calibri",10))
    namelabel.place(x=10,y=8)
    name=Entry(window,width=30,font=("calibri",10))
    name.place(x=120,y=8)
    name.focus()
    connectServer=Button(window,text="connect to chat server",bd=1,font=("calibri",10))
    connectServer.place(x=350,y=6)
    seperator=ttk.Separator(window,orient="horizontal")
    seperator.place(x=0,y=35,relwidth=1,height=0.1)
    connectButton=Button(window,text="connect",bd=1,font=("calibri",10))
    connectButton.place(x=282,y=160)
    disconnectButton=Button(window,text="disconnect",bd=1,font=("calibri",10))
    disconnectButton.place(x=350,y=160)
    refresh=Button(window,text="refresh",bd=1,font=("calibri",10))
    refresh.place(x=435,y=160)

    labelchat=Label(window,text="chat window",font=("calibri",10))
    labelchat.place(x=10,y=180)
    textarea=Text(window,width=67,height=6,font=("calibri",10))
    textarea.place(x=10,y=200)
    scrollbar2=Scrollbar(textarea)
    scrollbar2.place(relheight=1,relx=1)
   # scrollbar2.config(command=listbox.yview)
    text_message=Entry(window,width=43,font=("calibri",10))
    text_message.pack()
    text_message.place(x=98,y=306)
    attach=Button(window,text="attach and send",bd=1,font=("calibri",10))
    attach.place(x=10,y=305)
    filepathlabel=Label(window,text="",fg="blue",font=("calibri",10))
    filepathlabel.place(x=10,y=330)

    window.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
    openChatWindow()

setup()


#-----------Bolierplate Code Start -----