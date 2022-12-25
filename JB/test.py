from tkinter import *
from tkinter import messagebox
import sqlite3
import customtkinter

def mekanGuncelle(id,uyelikTuru, uyelikSonTarih):
    mekanKayit = [uyelikTuru, uyelikSonTarih,id]
    conn = sqlite3.connect("Jukebox.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE tbl_mekan SET mekanUyelikTuru=?, uyelikSonBulmaTar=? WHERE rowid=?",mekanKayit)

    conn.commit()
    conn.close()
    messagebox.showinfo("Mekan Ekleme", "Islem Basarili")


rootu = Tk()
rootu.resizable(False, False)
rootu.title("JukeBox")
rootu.geometry("400x230+1310+230")
rootu.iconbitmap("img/JukeBox.ico")
rootu.config(bg="black")

lblMekanEkle = customtkinter.CTkLabel(rootu, text="Mekan Guncelleme Ekrani", font=("Arial", 20))
lblMekanEkle.pack()
frameMekanEkle = Frame(rootu, bg="black")
frameMekanEkle.place(x=80, y=60)

lblID= customtkinter.CTkLabel(frameMekanEkle, text="ID:", text_color="White")
entryID= customtkinter.CTkEntry(frameMekanEkle)
lblMekanUyelikTuru = customtkinter.CTkLabel(frameMekanEkle, text="Mekan Uyelik Türü:", text_color="White")
uyelikTurleri = ["Kullanim Bedeli Odemeli", "Gelen Istek Ucretinden Komisyonlu"]
combaBoxMekanUyelikTuru = customtkinter.CTkComboBox(frameMekanEkle, values=uyelikTurleri)
lblMekanUyelikSonBulmaTarihi = customtkinter.CTkLabel(frameMekanEkle, text="Uyelik Son Tarih:", text_color="White")
entryMekanUyelikSonBulmaTarihi = customtkinter.CTkEntry(frameMekanEkle)
btnGuncelle = customtkinter.CTkButton(frameMekanEkle, text="Guncelle", width=50, command=lambda: mekanGuncelle(entryID.get(),
                                                                                                               combaBoxMekanUyelikTuru.get(),
                                                                                                               entryMekanUyelikSonBulmaTarihi.get()))

lblID.grid(row=0,column=0,pady=3, sticky=W)
entryID.grid(row=0,column=1,pady=3, padx=3)
lblMekanUyelikTuru.grid(row=1, column=0, pady=3)
combaBoxMekanUyelikTuru.grid(row=1, column=1, pady=3, padx=3)
lblMekanUyelikSonBulmaTarihi.grid(row=2, column=0, sticky=W, pady=3)
entryMekanUyelikSonBulmaTarihi.grid(row=2, column=1, pady=3, padx=3)
btnGuncelle.grid(row=3, column=1, pady=3, sticky=E)

rootu.mainloop()