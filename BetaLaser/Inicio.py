# -*- coding: utf-8 -*-

from Tkinter import *
from Interfaz import Interfaz
import getpass
# Gestor de geometría (pack)
from ttk import Separator
login = Tk()

class Inicio():
    def __init__(self):
        login.title("Acceso")
        login.geometry("400x300+400+200")

        #etiquetas muestra el nombre del campo
        self.userL = Label(login, text="Usuario:")
        self.passwordL = Label(login, text="Contraseña:")

        # Declara dos variables de tipo cadena para contener
        # el usuario y la contraseña:
        self.usuario = StringVar()
        self.clave = StringVar()

        # Realiza una lectura del nombre de usuario que
        # inició sesión en el sistema y lo asigna a la
        # variable 'self.usuario'
        self.usuario.set(getpass.getuser())
        #define cajas de entrada usuario
        self.usuario = Entry(login, textvariable=self.usuario, width=30)
        self.password = Entry(login, textvariable=self.clave, width=30, show="*")
        #barra separadora
        self.separ1 = Separator(login, orient=HORIZONTAL)

        #se define los botones
        self.aceptarB = Button(login, text="Aceptar", command=self.aceptar)
        self.cancelarB= Button(login, text="Cancelar", command=quit)

        # Se definen las posiciones de los widgets dentro de
        # la ventana. Todos los controles se van colocando
        # hacia el lado de arriba, excepto, los dos últimos,
        # los botones,
        self.userL.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.usuario.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
        self.passwordL.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.password.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
        self.separ1.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.aceptarB.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        self.cancelarB.pack(side=RIGHT, fill=BOTH, expand=True, padx=5, pady=5)

        # Cuando se inicia el programa se asigna el foco
        # a la caja de entrada de la contraseña para que se
        # pueda empezar a escribir directamente:

        self.password.focus_set()

        login.mainloop()

    # El método 'aceptar' se emplea para validar la
    # contraseña introducida. Será llamado cuando se
    # presione el botón 'Aceptar'.

    def aceptar(self):
        if self.clave.get() == '':
            print("Acceso permitido")
            print("Usuario:   ", self.usuario.get())
            print("Contraseña:", self.password.get())
            login.destroy()
            interfaz = Interfaz()
        else:
            print("Acceso denegado")

            # Se inicializa la variable 'self.clave'

            self.clave.set("")
            self.password.focus_set()
