import cv2
import logging

class Coordenadas:
    def optener(self):
        try:
            image = cv2.imread('photo/final.jpg')
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
            cv2.imshow('gray', gray)
            cv2.imshow('origin', origin)

            # print len(coordenadaX)
            # print len(coordenadaY)
            logging.info("La imagen se proceso y se optubieron las coordenadas")
            return coordenadaX, coordenadaY
        except (IOError, RuntimeError):
            logging.error("Error no verifique si existe el archivo o faltan librerias")

        cv2.destroyAllWindows()