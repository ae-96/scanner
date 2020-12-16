from tkinter import *
from  Frame3 import  frame3
from  tkinter import  filedialog
from  tkinter import ttk
from Scanner import scanner
class frame2 :
    def __init__(self,master):

        self.newmaster = master
        self.master = Frame(master)
        self.master.pack()
        self.enter_path = Label(self.master, text=" Please Enter Or Browse File Path : ", font="arial 14 italic")
        self.enter_path.grid(row=0, column=0)
        self.path_entry = Entry(self.master, font="arial 14 italic")
        self.path_entry.grid(row=0, column=1)
        self.OK_Button = Button(self.master, text=" OK ", command=self.OK, font="arial 12 italic", width=10)
        self.OK_Button.grid(row=0, column=3)
        self.browse = Button(self.master, text=" Browse File ", command=self.browse, font="arial 12 italic", width=10)
        self.browse.grid(row=1, column=3)
    def filedialog(self):
        self.filename=filedialog.askopenfilename(title="Select A File",filetype=(("ALL","*.*"),("txt","*.txt")))
        return self.filename
    def OK(self):
        self.File_Path = self.path_entry.get()
        self.master.pack_forget()
        self.master.destroy()
        ff = open(self.File_Path, "r")
        contents = ff.read()
        ff.close()
        self.f = frame3(self.newmaster, self.File_Path, contents)
        self.f.show_Label(contents)

    def browse(self):
        self.File_Path = self.filedialog()
        print(self.File_Path)
        if self.File_Path != "":
            self.master.pack_forget()
            self.master.destroy()
            ff = open(self.File_Path, "r")
            contents = ff.read()
            ff.close()
            self.f = frame3(self.newmaster, self.File_Path, contents)
            self.f.show_Label(contents)