from tkinter import *
def root_add_label():
    global root
    s=Label(root,text='this is a add Label')
    s.pack(side='left')

root=Tk()
root.wm_title('zheshi wm_title')
root.geometry('300x400')
w1=Label(root,text='this is Label named w1',background='green')
w2=Label(root,text='this is Label named w2')
w3=Label(root,text='this is Label named w3')
w1.pack()
w2.pack()
w3.pack()
b1=Button(root,text='this is a button named b1',command=root_add_label)
b1.pack()
root.mainloop()