from tkinter import *
root = Tk()                          
root.title("RA & Dec Convert Tool")  
#width ,height= 600, 600              
#root.geometry('%dx%d+%d+%d' % (width,height,(root.winfo_screenwidth() - width ) / 2, (root.winfo_screenheight() - height) / 2))
#root.maxsize(350,220)                
#root.minsize(300,200)                
label = Label(root, text="Please input the RA or Dec in float or h,m,s")
label.pack()


def convertButton1():
    result=str(u.get())
    if result == 'susan' :
        result = 'jfwang'
    elif result == 'jfwang' :
        result = 'susan'
    else:
        result=float(u.get())
        r1 = result/15
        h = int(r1//1)
        m1 = r1%1
        m2 = m1*60
        m3 = int(m2//1)
        s1 = m2%1
        s2 = s1*60
        s3 = round(s2,8)
        re=h,'h',m3,'m',s3,'s'
        result=re
    p.set(result)

    
def convertButton2():  
    result=str(u.get())
    if result == 'susan' :
        result = 'jfwang'
    elif result == 'jfwang' :
        result = 'susan'
    else:
        result=float(u.get())
        if result >= 0:
            h=int(result//1)
            m1=result%1
            m2=m1*60
            m3=int(m2//1)
            s1=m2%1
            s2=float(s1*60)
            s3=round(s2,8)
            re=h,'h',m3,'m',s3,'s'
            result=re
        elif result < 0:
            result = -result
            h=int(result//1)
            m1=result%1
            m2=m1*60
            m3=int(m2//1)
            s1=m2%1
            s2=float(s1*60)
            s3=round(s2,8)
            re=-h,'h',m3,'m',s3,'s'
            result=re
    p.set(result)
    

def convertButton3():
    result=str(u.get())
    if result == 'susan' :
        result = 'jfwang'
    elif result == 'jfwang' :
        result = 'susan'
    else:
        rlist = str(u.get())
        rlist = rlist.split(',') 
        rlist = [float(rlist[i]) for i in range(len(rlist))]
        rlist[2]=rlist[2]/60
        rlist[1]=rlist[1]+rlist[2]
        rlist[0]=rlist[0]+rlist[1]/60
        RA=rlist[0]*15
        RA1=round(RA,8)
        result=RA1
    p.set(result)

def convertButton4():
    result=str(u.get())
    if result == 'susan' :
        result = 'jfwang'
    elif result == 'jfwang' :
        result = 'susan'
    else:
        dlist=str(u.get())
        dlist = dlist.split(',')
        dlist = [float(dlist[i]) for i in range(len(dlist))]
        if dlist[0] >= 0:
            dlist = [float(dlist[i]) for i in range(len(dlist))]
            dlist[1] = (dlist[1]+dlist[2]/60)/60
            dlist[0] = dlist[0]+dlist[1]
            dlist[0] = round(dlist[0],8)
            result=dlist[0]
        elif dlist[0] < 0:
            dlist[0]=-dlist[0]
            dlist = [float(dlist[i]) for i in range(len(dlist))]
            dlist[1] = (dlist[1]+dlist[2]/60)/60
            dlist[0] = -(dlist[0]+dlist[1])
            dlist[0] = round(dlist[0],8)
            result=dlist[0]
    p.set(result)




frame = Frame(root)
frame.pack(padx=8, pady=8, ipadx=4)

lab1 = Label(frame, text="Input:", width=2, height=2, padx=15)
lab1.grid(row=0, column=0, padx=2, pady=2, sticky=W)
u = StringVar()
ent1 = Entry(frame, textvariable=u)
ent1.grid(row=0, column=1, sticky='ew', columnspan=3)

lab2 = Label(frame, text="Result:", width=2, height=2, padx=15)
lab2.grid(row=1, column=0, padx=2, pady=2, sticky=W)
p = StringVar()
ent2 = Entry(frame, textvariable=p, width=20)
ent2.grid(row=1, column=1, sticky='ew', columnspan=3)

button = Button(frame, text="RA :float to h,m,s", command=convertButton1, default='active')
button.grid(row=2, column=0, columnspan=2)
button = Button(frame, text="Dec:folat to h,m,s", command=convertButton2, default='active')
button.grid(row=2, column=2, columnspan=2)
button = Button(frame, text="RA :h,m,s to float", command=convertButton3, default='active')
button.grid(row=3, column=0, columnspan=2)
button = Button(frame, text="Dec:h,m,s to float", command=convertButton4, default='active')
button.grid(row=3, column=2, columnspan=2)




lab4 = Label(root,text='Powered by Susan')
lab4.pack()
lab5 = Label(root,text='Version 1.0.180322')
lab5.pack()



root.mainloop()
