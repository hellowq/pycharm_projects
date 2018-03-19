from tkinter import *
def add_label(event):
    global root
    s=Label(root,text='this is label')
    s.pack()
root=Tk()
root.geometry('300x400')
b=Button(root,text='button')
b.bind('<Button-1>',add_label)
b.pack()
root.mainloop()
