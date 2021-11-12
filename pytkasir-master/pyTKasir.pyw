# file: pyTKasir.py

from tkinter import *
from menuUtama import MenuUtama
from buatDataKasir import DatabaseToko

def run():
    database = DatabaseToko(file="pytkasir-master/data/datatoko.db")

    root = Tk() 
    pytkasir = MenuUtama(root, "Larisy Corner")
    root.mainloop()
    
if __name__ == '__main__':
    run()
