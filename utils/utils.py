import os

def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

def pause():
    input("\nPresione ENTER para continuar...")

def validador_input(msg):
    while True:
        mensaje = input(msg).strip()
        if mensaje == "":
            print("\n⚠️ ERROR: Este campo no puede estar vacío. Intente de nuevo.\n")
        else:
            return mensaje

def leer_indices(seleccion, maximo=None):
    indices = []
    for x in seleccion.split(","):
        try:
            num = int(x.strip())
            if maximo is None or 1 <= num <= maximo:
                indices.append(num)
        except ValueError:
            continue
    return indices

def salir(msg):
    print(msg)