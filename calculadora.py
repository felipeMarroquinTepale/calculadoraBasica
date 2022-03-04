from tkinter import*
from click import command

from matplotlib.pyplot import text

ventana = Tk()
ventana.title("Calculadora")

i=0

#Entrada
e_texto = Entry(ventana,font=("Calibri 20"),bg="white")

#columspan es para que exista x columnas debajo del cuadro de texto
#padx espacio horizontal de lados entre ventado del cuadro de texto
e_texto.grid(row=0,column=0,columnspan=4,padx=5,pady=5)

#Funciones
def click_boton(valor):
    #variable i es para el numero no lo ponga siempre en el indice 0 si no conforme vaya iterando la i, vaya en indice 0,1,2,3
    global i
    e_texto.insert(i,valor)
    i+=1
#Funcion para borrar valores
def borrar():
    #Borra indice 0 hasta el indice final
    e_texto.delete(0,END)
    #Reseteamos la variable i para que el indice comienze en 0 despues de borrar
    i = 0
#Funcion para hacer operaciones
def operaciones():
    operacion = e_texto.get()
    resultado = eval(operacion)
    e_texto.delete(0,END)
    e_texto.insert(0,resultado)
    i = 0
#Boton
#Witdth =ancho y height=altura
boton1 = Button(ventana,text="1",width=5,height=2,bg="#DCAA4E",command= lambda: click_boton(1))
boton2 = Button(ventana,text="2",width=5,height=2,bg="#DCAA4E",command= lambda: click_boton(2))
boton3 = Button(ventana,text="3",width=5,height=2,bg="#DCAA4E",command= lambda: click_boton(3))
boton4 = Button(ventana,text="4",width=5,height=2,bg="#DCAA4E",command= lambda: click_boton(4))
boton5 = Button(ventana,text="5",width=5,height=2,bg="#DCAA4E",command= lambda: click_boton(5))
boton6 = Button(ventana,text="6",width=5,height=2,bg="#DCAA4E",command= lambda: click_boton(6))
boton7 = Button(ventana,text="7",width=5,height=2,bg="#DCAA4E",command= lambda: click_boton(7))
boton8 = Button(ventana,text="8",width=5,height=2,bg="#DCAA4E",command= lambda: click_boton(8))
boton9 = Button(ventana,text="9",width=5,height=2,bg="#DCAA4E",command= lambda: click_boton(9))
boton0 = Button(ventana,text="0",width=13,height=2,bg="#DCAA4E",command= lambda: click_boton(0))

boton_borrar = Button(ventana,text="AC",width=5,height=2,bg="#DCAA4E",command = lambda: borrar())
boton_parentesis1 = Button(ventana,text="(",width=5,height=2,bg="#DCAA4E",command= lambda: click_boton("("))
boton_parentesis2 = Button(ventana,text=")",width=5,height=2,bg="#DCAA4E",command= lambda: click_boton(")"))
boton_punto = Button(ventana,text=".",width=5,height=2,bg="#DCAA4E",command= lambda: click_boton("."))

boton_div = Button(ventana,text="/",width=5,height=2,bg="#DCAA4E",command= lambda: click_boton("/" ))
boton_mul = Button(ventana,text="x",width=5,height=2,bg="#DCAA4E",command= lambda: click_boton("*"))
boton_sum = Button(ventana,text="+",width=5,height=2,bg="#DCAA4E",command= lambda: click_boton("+"))
boton_rest = Button(ventana,text="-",width=5,height=2,bg="#DCAA4E",command= lambda: click_boton("-"))
boton_igual = Button(ventana,text="=",width=5,height=2,bg="#DCAA4E",command= lambda: operaciones())

#Agregar botones en pantalla
boton_borrar.grid(row=1,column =0, padx=5, pady=5)
boton_parentesis1.grid(row=1,column =1, padx=5, pady=5)
boton_parentesis2.grid(row=1,column =2, padx=5, pady=5)
boton_div.grid(row=1,column =3, padx=5, pady=5)

boton7.grid(row=2,column =0, padx=5, pady=5)
boton8.grid(row=2,column =1, padx=5, pady=5)
boton9.grid(row=2,column =2, padx=5, pady=5)
boton_mul.grid(row=2,column =3, padx=5, pady=5)

boton4.grid(row=3,column =0, padx=5, pady=5)
boton5.grid(row=3,column =1, padx=5, pady=5)
boton6.grid(row=3,column =2, padx=5, pady=5)
boton_sum.grid(row=3,column =3, padx=5, pady=5)

boton1.grid(row=4,column =0, padx=5, pady=5)
boton2.grid(row=4,column =1, padx=5, pady=5)
boton3.grid(row=4,column =2, padx=5, pady=5)
boton_rest.grid(row=4,column =3, padx=5, pady=5)

boton0.grid(row=5,column=0,columnspan=2,padx=5,pady=5)
boton_punto.grid(row=5,column=2,padx=5,pady=5)
boton_igual.grid(row=5,column=3,padx=5,pady=5)

ventana.config(bg="#635D5C")
ventana.mainloop()

