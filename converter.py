from tkinter import *
from tkinter import filedialog as fd
import pathlib
from pdf2docx import parse

def searchFile():
    file=fd.askopenfilename()
    youPath.config(state='normal')
    youPath.delete('1',END)
    youPath.insert('1',file)
    youPath.config(state='readonly')

def convertTo():
    filePdf=youPath.get()
    fileWord=pathlib.Path(filePdf)
    fileWord=fileWord.stem + '.docx'
    parse(filePdf,fileWord)
    Label(screen, text="You are converting success!", font='Arial 15 bold').pack(pady=20)


screen=Tk()
screen.title('Converter PDF to Word')
screen.geometry('500x500')
screen.resizable(width=False,height=False)
screen['bg']='white'
Button(screen, text="Select you File", font='Arial 15 bold', fg='green', bg='coral', command=searchFile).pack()
label=Label(screen, text='You Path', bg='gold', font="Arial 20 bold",fg='red')
label.pack(pady=10)
youPath=Entry(screen, width=70, state='readonly')
youPath.pack(pady=10)
convertButton=Button(screen, text="He is converting to WORD", font='Arial 15 bold', fg='green', bg='coral', command=convertTo).pack(pady=50)
screen.mainloop()
