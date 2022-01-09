from tkinter import *
import sys
def iconwindow(contenedor, nombre):
    if getattr(sys, 'frozen', False) :
          
        if (sys.platform.startswith('win')): 
            contenedor.iconbitmap(sys._MEIPASS+'\\'+nombre+'.ico')
        else:
            logo = PhotoImage(file=sys._MEIPASS+'/'+nombre+'.png')
            contenedor.call('wm', 'iconphoto', contenedor._w, logo)
    else:
          
        if (sys.platform.startswith('win')): 
            contenedor.iconbitmap(nombre+'.ico')
        else:
            logo = PhotoImage(file=nombre+'.png')
            contenedor.call('wm', 'iconphoto', contenedor._w, logo)
