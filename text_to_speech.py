from importlib.resources import path
from gtts import gTTS
import os
from tkinter import *
from tkinter import filedialog


def selectfile(btn):
    global path
    path=filedialog.askopenfilename(title='select file to convert',initialdir='/')
    btn["text"]=path
    btn['width']=len(path)

def convert_to_audio():
    text=open(path,'r').read()
    language='en'
    output=gTTS(text=text,lang=language,slow=False)
    output.save('outputfile.mp3')
    os.system('start outputfile.mp3')

root=Tk()
canvas=Canvas(root,width=600,height=300)
canvas.pack()

label=Label(root,text='Text to speech converter',font=('times new roman','14','bold'))
canvas.create_window(300,100,window=label)

label1=Label(root,text='Select the file to make its speech :',font=('times new roman','12'))
canvas.create_window(150,150,window=label1)

button1=Button(root,text='select txt file',width=20,command=lambda:selectfile(button1))
canvas.create_window(350,150,window=button1)

button2=Button(root,text='convert and play',width=15,command=lambda:convert_to_audio())
canvas.create_window(280,200,window=button2)



root.mainloop()