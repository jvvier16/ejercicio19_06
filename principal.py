from funciones import *


while True:
    print("menu cotactos")
    print("1.agregar contactos\n2.mostrar contactos\n3.guardar archivo csv\4.salir")
    opc = int(input("ingrese opcion:"))
    if opc == 1:
        opcion_1()
    elif opc ==2:
        opcion_2()
    elif opc ==3:
        opcion_3()
    else:
        pass