import datetime
import time
import cv2
import os
import logging

class Camara:
    def Cam(self):
        try:
            self.cap = cv2.VideoCapture(0)
            time.sleep(2)
            while 1:
                # Capture of image and convert to RGB -> HSV
                ret, self.imagen = self.cap.read()

                cv2.imshow('Camara', self.imagen)
                tecla = cv2.waitKey(5) & 0xFF
                if tecla == 27:
                    try:
                       ts = datetime.datetime.now()
                       filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H"))
                       p = os.path.sep.join(("photo", filename))
                       # save the file
                       cv2.imwrite(p, self.imagen.copy())
                       # print("[INFO] saved {}".format(filename))
                       logging.info("Se guardo la imagen correctamente {}".format(filename))
                       break

                    except(NameError):
                       logging.error("No se pudo guardar la imagen, revise el path del directorio")
            cv2.destroyAllWindows()
        except(RuntimeError, IOError):
            logging.error("Error inesperado en tiempo de ejecucion")





















