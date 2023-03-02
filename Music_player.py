
import os
from playsound import playsound
from functools import *
from tkinter import  *
from pygame import mixer
from PIL import ImageTk, Image

mixer.init()






dir_path = os.path.dirname(os.path.realpath("/home/ashutosh/Music/"))
arr=[]
file1=[]
for root, dirs, files in os.walk(dir_path):
	for file in files:

		if file.endswith('.mp3'):
			path=root+'/'+str(file)
			arr.append(str(path))
			file1.append(str(file))
			# print (root+'/'+str(file))
			# print(os.path.splitext(path)[0])
# print(file1)









tkWindow = Tk()  
tkWindow.geometry('500x900')  
tkWindow.title('Music player By Ashutosh')
tkWindow.configure(bg= "#0f1a2b")

bg = PhotoImage(file = "music icon.png")
Current = 10


def play(Current):
	# playsound(arr[Current])
	mixer.music.load(arr[Current])

	
	

	text = Label(tkWindow, text=str(file1[Current]))
	text.place(x=70,y=90)
	mixer.music.play()
	text.destroy()

	print("Playing")
	return Current


def stop(Current):
	
	mixer.music.stop()
	print("Stopping")
	# return Current


def next():
	global Current
	global my_text
	

	if (Current==len(arr)-1):
		
		Current==0
	else:
		Current=Current+1
		mixer.music.stop()
		mixer.music.load(arr[Current])
		text = Label(tkWindow, text=file1[Current])
		text.place(x=70,y=700)
		
		
		
		mixer.music.play()

	print(Current)
	print(len(arr))
	




def prev():
	global Current
	global my_text
	Current=Current-1

	mixer.music.stop()
	mixer.music.load(arr[Current])
	
	
	mixer.music.play()

	print(Current)
	# return Current




play = partial(play, Current)
stop = partial(stop, Current)
next = partial(next)
prev = partial(prev)





canvas=Canvas(tkWindow, width=500, height=900,bg="#0f1a2b")
canvas.pack()

img= ImageTk.PhotoImage(Image.open("music icon.png"))

#Add image to the Canvas Items
canvas.create_image(-20,70,anchor=NW,image=img)

text_box = Text(
    tkWindow,
    height=800,
    width=500,
	bg="White"
    
    )
text_box.pack(expand=True)
text_box.insert('end', "short")






PlayButton = Button(tkWindow, text="Play",fg="White", command=play,bg="#0f1a2b").place(x=180, y=800)
PausButton = Button(tkWindow, text="Paus",fg="White", command=stop,bg="#0f1a2b").place(x=250, y=800)
PrevButton = Button(tkWindow, text="<-",fg="White", command=prev,bg="#0f1a2b").place(x=50, y=800)
NextButton = Button(tkWindow, text="->",fg="White", command=next,bg="#0f1a2b").place(x=400, y=800)



canvas.create_line(50,750,450,750, fill="White", width=3)


# my_label.pack()
tkWindow.mainloop()
			
			



