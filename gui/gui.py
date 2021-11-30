from tkinter import *
from pyautogui import size
import threading

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

def loading():
    global run
    run = True
    root = Tk()

    frameCnt = 8
    frames = [PhotoImage(file='loading.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]
    def update(ind):

        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        label.configure(image=frame)
        root.after(100, update, ind)
    label = Label(root)
    label.pack()
    root.after(0, update, 0)
    root.attributes('-fullscreen',True)
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
    loading()