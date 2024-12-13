from tkinter import*
import tkinter.font as font
import math

root = Tk()
root.title("CALCULATOR")
root["bg"] = "white"
root.geometry("310x400")

angka  = font.Font(size=15)

e = Entry(root,width=25,borderwidth=0)
e["font"]= angka
e["bg"] = "white"
e.grid(row = 0,columnspan=4,pady=20,padx=20)


def cetak(nilai):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current)+str(nilai))
def tambah():
    angka_awal = e.get()
    global a_awal
    global mtk
    mtk = "penjumlahan"
    a_awal = int(angka_awal)
    e.delete(0,END)
def kurang():
    angka_awal = e.get()
    global a_awal
    global mtk
    mtk = "pengurangan"
    a_awal = int(angka_awal)
    e.delete(0,END)
def bagi():
    angka_awal = e.get()
    global a_awal
    global mtk
    mtk = "pembagian"
    a_awal = int(angka_awal)
    e.delete(0,END)
def kali():
    angka_awal = e.get()
    global a_awal
    global mtk
    mtk = "perkalian"
    a_awal = int(angka_awal)
    e.delete(0,END)

def sisabagi():
    angka_awal = e.get()
    global a_awal
    global mtk
    mtk = "sisabagi"
    a_awal = int(angka_awal)
    e.delete(0,END)

def pangkat():
    angka_awal = e.get()
    global a_awal
    n_awal = int(angka_awal)
    e.delete(0,END)
    e.insert(0,a_awal **2)

def akar():
    angka_awal = e.get()
    global a_awal
    a_awal = int(angka_awal)
    e.delete(0,END)
    e.insert(0,math.sqrt(a_awal))


def hapus():
    e.delete(0,END)
def samadengan():
    angka_akhir = e.get()
    e.delete(0,END)
    if mtk == "penjumlahan":
        e.insert(0,a_awal + int(angka_akhir))
    elif mtk == "pengurangan":
        e.insert(0,a_awal - int(angka_akhir))
    elif mtk == "pembagian":
        try:
            hitung = a_awal / int(angka_akhir)
            e.insert(0,hitung)
        except ZeroDivisionError:
            e.insert(0,"UNDEFINED")
            
    elif mtk == "perkalian":
        e.insert(0,a_awal * int(angka_akhir))
    elif mtk == "sisabagi":
        e.insert(0,a_awal % int(angka_akhir))


tombol  = Button(root,text="1",padx = 30,bg="white",fg="black", pady = 20,command=lambda:cetak(1))
tombol2  = Button(root,text="2",padx = 30,bg="white",fg="black", pady = 20,command=lambda:cetak(2))
tombol3  = Button(root,text="3",padx = 30,bg="white",fg="black", pady = 20,command=lambda:cetak(3))
tombol4  = Button(root,text="4",padx = 30,bg="white",fg="black", pady = 20,command=lambda:cetak(4))
tombol5  = Button(root,text="5",padx = 30,bg="white",fg="black", pady = 20,command=lambda:cetak(5))
tombol6  = Button(root,text="6",padx = 30,bg="white",fg="black", pady = 20,command=lambda:cetak(6))
tombol7  = Button(root,text="7",padx = 30,bg="white",fg="black", pady = 20,command=lambda:cetak(7))
tombol8  = Button(root,text="8",padx = 30,bg="white",fg="black", pady = 20,command=lambda:cetak(8))
tombol9  = Button(root,text="9",padx = 30,bg="white",fg="black", pady = 20,command=lambda:cetak(9))
tombol0  = Button(root,text="0",padx = 30,bg="white",fg="black", pady = 20,command=lambda:cetak(0))
tomboltambah = Button(root,text="+",padx = 30,bg="white",fg="black", pady = 20,command=tambah)
tombolkurang = Button(root,text="-",padx = 30,bg="white",fg="black", pady = 20,command=kurang)
tombolbagi = Button(root,text="/",padx = 30,bg="white",fg="black", pady = 20,command=bagi)
tombolkali = Button(root,text="x",padx = 30,bg="white",fg="black", pady = 20,command=kali)
tombolpangkat = Button(root,text="x2",padx = 30,bg="white",fg="black", pady = 20,command=pangkat)
tombolakar = Button(root,text="sq2",padx = 25,bg="white",fg="black", pady = 20,command=akar)
tombolsisabagi = Button(root,text="%",padx = 30,bg="white",fg="black", pady = 20,command=sisabagi)
tombolhapus = Button(root,text="C",padx = 30,bg="white",fg="black", pady = 20,command=hapus)
tombolsamadengan = Button(root,text="=",padx = 60,bg="red", pady = 20,command=samadengan)


tombol.grid(row=3,column=0,pady=2)
tombol2.grid(row=3,column=1,pady=2)
tombol3.grid(row=3,column=2,pady=2)
tombol4.grid(row=2,column=0,pady=2)
tombol5.grid(row=2,column=1,pady=2)
tombol6.grid(row=2,column=2,pady=2)
tombol7.grid(row=1,column=0,pady=2)
tombol8.grid(row=1,column=1,pady=2)
tombol9.grid(row=1,column=2,pady=2)
tombol0.grid(row=4,column=1,pady=2)

tombolkali.grid(row=1,column=3,pady=2)
tombolkurang.grid(row=2,column=3,pady=2)
tomboltambah.grid(row=3,column=3,pady=2)
tombolbagi.grid(row=4,column=3,pady=2)
tombolhapus.grid(row=4,column=0,pady=2)
tombolsamadengan.grid(row=5,column=2,columnspan=2)
tombolpangkat.grid(row =5,column=0,pady=2)
tombolakar.grid(row =5,column=1,pady=2)
tombolsisabagi.grid(row =4,column=2,pady=2)



root.mainloop()
