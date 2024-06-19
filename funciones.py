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
    pass

def opcion_4():
    pass