from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
import  os
from Scanner import scanner
class frame3 :
    def __init__(self,master,filePath,contents):
        self.contents=contents
        self.scanner = scanner(self.contents)
        self.main=master
        self.Master = Frame(master)
        self.Master.pack(side=TOP)
        self.master_will_be_deleted = Frame(master)
        self.master_will_be_deleted.pack(side=BOTTOM)
        self._4_buttons_master = Frame(self.main)
        self._4_buttons_master.pack(side=TOP)
        self.save = Frame(self.main)
        self.save.pack(side=BOTTOM)
        self.path=filePath
        self.Scan_Button = Button(self.master_will_be_deleted, text=" Scan ", command=self.Scan, font="arial 15 italic", width=20)
        self.Scan_Button.pack(side=BOTTOM)
    def Scan(self):
        self.scanner.Scan()
        self.Scan_Button.destroy()
        self.Master.pack_forget()
        self.Master.destroy()
        self.Master = Frame(self.main)
        self.Master.pack(side=TOP)
        self.show_Label(self.scanner.outTokens())
        self.Save_Button = Button(self.master_will_be_deleted, text=" Save ", command=self.Save, font="arial 15 italic",width=20)
        self.Save_Button.pack(side=BOTTOM)
    def filedialog(self):
        filename=filedialog.asksaveasfilename(title="Save File")
        return filename
    def Save(self):
        self.path = self.filedialog()
        if self.path != "":
            f = open(self.path, "w")
            f.write(self.scanner.outTokens())
            f.close()



    def show_Label(self,contents=""):

        def myfunction(event):
            canvas.configure(scrollregion=canvas.bbox("all"), width=1000, height=500)

        canvas = Canvas(self.Master)
        self.scroll = Frame(self.Master)
        self.scroll.pack(side=BOTTOM,fill="x")
        self.frame = Frame(canvas)
        myscrollbar = Scrollbar(self.Master, command=canvas.yview)
        canvas.configure(yscrollcommand=myscrollbar.set)
        canvas.create_window((0, 0), window=self.frame, anchor='nw')
        self.frame.bind("<Configure>", myfunction)
        myscrollbar.pack(side=RIGHT,fill="y")
        canvas.pack(side=RIGHT)



        myscrollbar1 = Scrollbar(self.scroll, orient="horizontal", command=canvas.xview)
        canvas.configure(xscrollcommand=myscrollbar1.set)
        canvas.create_window((0, 0), window=self.frame, anchor='nw')
        self.frame.bind("<Configure>", myfunction)
        myscrollbar1.pack(side="bottom", fill="x")
        canvas.pack(side="bottom")


        self.text=Text(self.frame,width=5000,height=600)
        self.text.insert(INSERT, contents)

        self.text.pack(side=LEFT)