from tkinter import *
from pyautogui import press, size
import threading
from PIL import ImageTk, Image

def loading(time : int = 0):
    root = Tk()
    img = ImageTk.PhotoImage(Image.open('wait.svg'))
    panel = Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")

    root.attributes('-fullscreen',True)
    root.after(time, root.destroy)
    root.mainloop()
def yn(yn : bool):
    pass
def reload(time : int = 0):
    root = Tk()
    img = ImageTk.PhotoImage(Image.open('reloading.jpg'))
    panel = Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")

    root.attributes('-fullscreen',True)
    root.after(time, root.destroy)
    root.mainloop()
def pressA(time : int = 0):
    root = Tk()
    img = ImageTk.PhotoImage(Image.open('activate.jpg'))
    panel = Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")

    root.attributes('-fullscreen',True)
    root.after(time, root.destroy)
    root.mainloop()
def mic():
    pass



if __name__ == '__main__':
    reload(10000)