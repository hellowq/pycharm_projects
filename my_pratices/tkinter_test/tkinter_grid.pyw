from tkinter import *
def root_add_label():
    global root
    Label(root,text='this is a add Label').grid(row=2,sticky=W)

root=Tk()
root.geometry('300x400')
Label(root,text='账号').grid(row=0,sticky=W)
Entry(root).grid(row=0,column=1,sticky=E)
Label(root,text='密码').grid(row=1,sticky=W)
Entry(root).grid(row=1,column=1,sticky=E)
b=Button(root,text='登录').grid(row=2,column=1,sticky=E)
b.bind('<Button-1>',root)
root.resizable(False, False)
root.mainloop()