# NAMA  : SAUL SAYERS
# NIM   : 13520094
# TASK 7 SELEKSI ASISTEN IRK

# FILE INI MERUPAKAN FILE UNTUK MAIN PAGE DARI GUI

from tkinter import *

from algorithm import *
import os
from tkinter.filedialog import askopenfile 
import re

rex = re.compile("^[AGCT]+$")

def btn_clicked():
    print()

class ConstantSize() :
    HEIGHT = 702
    WIDTH = 1248

class MainPage(Frame):
    
    '''
    Initializes main component
    '''
    def __init__(self, parent, controller, frames):
        Frame.__init__(self, parent)
        self.solver = Solver()
        self.controller = controller
        self.frames = frames
        self.container = Frame(self)
        self.container.pack(fill="both", expand=True)
        self.path1 = ""
        self.path2 = ""

        self.canvas = Canvas(
            self.container,
            bg = "#ffffff",
            height = ConstantSize.HEIGHT,
            width = ConstantSize.WIDTH)
        self.canvas.place(x = 0, y = 0)
        self.canvas.pack(fill = "both", expand = True)

        self.background_img = PhotoImage(file = f"asset/background.png")
        self.canvas.create_image(
            312.0, 355.0,
            image=self.background_img)

        self.img0 = PhotoImage(file = f"asset/img0.png")
        self.b0 = Button(
            image = self.img0,
            command = lambda: self.upload1())

        self.b0.place(
            x = 1012, y = 24,
            width = 169,
            height = 40)

        self.img1 = PhotoImage(file = f"asset/img1.png")
        self.b1 = Button(
            image = self.img1,
            command = lambda: self.upload2())

        self.b1.place(
            x = 1012, y = 81,
            width = 169,
            height = 40)

        self.img2 = PhotoImage(file = f"asset/img2.png")
        self.b2 = Button(
            image = self.img2,
            command = lambda: self.solve())

        self.b2.place(
            x = 1110, y = 647,
            width = 106,
            height = 39)

        self.runtime = self.canvas.create_text(
            800, 675,
            text = "",
            fill = "#000000",
            font = ("RobotoRoman-Regular", int(15.0)))
        
        self.sol1 = self.canvas.create_text(
            800, 580,
            text = "",
            fill = "#000000",
            font = ("RobotoRoman-Regular", int(10.0)))
    
        self.sol2 = self.canvas.create_text(
            800, 610,
            text = "",
            fill = "#000000",
            font = ("RobotoRoman-Regular", int(10.0)))

        self.sol = self.canvas.create_text(
            800, 641,
            text = "",
            fill = "#000000",
            font = ("RobotoRoman-Regular", int(10.0)))

        self.file1 = self.canvas.create_text(
            800, 50,
            text = "",
            fill = "#000000",
            font = ("RobotoRoman-Regular", int(19.0)))

        self.file2 = self.canvas.create_text(
            800, 105,
            text = "",
            fill = "#000000",
            font = ("RobotoRoman-Regular", int(19.0)))

        self.frm = Frame(self.container)
        self.frm.config(width=750, height = 400)
        self.frm.place(x=470, y = 140)

        b3 = Button(
            text = "Creator",
            command =  lambda:
            [   self.popupuser()
            ])

        b3.place(
            x = 900, y = 24,
            width = 100,
            height = 40)

        b3 = Button(
            text = "Guide",
            command =  lambda:
            [   self.popupguide()
            ])

        b3.place(
            x = 900, y = 81,
            width = 100,
            height = 40)

    def popupuser(self):
        teks = "Created by : Saul Sayers\nNIM : 13520094\n"
        teks += "\n About me?\n"
        teks += "I was born in Surabaya on the third of February, 2002. I attended SMAN 5 Surabaya, i graduated in 2020.\nLuckily, i got the change for SNMPTN and later i got accepted to STEI ITB. I met many wonderful friends here"
        teks += "\n\nAs i entered STEI ITB, i realized my passion for coding and programming.\nI learned many programming languages and frameworks during the timeframe of my college. Im really passionate about my studies."
        teks += "\n\nI am really eager to join IRK LAB (:D)\nSemua mata kuliah paling aku favoritin ada di lab IRK soalnya heheheheheh"
        top= Toplevel(self.controller)
        width = 800
        height = 300
        top.geometry(str(width) + "x" + str(height))
        top.title("Error Message")
        self.labelpesan = Label(top, text= "\n" + teks, font=("Roboto bold", 10))
        self.labelpesan.pack()

    def popupguide(self):
        teks = "- Membuka root dari repository yang telah anda clone dan jalankan program dengan memanfaatkan run.bat yang tersedia.\n\n"
        teks += "- Ambil file input berisi DNA yang akan diperiksa penyelarasan optimalnya.\nProgram akan mendeteksi file input yang salah dan memberikan popup apabila input tidak berupa DNA\n\n"
        teks += "- Setelah memilih kedua file input, silahkan klik tombol solve.\nApabila mengklik tombol solve sebelum memilih input, program akan menampilkan popup error.\n\n"
        teks += "- Output yang diharapkan akan ditampilkan oleh program, berupa alignment,runtime program, matriks tracebacknya.\nUntuk kolom yang berisi warna merah merupakan kolom yang diambil rute tracebacknya.\nDengan catatan, karena rute diagonal bisa diambil saat mismatch ataupun match,\nmaka sebagai pembeda kolom biru merupakan rute diagonal yang diakibatkan karena mismatch sementara merah karena match"
        top= Toplevel(self.controller)
        width = 900
        height = 300
        top.geometry(str(width) + "x" + str(height))
        top.title("Error Message")
        self.labelpesan = Label(top, text= "\n" + teks, font=("Roboto bold", 10))
        self.labelpesan.pack()


    def popup(self,message):
        top= Toplevel(self.controller)
        width = 350
        height = 50
        top.geometry(str(width) + "x" + str(height))
        top.title("Error Message")
        self.labelpesan = Label(top, text= "\n" + message, font=("Roboto bold", 10))
        self.labelpesan.pack()

    def upload1(self):
        pathfile = askopenfile(mode = "r", filetypes = [("Text File", "*.txt")])
        if pathfile is not None:
            file = open(pathfile.name)
            m = rex.match(file.read())
            if m != None:
                self.path1 = pathfile.name
                self.canvas.itemconfig(self.file1, text=os.path.basename(self.path1))
            else : 
                self.popup("File not AGCT")

    def upload2(self):
        pathfile = askopenfile(mode = "r", filetypes = [("Text File", "*.txt")])
        if pathfile is not None:
            file = open(pathfile.name)
            m = rex.match(file.read())
            if m != None:
                self.path2 = pathfile.name
                self.canvas.itemconfig(self.file2, text=os.path.basename(self.path2))
            else : 
                self.popup("File not AGCT")

    def solve(self):
        if self.path1 != "" and self.path2 != "":
            self.solver.setDNA(self.path1,self.path2)
            if abs(len(self.solver.DNA1) - len(self.solver.DNA2)) > 5:
                self.popup("Selisih dna lebih dari 5")
                return
            self.solver.needlemanWunsch()

            ukuran = max(len(self.solver.DNA1),len(self.solver.DNA2))
            if 3 <= ukuran <= 7:
                ukuran = 10
            elif 8 <= ukuran <= 15 :
                ukuran = 8
            elif 16 <= ukuran <= 25 :
                ukuran = 6
            elif 26 <= ukuran <= 35 :
                ukuran = 4
            elif 36 <= ukuran <= 45 :
                ukuran = 2
            else :
                ukuran = 1

            for widget in self.frm.winfo_children():
                widget.destroy()

            for i in range(len(self.solver.matrix)):
                for j in range (len(self.solver.matrix[0])):
                    if sama([i,j], self.solver.points):
                        warna = "red"
                    elif sama([i,j], self.solver.points2):
                        warna = "blue"
                    else :
                        warna = "white"
                    self.table = Entry(self.frm, font=('Arial',ukuran,'bold'), width=ukuran, justify='center', bg = warna)
                    self.table.grid(row=i, column=j)
                    self.table.insert(END, self.solver.matrix[i][j])
                    # self.table.configure(state='readonly')
            
            # baris = len(self.solver.DNA2) + 1
            # kolom = len(self.solver.DNA1) + 1
            # self.table.grid(row = baris, column = kolom)
            # self.table.config({"background": "Red"})

            # for r in self.solver.route:
            #     if r == "D":
            #         baris == -1
            #         kolom == -1
            #         self.table.grid(row = baris, column = kolom)
            #         self.table.config(bg= "Orange")
            #     elif r == "M":
            #         baris == -1
            #         kolom == -1
            #         self.table.grid(row = baris, column = kolom)
            #         self.table.config(bg= "Red")
            #     elif r == "L":
            #         kolom == -1
            #         self.table.grid(row = baris, column = kolom)
            #         self.table.config(bg= "Red")
            #     else :
            #         baris == -1
            #         self.table.grid(row = baris, column = kolom)
            #         self.table.config(bg= "Red")
            
            self.canvas.itemconfig(self.runtime, text=str(self.solver.runtime) + " ms")
            self.canvas.itemconfig(self.sol1, text=self.solver.DNA1Sol)
            self.canvas.itemconfig(self.sol2, text=self.solver.DNA2Sol)
            self.canvas.itemconfig(self.sol, text=self.solver.sol)
        else : 
            self.popup("Input file first!")