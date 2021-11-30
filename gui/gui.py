from tkinter import *
from pyautogui import size
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
def reloadMB():
    pass
def pressA():
    pass
def mic():
    pass



if __name__ == '__main__':
    loading(1000)