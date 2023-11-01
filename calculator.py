from tkinter import *
import math
import re

i=str()
State=0

def getinput(entry1,variable):
    global i
    global State
    i=i+variable
    
    entry1.config(state=NORMAL)
    
    if entry1.get()=='Invalid Operation':
        entry1.delete(0,END)

    if variable<'0' or variable>'9':
        State+=1
        if State==2:
            operator(entry1)
            
    entry1.insert(END,variable)
    entry1.config(state=DISABLED)
        
                
def operator(entry1):
    global State
    value=str(entry1.get())
    result=eval(value)
    entry1.delete(0,END)
    entry1.insert(0,result)
    State=0

def equal(entry1):
    try:
        entry1.config(state=NORMAL)
        var=entry1.get()
        entry1.delete(0,END)
        entry1.insert(0,eval(var))
        entry1.config(state=DISABLED)
    except ZeroDivisionError:
        entry1.config(state=NORMAL)
        entry1.delete(0,END)
        entry1.insert(0,'Invalid Operation')
        entry1.config(state=DISABLED)

def clear(entry1):
    global State
    entry1.config(state=NORMAL)
    entry1.delete(0,END)
    entry1.config(state=DISABLED)
    State=0

def advanceoperator(entry1,variable):
    global State
    if State==0:
        entry1.config(state=NORMAL)
        val=entry1.get()
        entry1.delete(0,END)
        if variable=='!':
            entry1.insert(0,math.factorial(int(val)))
        elif variable=='√':
            entry1.insert(0,math.sqrt(int(val)))
        elif variable=='^':
            entry1.insert(0,(val+'^'))
        elif variable=='%':
            entry1.insert(0,(val+'%'))
        entry1.config(state=DISABLED)


#---------------Mainloop--------------------------------#

root=Tk()
root.title('Calculator')

entry=Entry(root,font=('Times New Roman',14,'bold'),bd=4,fg='Grey',state=DISABLED)
entry.grid(row=1,columnspan=5,sticky=W+E,pady=2)


##setting button layout
#display number

button1=Button(root,text='1',font=('arial',14,'bold'),bg='lightgrey',bd=2,command=lambda:getinput(entry,'1'))
button1.grid(row=2,column=0,sticky=W+E,pady=1,padx=1)

button2=Button(root,text='2',font=('arial',14,'bold'),bg='lightgrey',bd=2,command=lambda:getinput(entry,'2'))
button2.grid(row=2,column=1,sticky=W+E,pady=1,padx=1)

button3=Button(root,text='3',font=('arial',14,'bold'),bg='lightgrey',bd=2,command=lambda:getinput(entry,'3'))
button3.grid(row=2,column=2,sticky=W+E,pady=1,padx=1)

button4=Button(root,text='4',font=('arial',14,'bold'),bg='lightgrey',bd=2,command=lambda:getinput(entry,'4'))
button4.grid(row=3,column=0,sticky=W+E,pady=1,padx=1)

button5=Button(root,text='5',font=('arial',14,'bold'),bg='lightgrey',bd=2,command=lambda:getinput(entry,'5'))
button5.grid(row=3,column=1,sticky=W+E,pady=1,padx=1)

button6=Button(root,text='6',font=('arial',14,'bold'),bg='lightgrey',bd=2,command=lambda:getinput(entry,'6'))
button6.grid(row=3,column=2,sticky=W+E,pady=1,padx=1)

button7=Button(root,text='7',font=('arial',14,'bold'),bg='lightgrey',bd=2,command=lambda:getinput(entry,'7'))
button7.grid(row=4,column=0,sticky=W+E,pady=1,padx=1)

button8=Button(root,text='8',font=('arial',14,'bold'),bg='lightgrey',bd=2,command=lambda:getinput(entry,'8'))
button8.grid(row=4,column=1,sticky=W+E,pady=1,padx=1)

button9=Button(root,text='9',font=('arial',14,'bold'),bg='lightgrey',bd=2,command=lambda:getinput(entry,'9'))
button9.grid(row=4,column=2,sticky=W+E,pady=1,padx=1)

button9=Button(root,text='0',font=('arial',14,'bold'),bg='lightgrey',bd=2,command=lambda:getinput(entry,'0'))
button9.grid(row=5,column=1,sticky=W+E,pady=1,padx=1)

#display operator

# Basic operator

buttonmultiply=Button(root,text='*',font=('arial',14,'bold'),bg='lightgrey',bd=2,command=lambda:getinput(entry,'*'))
buttonmultiply.grid(row=2,column=3,sticky=S+N+W+E,pady=1,padx=1)

buttonadd=Button(root,text='+',font=('arial',14,'bold'),bg='lightgrey',bd=2,command=lambda:getinput(entry,'+'))
buttonadd.grid(row=4,column=3,sticky=S+N+W+E,pady=1,padx=1)

buttondivide=Button(root,text='/',font=('arial',14,'bold'),bg='lightgrey',bd=2,command=lambda:getinput(entry,'/'))
buttondivide.grid(row=5,column=3,sticky=S+N+W+E,pady=1,padx=1)

buttonsub=Button(root,text='-',font=('arial',14,'bold'),bg='lightgrey',bd=2,command=lambda:getinput(entry,'-'))
buttonsub.grid(row=3,column=3,sticky=S+N+W+E,pady=1,padx=1)

#Advance operator

buttonpercent=Button(root,text='%',font=('arial',14,'bold'),bg='lightgrey',bd=2,command=lambda:advanceoperator(entry,'%'))
buttonpercent.grid(row=3,column=4,sticky=S+N+W+E,pady=1,padx=1)

buttonexp=Button(root,text='^',font=('arial',14,'bold'),bg='lightgrey',bd=2,command=lambda:advanceoperator(entry,'^'))
buttonexp.grid(row=2,column=4,sticky=S+N+W+E,pady=1,padx=1)

buttonroot=Button(root,text='√',font=('arial',14,'bold'),bg='lightgrey',bd=2,command=lambda:advanceoperator(entry,'√'))
buttonroot.grid(row=4,column=4,sticky=S+N+W+E,pady=1,padx=1)

buttonfact=Button(root,text='!',font=('arial',14,'bold'),bg='lightgrey',bd=2,command=lambda:advanceoperator(entry,'!'))
buttonfact.grid(row=5,column=4,sticky=S+N+W+E,pady=1,padx=1)

#Clear--AC--

buttonclear=Button(root,text='AC',font=('arial',8,'bold'),bg='lightgrey',bd=2,command=lambda:clear(entry))
buttonclear.grid(row=5,column=0,sticky=S+N+W+E,pady=1,padx=1)


# display result

buttonequal=Button(root,text='=',font=('arial',14,'bold'),bg='lightgrey',bd=2,command=lambda:equal(entry))
buttonequal.grid(row=5,column=2,columnspan=1,sticky=W+E,pady=1,padx=2)

root.mainloop()