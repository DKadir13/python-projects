#Tkinter nedir
""" 
Tkinter bir python kütüphanesidir.
masaüstü programları tasarlamamızı sağlar.

"""
"""İlk aşamada tkinter isminde tk ismini verdik. İkinci aşamada bütün tkinter kütüphanesini çağırdık. 3.adımda ise message box u özel olarak import ettik """
import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = tk.Tk()
root.title("Tkinter Örnek Uygulama")
root.geometry("400x400")

userLabel = Label(root, text="Kullanıcı Adı       :" ,width=20, height=3, font=("Arial", 10), fg="darkblue", bg="gray", relief="groove", bd=5, anchor="w")

userLabel.place(x=5, y=26)
passwordLabel = Label(root, text=" ŞİFRE       :" ,width=20, height=3, font=("Arial", 10), fg="darkblue", bg="gray", relief="groove", bd=5, anchor="w")
passwordLabel.place(x=5, y=100)


#------------------Entry------------------
usernameEntry = Entry(root, width=15 , font="bold")
usernameEntry.place(x=200, y=40)

passwordEntry = Entry(root, width=15 , font="bold", show="*")
passwordEntry.place(x=200, y=115)
#show sayesinde şifrelerin gözüküp gözükemeyeceğini ayarlarız.
#-----------------------------------------

#------------------Fonksiyon------------------
def userControl():
    if usernameEntry.get() == "admin" and passwordEntry.get() == "123":
        tk.messagebox.showinfo("Giriş Başarılı", "Hoşgeldiniz")
    else:
        tk.messagebox.showinfo("Giriş Başarısız", "Kullanıcı adı veya şifre hatalı")

#---------------------------------------------

#------------------Button------------------
controlButton = Button(root, text = "Giriş ",font="bold", width=30 , command= userControl)
controlButton.place(x=30, y=200)



#------------------------------------------
root.mainloop()