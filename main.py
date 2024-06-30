
from tkinter import *
window =Tk()
window.title("")
window.minsize(600 ,500)
window.config(padx=30,pady=30)

def hesapla():
    boy=boy_data.get()
    kilo=kilo1.get()

    if kilo=="" or boy=="":
        sonuc.config(text="Değerleri boş bırakmayınız")
    else:
        try:
            bmi=float(kilo) / ((float(boy)/100) ** 2)
            sonuc0=sonuc_degeri(bmi)
            sonuc.config(text=sonuc0)
        except:
            sonuc.config(text="Değerleri düzgün giriniz!!!")

kg_label =Label(text="Kilonuzu giriniz(kg)",width=20)
kg_label.pack()

kilo1=Entry(window,width=20)
kilo1.pack()

boy_label =Label(text="Boyunuzu giriniz(cm)",width=20)
boy_label.pack()

boy_data=Entry(window,width=20)
boy_data.pack()

hesapla=Button(text="Hesapla",command=hesapla)
hesapla.pack()

yazi=Label(text="Vücut Kütle İndeksi Hesaplayıcı")
yazi.place(x=50,y=150)
yazi.config(font=('Courier', 20))
sonuc=Label(text="")
sonuc.pack()

def sonuc_degeri(bmi):
    sonuc_yazisi = f"Vücut Kütle İndeksiniz:{round(bmi,2)} Siz  "
    if bmi <=18.5:
        sonuc_yazisi +="zayıfsınız"
    elif bmi>=18.6 and bmi<=24.9:
        sonuc_yazisi+="normalsiniz"
    elif bmi>=25 and  bmi<= 29.9:
        sonuc_yazisi+="kilolu"
    elif bmi>=30:
        sonuc_yazisi+="obezsiniz"
    return sonuc_yazisi
window.mainloop()
