# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Admin"
__date__ = "$Sep 27, 2020 8:58:37 PM$"

import tkinter
import random

if __name__ == "__main__":
    #List2 Warna
    colours=['Red','Blue','Green','Pink','Black','Yellow',
             'Orange','White','Purple','Brown']
    score=0
    #Penggunaan Waktu
    time = 60
    #Untuk alur fungsi Games
    def mulaigame(event):
        if time==60:
            countdown()
        #untuk menjalankan fungsi dan memilih warna
        nextcolour()

    def nextcolour():
        #untuk menyatakan Score yang didapat
        global score
        global time
        
        #jika Games sedang dimulai
        if time>0:
            #buat kolom teks aktif
            e.focus_set()
            #jika warna dan kolom teks sama
            if (e.get().lower() == colours[1].lower()):
                score += 1 
            #untuk membersihkan kolom teks
            e.delete(0, tkinter.END)
            random.shuffle(colours)
            
            label.config(fg=str(colours[1]), text=str(colours[0]))
            #update Score
            scoreLabel.config(text="Score: " + str(score))
            
                
    def countdown():
        global time
        #jika Game udah mulai
        if time > 0:
            #pengurangan waktu
            time -= 1
            #update sisa waktu ke label
            timeLabel.config(text="Waktu Anda Tersisa : " + str(time))
            #menjalankan fungsi setelah 1 detik
            timeLabel.after(1000,countdown)
    #code untuk Driver
    #Code Untuk buat GUI
    root = tkinter.Tk()
    #untuk menentukan Title/judul
    root.title("ColorGames")
    #untuk menentukan ukuran
    root.geometry("375x200")
    #untuk menambahkan intruksi label
    intruction = tkinter.Label(root, text="Ketikan Kata sesuai Warnanya,bukan sesuai nama warnanya",font=('Helvetica',12))                    
    intruction.pack()
    #untuk menambahkan score label
    scoreLabel = tkinter.Label(root, text="Press Enter to Start",font=('Helvetica',12))
    scoreLabel.pack()
    #untuk menambahkan tempat waktu
    timeLabel = tkinter.Label(root,text="Waktu Anda Tersisa : " + str(time),font=('Helvetica',12))
    timeLabel.pack()
    #untuk menampilkan Waktu habis
    #untuk menampilkan Warna
    label = tkinter.Label(root,font=('Helvetica', 60))
    label.pack()
    #menambahkan Kolom Teks
    e=tkinter.Entry(root)
    root.bind('<Return>', mulaigame)
    e.pack()
    #untuk focus ke Kolom Teks
    e.focus_set()
    #untuk memulai GUI
    root.mainloop()
    
                        
                              