
from tkinter.ttk import Combobox
import File_compresion.compress_module as compression
from tkinter import *
from tkinter import filedialog

def compressit(i,o,v):
    if v=="":
        compression.compress(i,o)    
    else:
        compression.compress(i,o,int(v))    

def selectfile(i):
    global path
    path=filedialog.askopenfilename(initialdir='/',title='select file to decompress',)
    i['text']=path
    i['width']=len(path)

root=Tk()
root.title('compession engine')
root.geometry('600x300')

label=Label(root,text='File compression Engine',font=('Arial','14','bold'))
label.place(x=150,y=40)

label1=Label(root,text='Enter input file name :')
label1.place(x=150,y=90)

label2=Label(root,text='Enter Output file name :')
label2.place(x=150,y=130)

label3=Label(root,text='Select power of compression :')
label3.place(x=150,y=170)

iEntry=Button(root,text='select file to compress',width=20,command=lambda:selectfile(iEntry))
iEntry.place(x=300,y=90)

oEntry=Entry(root,width=20)
oEntry.place(x=300,y=130)

combobox1=Combobox(root,textvariable=9,values=[1,2,3,4,5,6,7,8,9],width=3)
combobox1['state']='readonly'
combobox1.place(x=330,y=170)

button=Button(root,text='Compress',command=lambda:compressit(path,oEntry.get(),combobox1.get()))
button.place(x=270,y=210)
root.mainloop()
