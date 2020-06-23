import sys
import os
from tkinter import filedialog
from tkinter import *

window=Tk()

window.title("Multi Modal Sentiment Analysis")
window.geometry('550x200')
def search_for_file_path ():
    currdir = os.getcwd()
    tempdir = filedialog.askopenfilename(parent=window, initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        print ("You chose: %s" % tempdir)
    return tempdir
def browse():
    textBox.delete(1.0, "end")
    textBox.insert(1.0, search_for_file_path())
def run():
    inputValue=textBox.get("1.0","end-1c")
    os.system('python image_emotion_gender_demo.py '+inputValue)
textBox=Text(window, height=2, width=60)
textBox.place(x=30,y=20)
#textBox.pack()
btn2 = Button(window, text="Browse", bg="black", fg="white",command=browse)
btn = Button(window, text="Analyze", bg="black", fg="white",command=run)
btn2.place(x=250,y=70)
btn.place(x=250,y=130)
#btn2.pack()
#btn.pack()

window.mainloop()

