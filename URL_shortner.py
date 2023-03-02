import pyshorteners
from functools import *



from tkinter import  *
s = pyshorteners.Shortener()
# tkWindow = Tk()


def validateLogin(link):
	
    link=username.get()
    short=s.tinyurl.short(link)
    print("The sorted url is : "+short)
    
   
    text_box = Text(
    tkWindow,
    height=1,
    width=40,
    
    )
    text_box.pack(expand=True)
    text_box.insert('end', short)


    return 
	


tkWindow = Tk()  
tkWindow.geometry('1000x700')  
tkWindow.title('URL-shortner')

#paste your link below title

usernameLabel = Label(tkWindow, text="Paste your link below ").place(x=350,y=100)
usernameLabel = Label(tkWindow, text="Shorted link is ").place(x=350,y=180)
usernameLabel = Label(tkWindow, text="By - Ashitosh Kurhe ").place(x=400,y=400)
usernameLabel = Label(tkWindow, text="URL Shortner").place(x=400,y=50)

#input box of link 
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).place(x=350,y=130)

#button for link shorten
validateLogin = partial(validateLogin, usernameEntry)


LoginButton = Button(tkWindow, text="Go", command=validateLogin).place(x=520, y=125)

tkWindow.mainloop()