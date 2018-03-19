from tkinter import *
import pymongo
MONGO_URL='localhost'
MONGO_DB='nanrenfuli'
MONGO_TABLE='nanrenfuli_wangpan'
client=pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]
table=db[MONGO_TABLE]
def search_mongo(string):
    for doc in table.find({}):
        if string in doc['title']:
            print(doc['wangpan'])
            return [string,doc['wangpan'],doc['tiquma'],doc['jieyamima']]
def get_entry_text(event):
    global root
    string1=e.get()
    print(string1)
    result_list=search_mongo(string1)
    print(result_list)
    for i in result_list:
        default_value = StringVar()
        default_value.set(i)
        s = Entry(root, textvariable = default_value,width=30)
        s.grid()
        #s.pack()

root=Tk()
root.geometry('300x400')
e=Entry(root, width=30)
e.grid(row=0,column=0,sticky=W)
#e.pack()
b=Button(root,text='搜索')
b.bind('<Button-1>',get_entry_text)
b.grid(row=0,sticky=E)
#b.pack()
root.mainloop()
