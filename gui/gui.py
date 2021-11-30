from tkinter import *
from pyautogui import size
import threading
from PIL import ImageTk, Image

def main():
    x, y = size()
    print(x, y)
    x, y = str(x), str(y)
    window = Tk()
    window.title('SpeechONeverWorkO')
    window.geometry(x + 'x' + y)
    window.attributes('-fullscreen',True)
    #makes canvas
    canvas = Canvas(window, width=800, height=800)
    canvas.pack() # this makes it visible
    #image loading time
    img = PhotoImage(file='loading.gif', format="gif -index 2")
    image = canvas.create_image(10, 10, anchor=NW, image=img)

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