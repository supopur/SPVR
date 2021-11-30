import threading
import gui

x = threading.Thread(target=gui.loading(), args=())
x.start()
print("test")