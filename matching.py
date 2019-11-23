from detect import rung
import os
import json
from criminal import ret_dict
from tkinter import *
from PIL import ImageTk, Image

has = rung()

d2 = json.load(open("tag.txt"))

if has==False:
    os.system("python notfound.py")
else:
    for key, value in d2.items():
        if value == has.person_id:
            cult = ret_dict(key)
            def main_account_screen():
                main_screen = Tk()   # create a GUI window 
                main_screen.geometry("550x500") # set the configuration of GUI window 
                main_screen.title("CRIMINAL DATABASE") # set the title of GUI window
                Label(text="MATCH FOUND!!",font='Helvetica 17 bold underline',foreground="red").place(x=160,y=30)
                Label(text="").pack()
                photo = ImageTk.PhotoImage(file =r"C:\Users\Hardik Jaroli\Desktop\Azure\test.jpg")
                Label(image=photo,width=150,height=150).place(x=180,y=80)
                Label(text="").pack()
                Label(text="ACCUSED ID:",font='Helvetica 10 bold',foreground="black").place(x=120,y=250)
                Label(text="").pack()
                Label(text=cult["ACCUSED ID"],font='Helvetica 10 bold',foreground="black").place(x=300,y=250)
                Label(text="").pack()
                Label(text="NAME:",font='Helvetica 10 bold',foreground="black").place(x=120,y=270)
                Label(text="").pack()
                Label(text=cult["NAME"],font='Helvetica 10 bold',foreground="black").place(x=300,y=270)
                Label(text="").pack()
                Label(text="AGE:",font='Helvetica 10 bold',foreground="black").place(x=120,y=290)
                Label(text="").pack()
                Label(text=cult["AGE"],font='Helvetica 10 bold',foreground="black").place(x=300,y=290)
                Label(text="").pack()
                Label(text="SEX:",font='Helvetica 10 bold',foreground="black").place(x=120,y=310)
                Label(text="").pack()
                Label(text=cult["SEX"],font='Helvetica 10 bold',foreground="black").place(x=300,y=310)
                Label(text="").pack()
                Label(text="HEIGHT:",font='Helvetica 10 bold',foreground="black").place(x=120,y=330)
                Label(text="").pack()
                Label(text=cult["HEIGHT"],font='Helvetica 10 bold',foreground="black").place(x=300,y=330)
                Label(text="").pack()
                Label(text="EYE COLOR:",font='Helvetica 10 bold',foreground="black").place(x=120,y=350)
                Label(text="").pack()
                Label(text=cult["EYE COLOR"],font='Helvetica 10 bold',foreground="black").place(x=300,y=350)
                Label(text="").pack()
                Label(text="CITY:",font='Helvetica 10 bold',foreground="black").place(x=120,y=370)
                Label(text="").pack()
                Label(text=cult["CITY"],font='Helvetica 10 bold',foreground="black").place(x=300,y=370)
                Label(text="").pack()
                Label(text="NATIONALITY:",font='Helvetica 10 bold',foreground="black").place(x=120,y=390)
                Label(text="").pack()
                Label(text=cult["NATIONALITY"],font='Helvetica 10 bold',foreground="black").place(x=300,y=390)
                Label(text="").pack()
                Label(text="CRIME:",font='Helvetica 10 bold',foreground="black").place(x=120,y=410)
                Label(text="").pack()
                Label(text=cult["CRIME"],font='Helvetica 10 bold',foreground="black").place(x=300,y=410)
                Label(text="").pack()
                Label(text="PREVIOUS RECORD:",font='Helvetica 10 bold',foreground="black").place(x=120,y=430)
                Label(text="").pack()
                Label(text=cult["PREVIOUS RECORD"],font='Helvetica 10 bold',foreground="black").place(x=300,y=430)
                Label(text="").pack()
                Button(text="EXIT", height="2", width="30",command=main_screen.destroy).place(x=150,y=450)
                main_screen.mainloop()
            main_account_screen()
            
