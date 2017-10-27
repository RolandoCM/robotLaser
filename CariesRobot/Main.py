from comunicacion.TransformarCoordenadas import TransformarCoordenadas
from procesarImagen.Coordenadas import Coordenadas

# modulo de captura de imagen
#Camara().Cam()
#time.sleep(5)

#modulo para Remover el fondo de la Imagen
#RemoverFondo().remove()

#Clousterizar la Imagen kmeans/kmeansImage.py
#KmeansImage().cluster()

# optener las coordenadas para enviar por modulo de comunicacion
coordenadaX, coordenadaY=Coordenadas().optener()


#paso de coordenadas a modulo para actuador
TransformarCoordenadas().cordenadas(coordenadaX, coordenadaY)