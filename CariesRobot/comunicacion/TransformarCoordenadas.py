import serialArduino as sa


class TransformarCoordenadas:

    def cordenadas(self, coordenadaX,coordenadaY):
        print coordenadaX
        print coordenadaY

        #enviar coordenadas trasformadas en coordenadas cartecianas
        #usables para porcesar por el brazo robotico
        sa.sendData(coordenadaX, coordenadaY)
        sa.closeConnection()