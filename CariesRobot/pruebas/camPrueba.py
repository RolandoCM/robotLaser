import os

import cv2
import Tkinter as tk

import datetime

import logging
from PIL import Image, ImageTk
from ProcesoAutomatico import IniciarProceso


class vid():
    def __init__(self,cam,root,canvas):
        self.cam = cam
        self.root = root
        self.canvas = canvas

    def update_video(self):
        self.readsuccessful, self.f = self.cam.read()
        self.gray_im = cv2.cvtColor(self.f, cv2.COLOR_BGR2RGB)
        self.a = Image.fromarray(self.gray_im)
        self.b = ImageTk.PhotoImage(image=self.a)
        self.canvas.create_image(0,0,image=self.b,anchor=tk.NW)
        self.root.update()
        self.root.after(33,self.update_video)
        return self.f
    def capture (self):
        ts = datetime.datetime.now()
        filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H"))
        p = os.path.sep.join(("../photo", filename))
        # save the file
        img = x.update_video()
        cv2.imwrite(p, img)
        print("[INFO] saved {}".format(filename))
        logging.info("Se guardo la imagen correctamente {}".format(filename))
    def procesoAutomatico(self):
        IniciarProceso()
        print "proceso"

if __name__ == '__main__':
    root = tk.Tk()
    root.config(background="#0B4C5F")
    root.resizable(width=False, height=False)
    videoframe = tk.LabelFrame(root,text='Video en tiempo real', bg="#0B615E")
    canvas = tk.Canvas(videoframe, width=640, height=480,  bg="#0B615E")
    canvas.grid(column=0, row=0)
    cam = cv2.VideoCapture(0)
    x = vid(cam,root,canvas)

    root.after(0,x.update_video)



    icon = tk.PhotoImage(file="../img/logoBrazo2.png")
    iconLabel = tk.Label(root, image=icon)
    iconLabel.grid(column=0, row=0)
    iconApp = tk.PhotoImage(file="../img/image3344.png")
    iconAppLabel = tk.Label(root, image=iconApp)
    iconAppLabel.grid(column=3, row=0)
    izqFrame = tk.Frame(root, width=300, height=500, bg="#008080")
    derFrame = tk.Frame(root, width=300, height=500, bg="#008080")
    footer = tk.Frame(root, width=300, height=200, bg="#008080")
    footerDer = tk.Frame(root, width=290, height=50, bg="#008080")
    footerIzq = tk.Frame(root, width=290, height=50, bg="#008080")

    button = tk.Button(text='Cerrar', master=footer, command=root.destroy)
    btnCapture = tk.Button(text='Capturar', master=footer, command=x.capture)
    btnCancel = tk.Button(text='Cancelar', master=footer, command=x.procesoAutomatico)

    information="hola"

    headIzq = tk.Label(text="Informacion del proceso", bg="#0B615E", master=izqFrame, width=36)
    headIzq.grid(column=0, row=0)
    info = tk.Label(text=information, bg="#008080", master=izqFrame, height=35, width=36)
    info.grid(column=0, row=1)

    headDer = tk.Label(text="Information general", bg="#0B615E", master=derFrame, width=36)
    headDer.grid(column=0, row=0)
    infoDer = tk.Label(text="hola", bg="#008080", master=derFrame, height=35, width=36)
    infoDer.grid(column=0, row=1)

    videoframe.grid(column=1, row=1, columnspan=1, rowspan=1, padx=5, pady=5, ipadx=5, ipady=5)


    izqFrame.grid(column=0, row=1)
    derFrame.grid(column=3, row=1)
    footer.grid(column=1, row=2)
    footerDer.grid(column=3, row=2)
    footerIzq.grid(column=0, row=2)

    button.grid(column=0, row=1)
    btnCapture.grid(column=1, row=1)
    btnCancel.grid(column=3, row=1)



    root.mainloop()
    del cam