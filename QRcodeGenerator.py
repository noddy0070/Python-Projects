from tkinter import *
import pyqrcode
import PIL.ImageTk, PIL.Image
from png import *

def genQRcode(linkname,link):
    
    file_name=linkname +".png"
    url=pyqrcode.create(link)
    url.png(file_name,scale=8)
    image=PIL.ImageTk.PhotoImage(PIL.Image.open(file_name))
    image_label=Label(root,image=image)
    image_label.image=image
    canvas.create_window(200,450,window=image_label)

    

root= Tk()
canvas= Canvas(root,width='400',height='600')
canvas.pack()

label= Label(root,text="QR Code Generator",font=("Arial",14,"bold"))
canvas.create_window(200,50,window=label)


label1= Label(root,text='Link Name:')
canvas.create_window(200,100,window=label1)

label2= Label(root,text="Link:")
canvas.create_window(200,150,window=label2)

entry1=Entry(root,width=20)
entry2=Entry(root,width=30)

canvas.create_window(200,130,window=entry1)
canvas.create_window(200,180,window=entry2)

button=Button(root,text='Generate QR code',command=lambda:genQRcode(entry1.get(),entry2.get()))
canvas.create_window(200,230,window=button)

root.mainloop()
