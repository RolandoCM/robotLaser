import cv2
import logging
import os
import datetime


class Coordenadas:
    def optener(self):
        try:
            ts = datetime.datetime.now()
            filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H"))
            p = os.path.sep.join(("../photo/procesada/", filename))
            image = cv2.imread(p)
            print p
            origin = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            width, height = gray.shape
            coordenadaX=[]
            coordenadaY=[]
            for x in range(width):
                for y in range(height):
                    if gray[x,y]<100:
                        gray[x,y]=0
                        coordenadaX.append(x)
                        coordenadaY.append(y)
            #cv2.imshow('IMAGEN PROCESADA', gray)
            pathFinal = os.path.sep.join(("../photo/terminada/", filename))
            cv2.imwrite(pathFinal, gray)
            # print len(coordenadaX)
            # print len(coordenadaY)
            logging.info("La imagen se proceso y se optubieron las coordenadas")
            return coordenadaX, coordenadaY
        except (IOError, RuntimeError):
            logging.error("Error no verifique si existe el archivo o faltan librerias")

        cv2.destroyAllWindows()