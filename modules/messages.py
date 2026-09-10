def menu_coordinador():
    print("CAMPUSLANDS ADMIN")
    print("-" * 50)
    print("\n>> Menú ADMIN <<\n")
    print("1. Registrar camper")
    print("2. Registrar trainer")
    print("3. Gestión de matricula en rutas")
    print("4. Gestión de módulos y evaluación")
    print("5. Reportes")
    print("6. Consulta riesgo de campers")
    print("0. Cerrar sesión\n")
    option_coordinador = input(">>> Ingrese una opción (0-6): ").strip()
    return option_coordinador

def menu_trainer():
    print("CAMPUSLANDS TRAINER")
    print("-" * 50)
    print("\n>> Menú TRAINER <<\n")
    print("1. Gestión de módulos y evaluación")
    print("2. Reportes")
    print("0. Cerrar sesión\n")
    option_trainer = input(">>> Ingrese una opción (0-2): ").strip()
    return option_trainer

def menu_camper():
    print("CAMPUSLANDS CAMPER")
    print("-" * 50)
    print("\n>> Menú CAMPER <<\n")
    print("1. Ver ruta asignada")
    print("2. Ver calificaciones")
    print("0. Cerrar sesión\n")
    option_camper = input(">>> Ingrese una opción (0-2): ").strip()
    return option_camper