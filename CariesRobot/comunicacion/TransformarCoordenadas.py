''' Este es un mega '''
#1 mm = 3.779528 px; 1 px = 0.264583 mm

import serialArduino as sa

class TransformarCoordenadas:

    def cordenadas(self, coordenadaX,coordenadaY):
        archivoCoordenadas = open("coordenadas.txt","w")
        xArduino = []
        yArduino = []
        PIXEL = 0.264583
        totalCoordenadas = len(coordenadaX)
        print coordenadaX
        print coordenadaY
        for x in range(totalCoordenadas):
            xArduino.append((float(coordenadaX[x])*PIXEL))
            yArduino.append((float(coordenadaY[x])*PIXEL))
        print xArduino
        print yArduino
        #for x in xArduino:
         #   archivoCoordenadas.write(x)
        #enviar coordenadas trasformadas en coordenadas cartecianas
        #usables para porcesar por el brazo robotico

        #sa.sendData(coordenadaX, coordenadaY)
        #sa.closeConnection()