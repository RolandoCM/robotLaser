# !/usr/bin/python
# -*- coding: utf-8 -*-
import time
import serial
import logging


try:
    arduinoPort = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
except IOError:
    logging.error('No se puede establecer conexión con el arduino')

def sendData(coordinateX, coordinateY):
    coordinates=str(coordinateX)+str(coordinateY)
    coordinates='k'
    print coordinates
    try:
        arduinoPort.setDTR(False)
        time.sleep(0.3)
        arduinoPort.flushInput()
        arduinoPort.flushOutput()
        arduinoPort.setDTR()
        logging.info('Estado del puerto -- '+str(arduinoPort.isOpen()))
        logging.info('DUMP de la configuración -- ' + str(arduinoPort))
        while True:
            # sleep to connection init
            time.sleep(0.8)
            arduinoPort.write(coordinates)
            getSerialValue = arduinoPort.readline()
            print '\nValor retornado de Arduino: %s' % (getSerialValue)
    except (IOError, RuntimeError, NameError):
        logging.error("Error en cominicación con arduino")
    except:
        logging.error('Error inesperado')

# Close serial port
def closeConnection():
    arduinoPort.close()
