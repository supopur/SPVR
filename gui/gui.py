from tkinter import *
from pyautogui import press, size
#import threading
from PIL import ImageTk, Image
from os import popen

def loading(time : int = 0):
    root = Tk()
    img = ImageTk.PhotoImage(Image.open('gui/wait.svg'))
    panel = Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")

    root.attributes('-fullscreen',True)
    root.after(time, root.destroy)
    root.mainloop()
def yn(yes : bool, time : int = 0):
    root = Tk()
    if yes == True:
        img = ImageTk.PhotoImage(Image.open('gui/yn.jpg'))
    else:
        img = ImageTk.PhotoImage(Image.open('gui/yn.jpg'))
    panel = Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")

    root.attributes('-fullscreen',True)
    root.after(time, root.destroy)
    root.mainloop()
def reload(time : int = 0):
    root = Tk()
    img = ImageTk.PhotoImage(Image.open('gui/reloading.jpg'))
    panel = Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")

    root.attributes('-fullscreen',True)
    root.after(time, root.destroy)
    root.mainloop()
def pressA(time : int = 0):
    
    root = Tk()
    img = ImageTk.PhotoImage(Image.open('gui/activate.jpg'))
    panel = Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")

    root.attributes('-fullscreen',True)
    root.after(time, root.destroy)
    root.mainloop()
def mic(time : int = 0):
    root = Tk()
    img = ImageTk.PhotoImage(Image.open('gui/mic.svg'))
    panel = Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")

    root.attributes('-fullscreen',True)
    root.after(time, root.destroy)
    root.mainloop()



if __name__ == '__main__':
    print('Error: Please import it in a file that is in the same directory as main.py')