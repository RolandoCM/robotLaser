import datetime
import cv2
import os

from comunicacion.TransformarCoordenadas import TransformarCoordenadas
from procesarImagen.Coordenadas import Coordenadas
from procesarImagen.RemoverFondo import RemoverFondo
from procesarImagen.kmeansImage import kmeans

class IniciarProceso:
    def procesar(self):
        # modulo de captura de imagen
        #Camara().Cam()
        # modulo para Remover el fondo de la Imagen

        RemoverFondo().remove()

        # Clousterizar la Imagen kmeans/kmeansImage.py

        kmeans().identificarCarie()

        # optener las coordenadas para enviar por modulo de comunicacion
        coordenadaX, coordenadaY=Coordenadas().optener()


        # paso de coordenadas a modulo para actuador
        TransformarCoordenadas().cordenadas(coordenadaX, coordenadaY)


    def __init__(self):
        self.procesar()