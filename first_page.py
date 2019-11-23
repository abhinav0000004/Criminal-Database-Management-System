from tkinter import *
from PIL import ImageTk, Image
import os
def main_account_screen():
    main_screen = Tk()   # create a GUI window 
    main_screen.geometry("550x500") # set the configuration of GUI window 
    main_screen.title("CRIMINAL DATABASE") # set the title of GUI window
 
    Label(text="WELCOME TO THE CRIMINAL DATABASE",font='Helvetica 17 bold underline').place(x=30,y=30)
    Label(text="").pack()
    
    photo = ImageTk.PhotoImage(file =r"C:\Users\Hardik Jaroli\Desktop\Azure\abh.jpg")
    Label(image=photo,width=350,height=300).place(x=80,y=60)
    Label(text="").pack()
    
    def capture():
        os.system("python capture.py")
 
# create Login Button 
    Button(text="CAPTURE THE IMAGE", height="2", width="50",font="Helvetica 10 bold ",command=capture).place(x=50,y=350)
    Label(text="").pack() 
 
# create a register button
    Button(text="EXIT", height="2", width="30",command=main_screen.destroy).place(x=150,y=400)
    main_screen.mainloop() # start the GUI 
main_account_screen()
