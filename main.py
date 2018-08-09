import cv2
from tkinter import *
import numpy as np
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename

class Hsv():
    def __init__(self):
        self.h = 0
        self.s = 0
        self.v = 0

    def upd_h(self, h):
        self.h = int(h)
        update_mask()

    def upd_s(self, s):
        self.s = int(s)
        update_mask()

    def upd_v(self, v):
        self.v = int(v)
        update_mask()

    def get(self):
        return (self.h, self.s, self.v)

def update_mask():
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
    h_min = np.array(hsv1.get(), np.uint8)
    h_max = np.array(hsv2.get(), np.uint8)
    raw_mask = cv2.inRange(hsv, h_min, h_max)
    mask = cv2.bitwise_and(hsv, hsv, mask=raw_mask)
    res = ImageTk.PhotoImage(Image.fromarray(mask))
    print(hsv1.get(), hsv2.get())
    can.itemconfig(area, image = res)

hsv1 = Hsv()
hsv2 = Hsv()
path = askopenfilename()
img = cv2.imread(path)
settings = Tk()
can = Canvas()
can.pack(side='top', fill='both', expand='yes')  
area = can.create_image(0, 0, image=ImageTk.PhotoImage(file=path), anchor='nw')
s_h1 = Scale(settings, from_=0, to=255, orient=HORIZONTAL, command=hsv1.upd_h)
s_h1.pack()
s_s1 = Scale(settings, from_=0, to=255, orient=HORIZONTAL, command=hsv1.upd_s)
s_s1.pack()
s_v1 = Scale(settings, from_=0, to=255, orient=HORIZONTAL, command=hsv1.upd_v)
s_v1.pack()
s_h2 = Scale(settings, from_=0, to=255, orient=HORIZONTAL, command=hsv2.upd_h)
s_h2.pack()
s_s2 = Scale(settings, from_=0, to=255, orient=HORIZONTAL, command=hsv2.upd_s)
s_s2.pack()
s_v2 = Scale(settings, from_=0, to=255, orient=HORIZONTAL, command=hsv2.upd_v)
s_v2.pack()
settings.mainloop()



