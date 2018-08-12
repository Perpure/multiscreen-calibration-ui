import cv2
import numpy as np
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk


class Hsv:
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
        return self.h, self.s, self.v


def update_mask():
    img = cv2.imread(window.path)
    print(window.path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
    h_min = np.array(hsv1.get(), np.uint8)
    h_max = np.array(hsv2.get(), np.uint8)
    raw_mask = cv2.inRange(hsv, h_min, h_max)
    mask = cv2.bitwise_and(hsv, hsv, mask=raw_mask)
    window.update(mask)
    print(hsv1.get(), hsv2.get())


class MainWindow:
    def __init__(self):
        self.view = None
        self.choose = None
        self.image = None

        self.build_widgets()

    def build_widgets(self):
        self.view = Canvas(settings, width=300, height=300, bg="white")
        self.view.pack()
        s_h1 = Scale(settings, from_=0, to=255, orient=HORIZONTAL, command=hsv1.upd_h)
        s_h1.pack()
        s_s1 = Scale(settings, from_=0, to=255, orient=HORIZONTAL, command=hsv1.upd_s)
        s_s1.pack()
        s_v1 = Scale(settings, from_=0, to=255, orient=HORIZONTAL, command=hsv1.upd_v)
        s_v1.pack()
        s_h2 = Scale(settings, from_=0, to=255, orient=HORIZONTAL, command=hsv2.upd_h)
        s_h2.set(255)
        s_h2.pack()
        s_s2 = Scale(settings, from_=0, to=255, orient=HORIZONTAL, command=hsv2.upd_s)
        s_s2.set(255)
        s_s2.pack()
        s_v2 = Scale(settings, from_=0, to=255, orient=HORIZONTAL, command=hsv2.upd_v)
        s_v2.set(255)
        s_v2.pack()

        choose = Button(settings, text="Open", command=self.choose_file)
        choose.pack()

    def update(self, mask):
        self.image = ImageTk.PhotoImage(Image.fromarray(mask))
        self.view.create_image(0, 0, image=self.image, anchor="center")

    def choose_file(self):
        self.path = askopenfilename()
        self.image = ImageTk.PhotoImage(Image.open(self.path))
        self.view.create_image(0, 0, image=self.image, anchor="center")


hsv1 = Hsv()
hsv2 = Hsv()
settings = Tk()
window = MainWindow()
settings.mainloop()
