#!/usr/bin/env python
import Tkinter
import Tkinter as tk
import Tkinter as tki
import datetime
from Tkinter import *
from ttk import Separator
import time

import cv2
import numpy as np


class Interfaz():
    def __init__(self):

        self.window = Tkinter.Tk() #crea la ventana principal
        self.window.wm_title("Laser Dental")
        self.window.geometry("1300x600+10+10")
        self.frame=None

        #Graphics window
        self.imageFrame = tk.Frame(self.window, width=600, height=400, bg="red")
        self.separadorM = Separator(self.window, orient=HORIZONTAL) #separador horizontal entre menu superior y elementos center
        self.f_menuSuperior = tk.Frame(self.window,width=1300, height=100, bg="#008080")
        self.separatorV1 = Separator(self.window, orient=VERTICAL) #separador vertical entre menu izquierda y frame camara
        self.separatorV2 = Separator(self.window, orient=VERTICAL) #separador vertical entre cuadro de informacion y frame camara
        self.f_Informacion_Der = tk.Frame(self.window,width=400, height=400,bg="#008080")
        self.f_menuIzq = tk.Frame(self.window,width=250,height=400, bg = "#008080")
        self.f_Informacion_Sub = tk.Frame(self.window, width=1300, height = 100, bg="green")

        #posicion de los frames en la pantalla principal
        self.f_menuSuperior.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.separadorM.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady = 5)
        self.f_menuIzq.pack(side=LEFT, fill=BOTH, expand=False, padx=5, pady=5)
        self.f_Informacion_Der.pack(side=RIGHT, fill=BOTH, expand=False, padx=5,pady=5)
        self.separatorV1.pack(side=LEFT, fill=BOTH, expand=True, padx= 5, pady=5 )
        self.separatorV2.pack(side=RIGHT, fill=BOTH, expand=True, padx= 5, pady=5 )
        self.imageFrame.pack(side=TOP, expand=False, padx=5, pady=5)
        self.f_Informacion_Sub.pack(side = TOP, fill=BOTH, expand=True,padx=5,pady=5)

        self.btn_foto = tki.Button(self.f_menuIzq, width= 10, height=10,text="Camara", bg="blue", command=self.Funtion)
        self.btn_foto.grid(row=0, column=0, padx=5, pady=5)
        self.informacion_L=Label(self.f_Informacion_Der, text="informacion", width=50, height=30, bg="blue")
        self.informacion_L.pack(side=TOP)
        #Interfaz.show_frame(self)
        self.window.mainloop()
    def Funtion(self):
       Interfaz.Camera(self)



    ##-------------------------------------- block camera ---------------------------------------------------------

    def Camera (self):

        # Capture video frames
        self.cap = cv2.VideoCapture(0)
        time.sleep(2)

        while (1):
            # Capturamos una imagen y la convertimos de RGB -> HSV
            ret, self.imagen = self.cap.read()
            if ret ==True:
                hsv = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2HSV)
                # Establecemos el rango de colores que vamos a detectar
                # En este caso de verde oscuro a verde-azulado claro
                verde_bajos = np.array([0, 0, 64], dtype=np.uint8)
                verde_altos = np.array([220, 92, 136], dtype=np.uint8)

                # Crear una mascara con solo los pixeles dentro del rango de verdes
                mask = cv2.inRange(hsv, verde_bajos, verde_altos)

                # Encontrar el area de los objetos que detecta la camara
                moments = cv2.moments(mask)
                area = moments['m00']

                # Descomentar para ver el area por pantalla
                # print area
                if (area > 2000000):
                    # Buscamos el centro x, y del objeto
                    x = int(moments['m10'] / moments['m00'])
                    y = int(moments['m01'] / moments['m00'])

                    # Mostramos sus coordenadas por pantalla
                    print "x = ", x
                    print "y = ", y

                    # Dibujamos una marca en el centro del objeto
                    cv2.rectangle(self.imagen, (x, y), (x + 2, y + 2), (0, 0, 255), 2)

                # Mostramos la imagen original con la marca del centro y
                # la mascara
                cv2.imshow('mask', mask)
                cv2.imshow('Camara', self.imagen)
                tecla = cv2.waitKey(5) & 0xFF
                if tecla == 27:
                    ts = datetime.datetime.now()
                    filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
                    p = os.path.sep.join(("photo", filename))
                    # save the file
                    cv2.imwrite(p, self.imagen.copy())
                    print("[INFO] saved {}".format(filename))
                    break


        cv2.destroyAllWindows()
    ##---------------------------------------------------------------- block camera     --------