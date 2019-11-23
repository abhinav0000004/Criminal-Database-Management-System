from tkinter import *
from PIL import ImageTk, Image
import os
def main_account_screen():
    main_screen = Tk()   # create a GUI window 
    main_screen.geometry("550x500") # set the configuration of GUI window 
    main_screen.title("CRIMINAL DATABASE") # set the title of GUI window
    Label(text="MATCH FOUND!!",font='Helvetica 17 bold underline',foreground="red").place(x=160,y=30)
    Label(text="").pack()
    photo = ImageTk.PhotoImage(file =r"C:\Users\abhin\Desktop\dbms projet\abh.jpg")
    Label(image=photo,width=150,height=150).place(x=180,y=80)
    Label(text="").pack()
    Label(text="ACCUSED ID:",font='Helvetica 10 bold',foreground="black").place(x=120,y=250)
    Label(text="").pack()
    Label(text="NAME:",font='Helvetica 10 bold',foreground="black").place(x=120,y=270)
    Label(text="").pack()
    Label(text="AGE:",font='Helvetica 10 bold',foreground="black").place(x=120,y=290)
    Label(text="").pack()
    Label(text="SEX:",font='Helvetica 10 bold',foreground="black").place(x=120,y=310)
    Label(text="").pack()
    Label(text="HEIGHT:",font='Helvetica 10 bold',foreground="black").place(x=120,y=330)
    Label(text="").pack()
    Label(text="EYE COLOR:",font='Helvetica 10 bold',foreground="black").place(x=120,y=350)
    Label(text="").pack()
    Label(text="CITY:",font='Helvetica 10 bold',foreground="black").place(x=120,y=370)
    Label(text="").pack()
    Label(text="NATIONALITY:",font='Helvetica 10 bold',foreground="black").place(x=120,y=390)
    Label(text="").pack()
    Label(text="CRIME:",font='Helvetica 10 bold',foreground="black").place(x=120,y=410)
    Label(text="").pack()
    Label(text="PREVIOUS RECORD:",font='Helvetica 10 bold',foreground="black").place(x=120,y=430)
    Label(text="").pack()
    Button(text="EXIT", height="2", width="30",command=main_screen.destroy).place(x=150,y=470)
    main_screen.mainloop()  
main_account_screen()
