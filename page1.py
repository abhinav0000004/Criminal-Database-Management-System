from tkinter import *
from PIL import ImageTk, Image
import os
def main_account_screen():
    main_screen = Tk()   # create a GUI window 
    main_screen.geometry("800x720") # set the configuration of GUI window 
    main_screen.title("CRIMINAL DATABASE") # set the title of GUI window
 
    Label(text="WELCOME TO THE CRIMINAL DATABASE",font='Helvetica 21 bold underline').place(x=110,y=30)
    Label(text="").pack()
    
    photo = ImageTk.PhotoImage(file =r"C:\Users\Hardik Jaroli\Desktop\Azure\test.jpg")
    Label(image=photo,width=640,height=480).place(x=80,y=70)
    Label(text="").pack()
    
    def matching():
        os.system("python matching.py")
 
# create Login Button 
    Button(text="MATCH WITH THE DATABASE", height="2", width="50",font="Helvetica 12 bold ",command=matching).place(x=150,y=600)
    Label(text="").pack() 
 
# create a register button
    Button(text="EXIT", height="2", width="30",command=main_screen.destroy).place(x=260,y=660)
    main_screen.mainloop() # start the GUI 
main_account_screen()
