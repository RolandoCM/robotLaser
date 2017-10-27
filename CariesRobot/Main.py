import time
import logger.logs

from comunicacion.TransformarCoordenadas import TransformarCoordenadas
from procesarImagen.Camara import Camara
from procesarImagen.Coordenadas import Coordenadas
from procesarImagen.RemoverFondo import RemoverFondo
from procesarImagen.kmeansImage import kmeans

# modulo de captura de imagen
Camara().Cam()
time.sleep(5)

#modulo para Remover el fondo de la Imagen

RemoverFondo().remove()

#Clousterizar la Imagen kmeans/kmeansImage.py
kmeans().identificarCarie()

# optener las coordenadas para enviar por modulo de comunicacion
coordenadaX, coordenadaY=Coordenadas().optener()


#paso de coordenadas a modulo para actuador
TransformarCoordenadas().cordenadas(coordenadaX, coordenadaY)