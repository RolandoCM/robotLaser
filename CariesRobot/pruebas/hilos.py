from threading import Thread

def hola():
    print "hola"
def otro():
    print "otro"



hilo1 = Thread(target=hola())
hilo2 = Thread(target=otro())

while(True):
    hilo1.start()
    hilo2.start()