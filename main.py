import tkinter as tk
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pswgenerator():
    letter = ['a','b','c','d','e','f','g','h','i','j','k',"l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    number = [0,1,2,3,4,5,6,7,8,9]
    symbol = ['!','#','$','%','&','(',')','*','+']

    nr_letter  = random.randint(8,10)
    nr_number = random.randint(2,4)
    nr_symbol = random.randint(2,4)

    P= []
    for l in range (nr_letter):
        P.append(random.choice(letter))


    for n in range (nr_number):
        P.append(random.choice(number))

    for s in range (nr_symbol):
        P.append(random.choice(symbol))

    random.shuffle(P)

    p = ""

    for i in P:
        p += str(i)


    
    pswinput.insert(0,p)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def savepsw ():

    if websiteinput.get() == "" or emailinput.get() == "" or pswinput.get() == "":
        messagebox.showinfo(message = "Please don't leave any fields empty!")
    
    else:
        is_ok = messagebox.askokcancel (title = websiteinput.get(),message = f"These are the detials entered: \nEmail: {emailinput.get()}"
                                f"\nPassword: {pswinput.get()} \nIs it ok to save?")
        
        
        if is_ok:
            with open ("MyPasswordManager.txt",mode = "a") as file:
                l = websiteinput.get() + " | " + emailinput.get() + " | " + pswinput.get() +"\n"
                file.write (l)

            messagebox.showinfo(message = "Password saved!")

    



# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.minsize (height = 400, width = 600)
window.config (padx = 100, pady = 100, bg = "white")


canvas = tk.Canvas(height = 200, width = 200, bg = "white",highlightthickness=0)
logo_img = tk.PhotoImage (file = "logo.png")
canvas.create_image(90,80, image = logo_img)
# canvas.create_text(200,200, text = "test",fill = "white", font = ("Arial", 35, "bold"))
canvas.grid(column = 3, row = 1)


websitelabel = tk.Label (text = "Website:",font = ("Arial",  15, "bold"), bg = "white",fg = "black")
websitelabel.grid(column =2 , row = 2)

websiteinput = tk.Entry(width = 40,bg = "white", fg = "black",highlightthickness=0, insertbackground = "black")
websiteinput.grid(column = 3, row = 2, columnspan = 2)
websiteinput.focus()

emaillabel = tk.Label (text = "Email/Username:",font = ("Arial",  15, "bold"), bg = "white",fg = "black")
emaillabel.grid(column = 2, row = 3)

emailinput = tk.Entry(width = 40, bg = "white",fg = "black",highlightthickness=0, insertbackground = "black")
emailinput.insert(0,"zzq01991@gmail.com")
emailinput.grid(column = 3, row = 3,columnspan = 2)



pswlabel = tk.Label (text = "Password:",font = ("Arial",  15, "bold"), bg = "white",fg = "black")
pswlabel.grid(column = 2, row = 4)

pswinput = tk.Entry(width = 22, bg = "white",fg = "black", highlightthickness=0, insertbackground = "black")
pswinput.grid(column = 3, row = 4)



generatorbutton = tk.Button(text = "Generate Password" ,  bg = "white", highlightbackground="white", command = pswgenerator)
generatorbutton.grid(column = 4, row= 4)


addbutton = tk.Button(text = "Add" , width =37,  bg = "white", highlightbackground="white", command = savepsw)
addbutton.grid(column = 3, row= 5, columnspan = 2)

window.mainloop()
