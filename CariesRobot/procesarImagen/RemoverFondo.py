import datetime
import numpy as np
import cv2
import logging
import os

class RemoverFondo:
    def remove(self):
        try:
            #cv2.namedWindow('image', cv2.WINDOW_NORMAL)
            # cargar imagen
            ts = datetime.datetime.now()
            filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H"))
            p = os.path.sep.join(("../photo", filename))
            try:
                imgo = cv2.imread(p)
                #cv2.imshow('IMAGEN ORIGINAL', imgo) #mostramos la imagen origunal
                height, width = imgo.shape[:2]
            except(NameError):
                logging.error("El archivo no se encontro")

            #Create a mask holder
            mask = np.zeros(imgo.shape[:2],np.uint8)

            #Grab Cut the object
            bgdModel = np.zeros((1,65),np.float64)
            fgdModel = np.zeros((1,65),np.float64)

            rect = (10,10,width-30,height-30)
            cv2.grabCut(imgo,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
            mask = np.where((mask==2)|(mask==0),0,1).astype('uint8')
            img1 = imgo*mask[:,:,np.newaxis]

            #Get the background
            background = imgo-img1

            #Change all pixels in the background that are not black to white
            background[np.where((background > [0,0,0]).all(axis = 2))] = [255,255,255]

            #Add the background and the image
            final = background + img1
            gray = cv2.cvtColor(final, cv2.COLOR_BGR2GRAY)

            #cv2.imshow('image', final )
            #cv2.imshow('original', imgo)
            #cv2.imshow('gray',gray)
            try:
                ts = datetime.datetime.now()
                filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H"))
                p = os.path.sep.join(("../photo/procesada", filename))
                cv2.imwrite(p, final)
                logging.info("Imagen procesada satisfactoriamente (Se a removido el fondo de la imagen)")
            except (IOError, NameError):
                logging.error("Error al intentar guardar el archivo")
        except (RuntimeError, IOError):
            logging.error("Error en tiempo de ejecucion")


#k = cv2.waitKey(0)
#if k==27:
#    cv2.destroyAllWindows()