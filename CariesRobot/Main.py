'''
 Modulo principal, controla todos los procesos de el sistema
 se encarga de hacer la conexion entre varios modulos y paso de parametros
 Proceso:
 1. Login
 2. Tomar captura de imagen
 3. Guardar camara en carpeta predeterminada por el sistema
 4. Preprocesamiento de imagen con metodos GrapCut e implementacion de mascaras y operaciones de imagenes
        para eliminar el fondo
 5. Clousterizar la imagen sin fondo para identificar el tipo de carie y proceos a realizar
 6. Optener coordenadas de la imagen clousterizada
 7. Procesar coordenadas y usar modulo definido para comunicacion con Arduino
 '''
from procesarImagen.Coordenadas import Coordenadas
from procesarImagen.RemoverFondo import RemoverFondo
from procesarImagen.kmeansImage import kmeans

# modulo de captura de imagen
#Camara().Cam()

#modulo para Remover el fondo de la Imagen

#RemoverFondo().remove()

#Clousterizar la Imagen kmeans/kmeansImage.py

#kmeans().identificarCarie()

# optener las coordenadas para enviar por modulo de comunicacion
#coordenadaX, coordenadaY=Coordenadas().optener()


#paso de coordenadas a modulo para actuador
#TransformarCoordenadas().cordenadas(coordenadaX, coordenadaY)