contactos = []

def opcion_1():
    print("agregar contacto")
    nombre = validar_nombre
    telefono = validar_telefono
    correo = validar_correo
    contacto = {"nombre":nombre,"telefono":telefono,"correo":correo}
    contactos.append(contacto)

def opcion_2():
    if len (contactos)==0:
        print("no existen contactos,primero debe agregar un contacto")
    else:
        print("lista de contactos")
        for c in contactos:
            print(f"nombre:{c['nombre']}")
            print(f"telefono:{c['telefono']}")
            print(f"correo:{c['correo']}")

def opcion_3():
    if validar_contacto:
        print("no existen contactos,primero debe agregar un contacto")
    else:
        nombre_archivo = input("ingrese nombre del archivo: ")
        import csv
        with open(nombre_archivo+".csv","w" )as archivo:
            esritor = csv.DictWriter(archivo,["nombre","telefono","correo"])
            esritor.writerows(contactos)
        print("acrichivo creado")

def opcion_4():
    print("adios")
    exit()
    
####################################################################
#funcionesde validar

def validar_opciones(lista_opciones):
    try:
        opc = int(input("ingrese una opcion: "))
        if opc in lista_opciones:
            return opc
        else:
            print("error opcion incorrecta")
    except:
        print("error debe ingresar un numero entero")

def validar_nombre():
    while True:
        nombre = input("ingrese nombre:") 
        if len (nombre)>3 and nombre.isalpha():
            return nombre
        else:
            print("error nombre debe tene 3 letras almenos") 
def validar_telefono():
    try:
        telefono = int(input("ingrese telefono: "))
        if len(str(telefono))==9 and str(telefono)[0]=='9':
            return telefono
        else:
            print("error el telefono debe empezr con 9 y tener 9 digitos")
        
    except:
        print("error debe ingresar un numero entero")

def validar_correo():
    #pattern
    correo = input("ingrese correo: ")
    if correo.lower().endswith("@gmail.com") and len(correo.strip())>=13:
        return correo
    else:
        print("error correo incorrecto")
def validar_contacto():
    if len(contactos)==0:
        print("no existen contactos debe agregar")
    else:
        return contactos
def validar_nombre_archivo():
    nombre_archivo = input("ingrese nombre del archivo: ") 
    if len(nombre_archivo.strip()):
        return nombre_archivo