from Tkinter import *

ventana = Tk()

img = PhotoImage(file='captura.jpg')
widget = Label(ventana, image=img).pack()
ventana.mainloop()
