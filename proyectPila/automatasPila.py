from tkinter import *
from pila import Pila
import re
import os



def iniciar_validacion():
    os.system('cls')
    cadenaEntrante = entrada.get()
    #aqui esta la nueva cadena
    cadenaSeparada = cadenaEntrante.split(' ')
    #longitud de la cadena
    longitud = cadenaSeparada.__len__()

    posicionCadena = 0
    bandera = True    

    #creamos la pila
    pila = Pila()
    #agregamos los valores a la pila
    print('push')
    pila.apilar('F')
    pila.ver_pila()


    while bandera == True:
        #sacamos el primer elemento de la pila
        valorPila = pila.desapilar()

        #lo que sacamos de la pila lo metemos al switch y validamos
        if valorPila == 'F':
            print('pop ', valorPila)
            print('push')
            pila.apilar('PARAM')
            print('push')
            pila.apilar(':')
            print('push')
            pila.apilar('PF')
            print('push')
            pila.apilar('PA')
            print('push')
            pila.apilar('PI')
            print('push')
            pila.apilar('ID')
            print('push')
            pila.apilar('TIPO')
            pila.ver_pila()


        elif valorPila == 'TIPO':
            print('pop ', valorPila)
            print('push def')
            pila.apilar('def')
            pila.ver_pila()
            nuevoValor = pila.desapilar()

            if nuevoValor == cadenaSeparada[posicionCadena]:
                print('pop', nuevoValor)
                pila.ver_pila()
                posicionCadena = posicionCadena + 1
            else:
                print(f'esta parte {cadenaSeparada[posicionCadena]} no cumple ')
                pila.apilar('def')
                pila.ver_pila()
                bandera = False

           
        elif valorPila == 'ID':
            print('pop ', valorPila)
            #aqui debo ingresar lo que produce ID
            candenaA = re.compile("(^([a-z]+)([A-Z]*)([_]*)([a-z]*)([A-Z]*)([0-9]*)([a-z]*)([A-Z]*))")
            result = re.fullmatch(candenaA, cadenaSeparada[posicionCadena])
            if result == None:
                print('su cadena no paso')
                pila.apilar('ID')
                pila.ver_pila()
                bandera= False
            else:
                print('su cadena si paso')
                pila.ver_pila()
                posicionCadena = posicionCadena + 1


        elif valorPila == 'PI':
            print('pop ', valorPila)
            print('push (')
            pila.apilar('(')
            pila.ver_pila()
            nuevoValor1 = pila.desapilar()
            if nuevoValor1 == cadenaSeparada[posicionCadena]:
                print('pop', nuevoValor1)
                pila.ver_pila()
                posicionCadena = posicionCadena + 1
            else:
                print(f'esta parte {cadenaSeparada[posicionCadena]} no cumple ')
                pila.apilar('(')
                pila.ver_pila()
                bandera = False


        elif valorPila == 'PA':
            print('pop ', valorPila)
             #aqui debo ingresar lo que produce PA
            candenaPA = re.compile("(^$|^([a-z]+)([A-Z]*)([_]*)([0-9]*)([a-z]*)([A-Z]*))")
            result = re.fullmatch(candenaPA, cadenaSeparada[posicionCadena])
            if result == None:
                print('su cadena no paso')
                pila.apilar('PA')
                pila.ver_pila()
                bandera= False
            else:
                print('su cadena si paso')
                pila.ver_pila()
                posicionCadena = posicionCadena + 1


        elif valorPila == 'PF':
            print('pop ', valorPila)
            print('push )')
            pila.apilar(')')
            pila.ver_pila()
            nuevoValor1 = pila.desapilar()
            if nuevoValor1 == cadenaSeparada[posicionCadena]:
                print('pop', nuevoValor1)
                pila.ver_pila()
                posicionCadena = posicionCadena + 1
            else:
                print(f'esta parte {cadenaSeparada[posicionCadena]} no cumple ')
                pila.apilar(')')
                pila.ver_pila()
                bandera = False

        elif valorPila == ':':
            if valorPila == cadenaSeparada[posicionCadena]:
                print('pop ', valorPila)
                pila.ver_pila()
                posicionCadena = posicionCadena + 1
            else:
                print(f'esta parte {cadenaSeparada[posicionCadena]} no cumple ')
                pila.apilar(':')
                pila.ver_pila()
                bandera = False


        elif valorPila == 'PARAM':
            #aqui tengo que mandar el 'return parametro | vacio' a la pila
            cadenaUltimo = cadenaSeparada[cadenaSeparada.__len__() - 1]

            print('pop ', valorPila)
            if cadenaUltimo == ":":
                print('la pila esta vacia? ', pila.esta_vacia())
                pila.ver_pila()
                print('el ultimo valor de la cadena es: ', cadenaUltimo)
                salida.set('LA CADENA ES CORRECTAA')
                bandera = False
                
            else:
                print('push ID')
                pila.apilar('ID')
                print('push return')
                pila.apilar('return')
                pila.ver_pila()
                retornoPila = pila.desapilar()
                if retornoPila == cadenaSeparada[posicionCadena]:
                    print('pop ', retornoPila)
                    pila.ver_pila()
                    posicionCadena +=1

                    #voy hacer con el ID
                    pilaId = pila.desapilar()
                    print('pop ', pilaId)
                    #aqui debo ingresar lo que produce ID
                    candenaA = re.compile("(^([a-z]+)([A-Z]*)([_]*)([a-z]*)([A-Z]*)([0-9]*)([a-z]*)([A-Z]*))")
                    result = re.fullmatch(candenaA, cadenaSeparada[posicionCadena])
                    if result == None:
                        print('su cadena no paso')
                        pila.apilar('ID')
                        pila.ver_pila()
                        bandera= False
                    else:
                        print('la cadena que ingreso es correcta')
                        print('la pila esta vacia? ', pila.esta_vacia())
                        pila.ver_pila()
                        print('el ultimo valor de la cadena es: ', cadenaUltimo)
                        salida.set('LA CADENA ES CORRECTAA')
                        bandera = False


                else:
                    print(f'esta parte {cadenaSeparada[posicionCadena]} no cumple ')
                    pila.apilar('return')
                    pila.ver_pila()
                    bandera = False
    

    


ventana = Tk()

ventana.geometry('550x350')
ventana.config(bg='#0E476C')

#declaramos los variables de entrada y salida
entrada = StringVar()
salida = StringVar()


#declaramos un label
title = Label(ventana, text='Escriba la funcion de python')
title.place(x=10,y=10, width=500, height=50)
title.config(font="Ubuntu 30 normal", fg='white', bg='#0E476C')

#declaro el cuadro de texto
cuadrotxt = Entry(ventana, font='arial 20', justify='center', textvariable=entrada)
cuadrotxt.place(x=110,y= 120,width=350, height=50)

#campo donse se muestra los resultados
labelResultado = Label(ventana, textvariable=salida, bg='#FFC12C')
labelResultado.place(x=130, y=300) 

#declaramos el boton
border_color = Frame(ventana, background="#003C6D")

boton = Button(ventana, text='calcular', command=iniciar_validacion)
boton.place(x=137, y=200, width=300,height=40)
boton.config(font="Ubuntu 15 normal",bg="#17AEBF",fg='white' )


def main():
    ventana.mainloop()


if __name__ == '__main__':
    main()