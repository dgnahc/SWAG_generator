from tkinter import *
from tkinter import filedialog
from os import path
from tkinter import Menu

class GUI:
    def __init__(self, window):
        self.window = window
        window.geometry('500x400')
        fm = Frame(window)
        Label(fm, text="Welcome to SAWG generator!", height=8, font = ("Consolas")).pack(side=TOP)
        Button(fm, text="Upload PDF file", command=self.uploadFile, font=("Consolas",12), bd=1, bg="black", fg="white").pack(side=TOP, expand=YES)
        fm.pack(fill=BOTH, expand=YES)

    def uploadFile(self):
        # TODO: how to read in(extract) pdf file...
        file = filedialog.askopenfilename(title = "Select file", filetypes= (("Text files","*.txt"),("PDF files","*.pdf")))
        print(file)

        
if __name__ == "__main__":
    root = Tk(className=' SWAG generator')    
    display = GUI(root)    
    root.mainloop()