import tkinter as tk
from tkinter import ttk
from criminal import insert_rec
      
win = tk.Tk()  
# Application Name  
win.title("Python GUI App")
win.geometry("400x400")  
# Label
headd = ttk.Label(win, text = "ENTER THE DETAILS OF CRIMINAL",font='Helvetica 17 bold underline').place(x=0,y=0)
id = ttk.Label(win, text = "ACCUSED ID:",font='Helvetica 12 bold').place(x=0,y=30)
name = ttk.Label(win, text = "NAME:",font='Helvetica 12 bold').place(x=0,y=55)
age = ttk.Label(win, text = "AGE:",font='Helvetica 12 bold').place(x=0,y=80)
sex = ttk.Label(win, text = "SEX:",font='Helvetica 12 bold').place(x=0,y=105)
height = ttk.Label(win, text = "HEIGHT:",font='Helvetica 12 bold').place(x=0,y=130)
eye = ttk.Label(win, text = "EYE COLOR:",font='Helvetica 12 bold').place(x=0,y=155)
city = ttk.Label(win, text = "CITY:",font='Helvetica 12 bold').place(x=0,y=180)
nationality = ttk.Label(win, text = "NATIONALITY:",font='Helvetica 12 bold').place(x=00,y=205)
crime = ttk.Label(win, text = "CRIME:",font='Helvetica 12 bold').place(x=0,y=230)
last = ttk.Label(win, text = "LAST RECORD:",font='Helvetica 12 bold').place(x=00,y=255)
# Click event    
# Textbox widget  
idd = tk.StringVar()  
nameEntered = ttk.Entry(win, width = 12, textvariable = idd).place(x=150,y=30)
namee = tk.StringVar()  
nameEntered = ttk.Entry(win, width = 25, textvariable = namee).place(x=150,y=55) 
agee = tk.StringVar()  
nameEntered = ttk.Entry(win, width = 12, textvariable = agee).place(x=150,y=80)
sexx = tk.StringVar()  
nameEntered = ttk.Entry(win, width = 12, textvariable = sexx).place(x=150,y=105)
heightt = tk.StringVar()  
nameEntered = ttk.Entry(win, width = 12, textvariable = heightt).place(x=150,y=130)
eyee = tk.StringVar()  
nameEntered = ttk.Entry(win, width = 20, textvariable = eyee).place(x=150,y=155)
cityy = tk.StringVar()  
nameEntered= ttk.Entry(win, width = 20, textvariable = cityy).place(x=150,y=180)
nation = tk.StringVar()  
nameEntered = ttk.Entry(win, width = 20, textvariable = nation).place(x=150,y=205)
crimee = tk.StringVar()  
nameEntered = ttk.Entry(win, width = 40, textvariable = crimee).place(x=150,y=230)
lastt = tk.StringVar()  
nameEntered = ttk.Entry(win, width = 40, textvariable = lastt).place(x=150,y=255)
def click(): 
    dict={'ACCUSED ID':idd.get(),'NAME':namee.get(),'AGE':agee.get(),'SEX':sexx.get(),'HEIGHT':heightt.get(),'EYE COLOR':eyee.get(),'CITY':cityy.get(),'NATIONALITY':nation.get(),'CRIME':crimee.get(),'PREVIOUS RECORD':lastt.get()}
    insert_rec(dict)
       
# Button widget  
button = ttk.Button(win, text = "submit", command = click).place(x=150,y=300)
win.mainloop()

