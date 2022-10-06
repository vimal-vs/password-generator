'''   Password Generator  '''

# Modules and Libraries 

import string
import tkinter
from tkinter import Tk,Label,Button,RAISED,BOTTOM,IntVar,Checkbutton,messagebox,simpledialog,Entry
from PIL import ImageTk,Image
from random import randint,choice
import requests
import smtplib
import pyperclip

# Password Characters

characters = string.ascii_letters + string.punctuation + string.digits
characters1 = string.ascii_letters + string.digits
characters2 = string.ascii_letters + string.punctuation 


# GUI

tk = Tk()

tk.title('Password Generator')
tk.iconbitmap('pass_logo.ico')
tk.geometry('600x800')


# Background Image

bg_img = Image.open('pass.png')
bg_lbl = ImageTk.PhotoImage(bg_img)
label = Label(image=bg_lbl)
label.image = bg_lbl 
label.place(relwidth=1,relheight=1)

h1 = Label(tk,text='Password Generator',padx=5,pady=1,bg='black',fg='white',font='IMPRISHA 20 ')
h1.pack(padx=20,pady=20)




# CheckButtons

CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()

C1 = Checkbutton(tk, text = 'Alphabets', variable = CheckVar1, 
                 onvalue = 1, offvalue = 0, height=5, 
                 width = 8,bg='black',fg='white',selectcolor='#3377ff',activebackground='black',activeforeground='white',font='IMPRISHA')

C2 = Checkbutton(tk, text = 'Numbers', variable = CheckVar2, 
                 onvalue = 1, offvalue = 0, height=5, 
                 width = 8,bg='black',fg='white',selectcolor='#3377ff',activebackground='black',activeforeground='white',font='IMPRISHA')

C3 = Checkbutton(tk, text = 'Symbols', variable = CheckVar3, 
                 onvalue = 1, offvalue = 0, height=5, 
                 width = 8,bg='black',fg='white',selectcolor='#3377ff',activebackground='black',activeforeground='white',font='IMPRISHA')

C1.pack(pady=8)
C2.pack(pady=8)
C3.pack(pady=8)




# Buttons

#quit
quit_button = Button(
    tk,text='Quit',padx=10,pady=1,command=lambda : quitt(),
    bg='black',fg='white',activebackground='#3377ff',activeforeground='white',relief=RAISED,
    bd=5,width=5,font='IMPRISHA 8')

quit_button.place(relx=0.45,rely=0.85)

#textfile
textfile_button = Button(
    tk,text='Text File',padx=20,pady=10,bg='black',fg='white',activebackground='#3377ff',activeforeground='white',
    relief=RAISED,bd=5,width=5,font='IMPRISHA 11',command=lambda: textfile())

textfile_button.place(relx=0.42,rely=0.75)

#clipboard
clipboard_button = Button(tk,text='ClipBoard',padx=20,pady=10,bg='black',fg='white',activebackground='#3377ff',activeforeground='white',
relief=RAISED,bd=5,width=5,font='IMPRISHA 11',command=lambda: clipboard())

clipboard_button.place(relx=0.42,rely=0.65)

#mail
button_mail = Button(tk, text='Email',bg='black',fg='white',activebackground='#3377ff',activeforeground='white',
    bd=3,relief=RAISED,font='IMPRISHA 12', command=lambda : mail())
button_mail.place(relx=0.7,rely=0.55,relwidth=0.15,relheight=0.04)

entry_mail = Entry(tk,bg='black',fg='white')
entry_mail.place(relx=0.29,rely=0.55,relwidth=0.4,relheight=0.04)



# PY Functions

password = ''

def generate():

    global password 
    password = ''

    if CheckVar1.get() == 1 and CheckVar2.get() == 1 and CheckVar3.get() == 1:
        password =  "".join(choice(characters) for x in range(randint(8,16)))
       

    elif CheckVar1.get() == 1 and CheckVar2.get() == 1 and CheckVar3.get() == 0: 
        password =  "".join(choice(characters1) for x in range(randint(8,16)))
       

    elif CheckVar1.get() == 1 and CheckVar2.get() == 0 and CheckVar3.get() == 1:
        password =  "".join(choice(characters2) for x in range(randint(8,16)))
       
    
    elif CheckVar1.get() == 0 :
        messagebox.showerror('Error','Alphabets is Mandatory')

    elif CheckVar2.get() == 0 and CheckVar3.get() == 0:
        messagebox.showerror('Error','Select atleast 2')

    else :
        messagebox.showerror('Error','Error404')




def textfile():
    
    generate()

    if len(password)>=8:

        pass_file = open('password.txt', 'a')
        pass_file.write(password)
        pass_file.close()
        messagebox.showinfo('Password saved','Saved in password.txt')



def mail():

    generate()

    if len(password)>=8:

        mail = entry_mail.get()

        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('passgen.pybot@gmail.com','mncugcthvrwbdiay')

        subject = 'Password Generated'
        body = 'Your generated password is\n',password

        msg = f'Subject: {subject}\n\n{body}'
    
    
        server.sendmail(
            'passgen.pybot@gmail.com',
            mail,
            msg
        )

        server.quit()

        messagebox.showinfo('Password Generated','Your Password is sent to your mail')



def clipboard():
    
    generate()

    if len(password)>=8:

        pyperclip.copy(password)
        messagebox.showinfo('Password Generated','Password is copied to clipboard')



def quitt():

    raise SystemExit




# End 

tk.mainloop()