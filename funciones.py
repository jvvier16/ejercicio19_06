contactos = []

def opcion_1():
    print("agregar contacto")
    nombre = input ("ingrese nombre: ")
    telefono = int(input("ingrese el telefono: "))
    correo = input("ingrese el correo: ")
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
    if len (contactos)==0:
        print("no existen contactos,primero debe agregar un contacto")
    else:
        nombre_archivo = input("ingrese nombre del archivo: ")
        import csv
        with open(nombre_archivo+".csv","w" )as archivo:
            esritor = csv.DictWriter(archivo,["nombre","telefono","correo"])
            esritor.writerows(contactos)
        print("acrichivo creado")

def opcion_4():
    pass