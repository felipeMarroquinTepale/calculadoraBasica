from tkinter import *
import re
import os
import threading
import time

#192.168.1.69

def ip():
    # aqui ponemos el metodo que va a llamar a los otros
    cadenaEntrante = entrada.get()

    if cadenaEntrante[1] == '0': 
        threading.Thread(target=a).start()
    elif cadenaEntrante[1] == '7':
        threading.Thread(target=b).start()
    elif cadenaEntrante[1] == '9':
        threading.Thread(target=c).start()
    else: 
        salida.set('Lo que ingreso no es una IP')


def a():
     candenaA = re.compile("(^(10)(\.([2]([0-5][0-5]|[01234][6-9])|[1][0-9][0-9]|[1-9][0-9]|[0-9])){3})")
     result = re.fullmatch(candenaA, entrada.get())

     if result == None:
        salida.set('su IP no corresponde con el rango')
        print('Su IP no corresponde con el rango')
     else:
        salida.set('''
    ---------------------------------------------------------
            SU IP CORRESPONDE A LA
                CLASE: A
    ---------------------------------------------------------''')
        if entrada.get() == '192.168.1.69':
            os.system(f'ping {entrada.get()}')
        # os.system(f'ping {entrada.get()})



def b():
    cadenaB = re.compile("(^(172)\.(1[6-9]|2[0-9]|3[0-1])(\.(2[0-4][0-9]|25[0-5]|[1][0-9][0-9]|[1-9][0-9]|[0-9])){2})")
    result = re.fullmatch(cadenaB, entrada.get())

    if result == None:
        salida.set('su IP no corresponde con el rango')
    else:
        salida.set('''
    ---------------------------------------------------------
            SU IP CORRESPONDE A LA
                CLASE: B
    ---------------------------------------------------------''')
        if entrada.get() == '192.168.1.69':
            os.system(f'ping {entrada.get()}')
        #os.system(f'ping {entrada.get()}')


def c():
    cadenaC = re.compile("(^(192)\.(168)(\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])){2})")
    result = re.fullmatch(cadenaC, entrada.get())

    if result == None:
        salida.set('su IP no corresponde con el rango')
    else:
        salida.set('''
    ---------------------------------------------------------
            SU IP CORRESPONDE A LA
                CLASE: C
    ---------------------------------------------------------''')
        if entrada.get() == '192.168.1.69':
            os.system(f'ping {entrada.get()}')
            time.sleep(10)
            os.system('^C')
            

        # os.system(f'netstat {entrada.get()}')


ventana = Tk()
ventana.geometry('580x440')
ventana.config(bg='#0E476C')


#declaramos variables para obtener los datos 
entrada = StringVar()
salida = StringVar()



#declaramos un label para poner halgo
title = Label(ventana,text="VALIDAR IP")
title.place(x=10,y=10, width=560, height=60)
title.config(font="Ubuntu 30 normal", fg='white', bg='#0E476C')

#campo donse se muestra los resultados
labelResultado = Label(ventana, textvariable=salida, bg='#FFC12C')
labelResultado.place(x=130, y=300) 



#declaramos el cuadro de texto
cuadro = Entry(ventana,font='arial 20',justify='center', textvariable=entrada)
cuadro.place(x=110,y= 130,width=350, height=50)


#declaramos el boton
border_color = Frame(ventana, background="#003C6D")

boton = Button(ventana, text='calcular', command=ip)
boton.place(x=137, y=200, width=300,height=40)
boton.config(font="Ubuntu 15 normal",bg="#17AEBF",fg='white' )


def main():
    ventana.mainloop()


if __name__ == '__main__':
    main()