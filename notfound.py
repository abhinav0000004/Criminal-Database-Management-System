from tkinter import *
from PIL import ImageTk, Image
import os
def main_account_screen():
    main_screen = Tk()   # create a GUI window 
    main_screen.geometry("250x200") # set the configuration of GUI window 
    main_screen.title("CRIMINAL DATABASE") # set the title of GUI window
    Label(text="MATCH NOT FOUND!!",font='Helvetica 17 bold underline',foreground="red").place(x=0,y=30)
    Label(text="").pack()
    Label(text=" Do you Want to add this to database?",font='Helvetica 10 bold',foreground="black").place(x=0,y=70)
    Label(text="").pack()
    def helloCallBack():
     os.system('python form.py')
    Button(text="YES", height="1", width="20",font="Helvetica 10 bold",command=helloCallBack).place(x=30,y=100)
    Label(text="").pack()
    Button(text="NO", height="1", width="20",font="Helvetica 10 bold ",command=main_screen.destroy).place(x=30,y=140)
    Label(text="").pack()
    main_screen.mainloop()  
main_account_screen()

