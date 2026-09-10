import utils.utils as ut
import modules.main as m
import utils.utils as ut
import json


estados = (
    "En proceso de ingreso",
    "Inscrito",
    "Aprobado",
    "Cursando",
    "Graduado",
    "Expulsado",
    "Retirado"
    )

horarios = (
    "06:00 - 10:00",
    "10:00 - 14:00",
    "14:00 - 18:00",
    "18:00 - 22:00"
    )

rutas = (
    ("Fundamentos de programación (Introducción a la algoritmia, PSeInt y Python)", []),
    ("Programación Web (HTML, CSS y Bootstrap)", []),
    ("Programación formal", [
        "Java",
        "JavaScript",
        "C#"
        ]),
    ("Bases de datos", [
        "MySQL",
        "MongoDB",
        "PostgreSQL"
        ]),
    ("Backend", [
        "NetCore",
        "Spring Boot",
        "NodeJS",
        "Express"
        ])
)

salones = ("Artemis", "Sputnik", "Apolo")

riesgos = (
    "Bajo",
    "Medio",
    "Alto"
)

usuarios = {
    "cordcamp2025" : {
    "nombres" : "Jorge Alberto",
    "apellidos" : "Gomez Chaparro",
    "rol" : "coordinador"
    }
}
areas = {}
matriculas = []
evaluaciones = []

cod_camper = None

def login():
    cargar_datos()
    isActiveLogin = True
    while isActiveLogin:
        ut.clear_screen()
        print("¡BIENVENIDO A CAMPUSLANDS!")
        print("-" * 50)
        print("\nMenú de login\n")
        print("1. Iniciar sesión")
        print("2. Trainers y rutas (test)")
        print("0. Salir\n")
        option_login = input(">>> Ingrese una opción (0-1): ").strip()
        try:
            match option_login:
                case "1":
                    ut.clear_screen()
                    print("CAMPUSLANDS")
                    print("-" * 50)
                    print("Iniciar sesión")

                    user_id = input("\n>>> Ingrese su ID: ").strip()

                    if user_id not in usuarios:
                        print(f"\n⚠️ El usuario con ID '{user_id}' no ha sido registrado.")
                        ut.pause()
                    else:
                        rol = usuarios[user_id]["rol"]
                        ut.clear_screen()
                        print(f"\n✅ Inicio de sesión exitoso. Bienvenido, {usuarios[user_id]['nombres']} {usuarios[user_id]['apellidos']} ({rol}).\n")
                        ut.pause()
                        if rol == "coordinador":
                            m.main_coordinador()
                        elif rol == "trainer":
                            m.main_trainer()
                        elif rol == "camper":
                            m.main_camper()
                        else:
                            print("⚠️ ID desconocido.")
                        ut.pause()

                case "2":
                    ut.clear_screen()
                    ver_trainer_ruta()

                case "0":
                    print("\n¡Gracias por usar CAMPUSLANDS!")
                    isActiveLogin = False

                case _:
                    print("\n⚠️ ERROR: Debe ingresar un número entre 0 y 1.")
                    ut.pause()
        except ValueError:
            print("\n⚠️ ERROR INESPERADO.")
            ut.pause()

def registro_campers():
    global usuarios
    isActiveRegistroCamper = True
    while isActiveRegistroCamper:
        try:
            ut.clear_screen()
            print("CAMPUSLANDS ADMIN")
            print("-" * 50)
            print("\n>> Registro de campers <<\n")
            print("1. Registrar información")
            print("2. Registrar nota de prueba inicial")
            print("3. Cambiar estado")
            print("4. Modificar riesgo")
            print("0. Volver al menú principal.\n")
            option_registro_camper = input(">>> Ingrese una opción (0-4): ").strip()

            match option_registro_camper:
                case "1":
                    ut.clear_screen()
                    print("CAMPUSLANDS ADMIN")
                    print("-" * 50)
                    print("\nRegistrando información del camper...\n")
                    cod_camper = ut.validador_input("\t> Número de identificación para el camper: ").strip()
                    if cod_camper in usuarios and usuarios[cod_camper]["rol"] == "camper":
                        print("\nEste número de identificación ya fue registrado. Intente de nuevo.")
                    else:
                        nombres = ut.validador_input("\t> Nombre(s): ").title().strip()
                        apellidos = ut.validador_input("\t> Apellidos: ").title().strip()
                        direccion = ut.validador_input("\t> Dirección: ").upper().strip()
                        acudiente = ut.validador_input("\t> Nombre del acudiente: ").title().strip()
                        movil = ut.validador_input("\t> Número de teléfono movil: ").strip()
                        telefono = ut.validador_input("\t> Número de teléfono fijo: ").strip()
                        estado_camper = estados[0]
                        riesgo_camper = riesgos[0]
                        nota_prueba_inicio = None
                        ruta = None
                        calificaciones = None
                        rol = "camper"
                        
                        usuarios[cod_camper] = {
                            "nombres" : nombres,
                            "apellidos" : apellidos,
                            "direccion" : direccion,
                            "acudiente" : acudiente,
                            "movil" : movil,
                            "telefono" : telefono,
                            "riesgo_camper" : riesgo_camper,
                            "estado_camper" : estado_camper,
                            "nota_prueba_inicio" : nota_prueba_inicio,
                            "ruta" : ruta,
                            "calificaciones" : calificaciones,
                            "rol" : rol
                        }
                        print("\nInformación registrada con éxito.")
                    guardar_datos()
                    ut.pause()

                case "2":
                    ut.clear_screen()
                    print("CAMPUSLANDS ADMIN")
                    print("-" * 50)
                    print("\nRegistrando nota de prueba inicial...\n")
                    try:
                        cod_camper = input("\t> Número de identificación del camper: ").strip()
                        if cod_camper not in usuarios or usuarios[cod_camper]["rol"] != "camper":
                            print("\nEste número de identificación no ha sido registrado. Intente de nuevo.")
                        else:
                        
                            print(f"\t> Aspirante: {usuarios[cod_camper]['nombres']} {usuarios[cod_camper]['apellidos']}\n")
                            nota_prueba_inicio = int(input("\t> Nota de prueba inicial (0-100): "))
                            usuarios[cod_camper]['nota_prueba_inicio'] = nota_prueba_inicio

                            if nota_prueba_inicio >= 60:
                                usuarios[cod_camper]['estado_camper'] = estados[1]
                                print(f"\nEl aspirante aprobó la prueba inicial. Su estado ha cambiado a '{estados[1]}'.")
                            else:
                                usuarios[cod_camper]['estado_camper'] = estados[0]
                                print("\nEl aspirante no aprobó la prueba inicial.")
                        guardar_datos()
                    except ValueError:
                        print("\n⚠️ ERROR: La nota debe ser un número entero positivo entre 0 y 100.")
                    ut.pause()
                        
                case "3":
                    ut.clear_screen()
                    print("CAMPUSLANDS ADMIN")
                    print("-" * 50)
                    print("\nCambiar estado\n")
                    cod_camper = input("\t> Número de identificación del camper: ").strip()
                    if cod_camper not in usuarios or usuarios[cod_camper]["rol"] != "camper":
                        print("\nEste número de identificación no ha sido registrado. Intente de nuevo.")
                    else:
                        try:
                            print(f"\t> Aspirante: {usuarios[cod_camper]['nombres']} {usuarios[cod_camper]['apellidos']}\n")
                            print("-" * 25)
                            print("\nLISTA DE ESTADOS:\n")
                            for idx, estado in enumerate(estados, 1):
                                print(f"{idx}. {estado}")
                            num_estado = int(input("\n>>> Ingrese el número del item que desea asignar como nuevo estado: "))
                            usuarios[cod_camper]['estado_camper'] = estados[num_estado - 1]
                            print("\nEstado cambiado con éxito.")
                            guardar_datos()
                        except ValueError:
                            print("\n⚠️ ERROR: Debe ingresar un número de la lista.")
                    ut.pause()
                
                case "4":
                    ut.clear_screen()
                    print("CAMPUSLANDS ADMIN")
                    print("-" * 50)
                    print("\nModificar riesgo\n")
                    cod_camper = input("\t> Número de identificación del camper: ").strip()
                    if cod_camper not in usuarios or usuarios[cod_camper]["rol"] != "camper":
                        print("\nEste número de identificación no ha sido registrado. Intente de nuevo.")
                    else:
                        try:
                            print(f"\t> Aspirante: {usuarios[cod_camper]['nombres']} {usuarios[cod_camper]['apellidos']}\n")
                            print("-" * 25)
                            print("\nLISTA DE ESTADOS DE RIESGO:\n")
                            for idx, riesgo in enumerate(riesgos, 1):
                                print(f"{idx}. {riesgo}")
                            num_riesgo = int(input("\n>>> Ingrese el número del item que desea asignar como nuevo estado de riesgo: "))
                            usuarios[cod_camper]['riesgo_camper'] = riesgos[num_riesgo - 1]
                            print("\nEstado de riesgo modificado con éxito.")
                            guardar_datos()
                        except ValueError:
                            print("\n⚠️ ERROR: Debe ingresar un número de la lista.")
                    ut.pause()
                        
                case "0":
                    isActiveRegistroCamper = False
                case _:
                    print("\n⚠️ ERROR: Debe ingresar un número entre 0 y 4. Intente de nuevo.")
                    ut.pause()
        except ValueError:
            print("\n⚠️ ERROR INESPERADO.")
            ut.pause()

def registro_trainers():
    global usuarios, areas
    isActiveRegistroTrainer = True
    while isActiveRegistroTrainer:
        try:
            ut.clear_screen()
            print("CAMPUSLANDS ADMIN")
            print("-" * 50)
            print("\n>> Registro de trainers <<\n")
            print("1. Registrar información")
            print("2. Asignar horario")
            print("3. Asignar ruta")
            print("0. Volver al menú principal\n")
            option_registro_trainer = input("Ingrese una opción (0-3): ").strip()

            match option_registro_trainer:
                case "1":
                    ut.clear_screen()
                    print("CAMPUSLANDS ADMIN")
                    print("-" * 50)
                    print("\nRegistrando información del trainer...\n")
                    user_trainer = ut.validador_input("\t> Ingrese el ID para el trainer: ").strip()
                    if user_trainer in usuarios and usuarios[user_trainer]["rol"] == "trainer":
                        print("\nEste usuario ya ha sido registrado. Intente de nuevo.")
                    else:
                        nombre_trainer = ut.validador_input("\t> Nombre(s): ").title().strip()
                        apellido_trainer = ut.validador_input("\t> Apellidos: ").title().strip()
                        direccion_trainer = ut.validador_input("\t> Dirección: ").upper().strip()
                        movil_trainer = ut.validador_input("\t> Número de teléfono movil: ").strip()
                        telefono_trainer = ut.validador_input("\t> Número de teléfono fijo: ").strip()
                        horario_trainer = None
                        ruta_trainer = []
                        rol_trainer = "trainer"

                        usuarios[user_trainer] = {
                            'nombres' : nombre_trainer,
                            'apellidos' : apellido_trainer,
                            'direccion' : direccion_trainer,
                            'movil' : movil_trainer,
                            'telefono' : telefono_trainer,
                            'horario' : horario_trainer,
                            'ruta' : ruta_trainer,
                            'rol' : rol_trainer
                            }
                        areas[user_trainer] = {
                            'trainer': f"{nombre_trainer} {apellido_trainer}",
                            'materias': [],
                            'campers': [],
                            'salon' : None
                            }
                        print("\nInformación registrada con éxito.")
                    guardar_datos()
                    ut.pause()

                case "2": 
                    ut.clear_screen()
                    print("CAMPUSLANDS ADMIN")
                    print("-" * 50)
                    print("\n>> Asignar horario <<\n")
                    user_trainer = input("\t> Ingrese el ID del trainer: ").strip()
                    if user_trainer not in usuarios or usuarios[user_trainer]["rol"] != "trainer":
                        print("\nEste trainer aún no ha sido registrado. Intente nuevamente.")
                    else:
                        try:
                            print(f"\t> Trainer: {usuarios[user_trainer]['nombres']} {usuarios[user_trainer]['apellidos']}\n")
                            print("-" * 25)
                            print("\nLISTA DE HORARIOS DISPONIBLES:\n")
                            for idx, horarios_trainer in enumerate(horarios, 1):
                                print(f"{idx}. {horarios_trainer}")
                            num_horario = int(input("\n>>> Ingrese el número del item que desea asignar como horario: "))
                            usuarios[user_trainer]['horario'] = horarios[num_horario - 1]
                            print("\nHorario asignado con éxito.")
                            guardar_datos()
                        except ValueError:
                            print("\n⚠️ ERROR: Debe ingresar un número de la lista.")
                    ut.pause()


                case "3":
                    ut.clear_screen()
                    print("CAMPUSLANDS ADMIN")
                    print("-" * 50)
                    print("\n>> Asignar ruta <<\n")
                    user_trainer = input("\t> Ingrese el ID del trainer: ").strip()
                    if user_trainer not in usuarios or usuarios[user_trainer]["rol"] != "trainer":
                        print("\nEste trainer aún no ha sido registrado. Intente nuevamente.")
                    else:
                        print(f"\t> Trainer: {usuarios[user_trainer]['nombres']} {usuarios[user_trainer]['apellidos']}\n")

                    if not usuarios[user_trainer]['horario']:
                        print("\nEste trainer aún no tiene un horario asignado. Asigne un horario primero (opción 2).")
                        ut.pause()
                        return
                    
                    horario_trainer = usuarios[user_trainer]['horario']
                    nombre_trainer = f"{usuarios[user_trainer]['nombres']} {usuarios[user_trainer]['apellidos']}"

                    if rutas[0][0] not in usuarios[user_trainer]['ruta']: 
                        usuarios[user_trainer]['ruta'].append(rutas[0][0])
                    if rutas[1][0] not in usuarios[user_trainer]['ruta']:
                        usuarios[user_trainer]['ruta'].append(rutas[1][0])
                    print(f"\n'{rutas[0][0]}' y '{rutas[1][0]}', asignadas por defecto como rutas básicas.")
                    print("-" * 25)

                    try:
                        print("\nASIGNACIÓN DE RUTA ESPECIALIZADA:")
                        tema_1, subtemas_1 = rutas[2]
                        print(f"\nSeleccione 2 especializaciones para la ruta de {tema_1}\n")
                        for idx, sub_1 in enumerate(subtemas_1, 1):
                            print(f"{idx}. {sub_1}")
                        num_espec_1 = ut.leer_indices(input("\n>>> Ingrese dos números de items separados por comas: "))
                        if 1 <= len(num_espec_1) <= 2:
                            for i in num_espec_1:
                                if 1 <= i <= len(subtemas_1):
                                    usuarios[user_trainer]['ruta'].append(f"{tema_1} - {subtemas_1[i - 1]}")

                        tema_2, subtemas_2 = rutas[3]
                        print(f"\nSeleccione 1 especialización para la ruta de {tema_2}\n")
                        for idx, sub_2 in enumerate(subtemas_2, 1):
                            print(f"{idx}. {sub_2}")
                        num_espec_2 = int(input("\n>>> Ingrese el número del SGBD a asignar: "))
                        if 1 <= num_espec_2 <= len(subtemas_2):
                            usuarios[user_trainer]['ruta'].append(f"{tema_2} - {subtemas_2[num_espec_2 - 1]}")

                        tema_3, subtemas_3 = rutas[4]
                        print(f"\nSeleccione 2 especializaciones para la ruta de {tema_3}\n")
                        for idx, sub_3 in enumerate(subtemas_3, 1):
                            print(f"{idx}. {sub_3}")
                        num_espec_3 = ut.leer_indices(input("\n>>> Ingrese dos números de items separados por comas: "))
                        if 1 <= len(num_espec_3) <= 2:
                            for i in num_espec_3:
                                if 1 <= i <= len(subtemas_3):
                                    usuarios[user_trainer]['ruta'].append(f"{tema_3} - {subtemas_3[i - 1]}")
                        print("-" * 50)
                        
                        if user_trainer not in areas:
                            areas[user_trainer] = {
                                "trainer": nombre_trainer,
                                "materias": usuarios[user_trainer]['ruta'],
                                "campers": [],
                                "salon" : None
                            }
                            print(f"✅ Ruta creada exitosamente para el trainer {nombre_trainer}.")
                        else:
                            areas[user_trainer]['materias'] = usuarios[user_trainer]['ruta']
                            print(f"✅ Ruta creada exitosamente para el trainer {nombre_trainer}.")

                        print("\nSALONES DISPONIBLES:\n")
                        for idx, s in enumerate(salones, 1):
                            print(f"{idx}. {s}")
                        num_salon = int(ut.validador_input("\n>>> Seleccione el salón para este trainer: "))
                        areas[user_trainer]['salon'] = salones[num_salon - 1]
                        print(f"\n✅ Salón asignado: {areas[user_trainer]['salon']}")
                    except ValueError:
                        print("\n⚠️ ERROR: Debe ingresar un número de la lista.")
                    guardar_datos()
                    ut.pause()

                case "0":
                    isActiveRegistroTrainer = False
                case _:
                    print("\n⚠️ ERROR: Debe ingresar un número entre 0 y 3")
                    ut.pause()
        except ValueError:
            print("\n⚠️ ERROR INESPERADO.")
            ut.pause()

def gestion_rutas():
    global usuarios, areas
    try:
        ut.clear_screen()
        print("CAMPUSLANDS ADMIN")
        print("-" * 50)
        print("\n>>> Asignar ruta a campers <<<\n")

        cod_camper = input("\t> Número de identificación del camper: ").strip()
        if cod_camper not in usuarios or usuarios[cod_camper]["rol"] != "camper":
            print("\n⚠️ Este número de identificación no ha sido registrado. Intente de nuevo.\n")
        
        else:
            print(f"\t> Camper: {usuarios[cod_camper]['nombres']} {usuarios[cod_camper]['apellidos']}\n")
            print("-" * 25)
            print("\nAREAS Y RUTAS DISPONIBLES:\n")

            disponibles = []
            for idx, (user_trainer, info) in enumerate(areas.items(), 1):
                cupo = len(info["campers"])
                if cupo < 33:
                    print(f"{idx}. Trainer: {info['trainer']} | Cupo: {cupo}/33")
                    print(f"\n> MATERIAS:\n" + "\n".join(info['materias']))
                    print("-" * 50)
                    disponibles.append(user_trainer)
                else:
                    print(f"{idx}. Trainer: {info['trainer']} | ❌ Ruta llena")

            if not disponibles:
                print("\n No hay rutas con cupos disponibles.")
                return

            while True:
                try:
                    num_area = int(input("\n>>> Ingrese el número del trainer al que desea asignar el camper: "))
                    if 1 <= num_area <= len(disponibles):
                        break
                    else:
                        print("\n⚠️ ERROR: Opción fuera de rango. Intente de nuevo.")
                except ValueError:
                    print("\n⚠️ ERROR: Debe ingresar un número válido. Intente de nuevo.")

            area_selec = disponibles[num_area - 1]
            areas[area_selec]["campers"].append(cod_camper)
            usuarios[cod_camper]["ruta"] = list(areas[area_selec]["materias"])
            usuarios[cod_camper]["estado_camper"] = estados[3]
            usuarios[cod_camper]["salon"] = areas[area_selec]["salon"]

            print(f"\n✅ El camper '{usuarios[cod_camper]['nombres']} {usuarios[cod_camper]['apellidos']}' fue asignado a la ruta del trainer {areas[area_selec]['trainer']}.")
            print(f"Salón asignado: {usuarios[cod_camper]['salon']}")
            guardar_datos()
        ut.pause()
    except ValueError:
        print("\n⚠️ ERROR INESPERADO.")
        ut.pause()

def gestion_modulos_evaluacion():
    global usuarios
    ut.clear_screen()
    print("CAMPUSLANDS ADMIN")
    print("-" * 50)
    print("\n Calcular nota final del camper...\n")
    cod_camper = input("\t> Número de identificación del camper: ").strip()
    if cod_camper not in usuarios or usuarios[cod_camper]["rol"] != "camper":
        print("\nEste número de identificación no ha sido registrado. Intente de nuevo.")
    elif not usuarios[cod_camper]['ruta']:
        print("\nEste camper aún no tiene una ruta asignada. Asigne una ruta (Gestión de matrícula en rutas).")
    else:
        print(f"\t> Camper: {usuarios[cod_camper]['nombres']} {usuarios[cod_camper]['apellidos']}\n")
        print("-" * 25)
        print(f"\nRUTA ASIGNADA:\n")
        print("\n".join(usuarios[cod_camper]['ruta']))
    
        try:
            nombre_modulo = ut.validador_input(f"\n\t> Nombre del módulo a evaluar: ").title().strip()
            nota_teoria = int(input("\t> Nota de teoría (0-100): "))
            nota_practica = int(input("\t> Nota de práctica (0-100): "))
            nota_quices = int(input("\t> Nota de quices/trabajos (0-100): "))

            if nota_teoria < 0 or nota_practica < 0 or nota_quices < 0:
                print("\n⚠️ ERROR: Todas las notas deben ser números enteros positivos entre 0 y 100.")
                ut.pause()
                return
            elif nota_teoria > 100 or nota_practica > 100 or nota_quices > 100:
                print("\n⚠️ ERROR: Todas las notas deben ser números enteros positivos entre 0 y 100.")
                ut.pause()
                return

            nota_final = (0.3 * nota_teoria) + (0.6 * nota_practica) + (0.1 * nota_quices)
            estado_modulo = "Aprobado" if nota_final >= 60 else "Reprobado"

            if not usuarios[cod_camper].get('calificaciones'):
                usuarios[cod_camper]['calificaciones'] = {}

            usuarios[cod_camper]['calificaciones'][nombre_modulo] = {
                "nota_teoria": nota_teoria,
                "nota_practica": nota_practica,
                "nota_quices": nota_quices,
                "nota_final": round(nota_final),
                "estado_modulo": estado_modulo
            }
            print(f"\n✅ Módulo '{nombre_modulo}' evaluado. Nota final: {round(nota_final)} - Estado: {estado_modulo}")
        except ValueError:
            print("\n⚠️ ERROR: Las notas deben ser números enteros positivos entre 0 y 100.")
    guardar_datos()
    ut.pause()

def reportes():
    global usuarios, areas
    while True:
        ut.clear_screen()
        print("CAMPUSLANDS ADMIN")
        print("-" * 50)
        print("\n>> Reportes <<\n")
        print("1. Listar campers inscritos")
        print("2. Listar campers aprobados")
        print("3. Listar trainers activos")
        print("4. Listar campers con bajo rendimiento")
        print("5. Listar campers y trainers por ruta")
        print("6. Reporte por módulo")
        print("0. Volver al menú principal\n")
        option_reportes = input(">>> Ingrese una opción (0-6): ").strip()
        try:
            match option_reportes:
                case "1":
                    ut.clear_screen()
                    print("CAMPUSLANDS ADMIN")
                    print("-" * 50)
                    print("\n>> Campers inscritos <<\n")
                    inscritos = [f"{info['nombres']} {info['apellidos']} (ID: {cod})" for cod, info in usuarios.items() if info['rol'] == 'camper' and info['estado_camper'] == 'Inscrito']
                    if inscritos:
                        print("\n".join(inscritos))
                    else:
                        print("No hay campers inscritos.")
                    ut.pause()

                case "2":
                    ut.clear_screen()
                    print("CAMPUSLANDS ADMIN")
                    print("-" * 50)
                    print("\n>> Campers aprobados <<\n")
                    aprobados = [f"{info['nombres']} {info['apellidos']} (ID: {cod})" for cod, info in usuarios.items() if info['rol'] == 'camper' and info['estado_camper'] == 'Aprobado']
                    if aprobados:
                        print("\n".join(aprobados))
                    else:
                        print("No hay campers aprobados.")
                    ut.pause()

                case "3":
                    ut.clear_screen()
                    print("CAMPUSLANDS ADMIN")
                    print("-" * 50)
                    print("\n>> Trainers activos <<\n")
                    activos = [f"{info['nombres']} {info['apellidos']} (ID: {cod})" for cod, info in usuarios.items() if info['rol'] == 'trainer']
                    if activos:
                        print("\n".join(activos))
                    else:
                        print("No hay trainers activos.")
                    ut.pause()

                case "4":
                    ut.clear_screen()
                    print("CAMPUSLANDS ADMIN")
                    print("-" * 50)
                    print("\n>> Campers con bajo rendimiento <<\n")
                    bajo_rendimiento = []
                    for cod, info in usuarios.items():
                        if info['rol'] == 'camper' and info.get('calificaciones'):
                            for mod, cal in info['calificaciones'].items():
                                if cal['estado_modulo'] == 'Reprobado':
                                    bajo_rendimiento.append(f"{info['nombres']} {info['apellidos']} (ID: {cod}) - Módulo: {mod} - Nota Final: {cal['nota_final']}")
                    if bajo_rendimiento:
                        print("\n".join(bajo_rendimiento))
                    else:
                        print("No hay campers con bajo rendimiento.")
                    ut.pause()
                
                case "5":
                    ut.clear_screen()
                    print("CAMPUSLANDS ADMIN")
                    print("-" * 50)
                    print("\n>> Campers y trainers por ruta <<\n")
                    for user_trainer, info in areas.items():
                        print(f"Trainer: {info['trainer']} | Salón: {info['salon']}")
                        if info['campers']:
                            for camper_id in info['campers']:
                                camper_info = usuarios.get(camper_id)
                                if camper_info:
                                    print(f"  - {camper_info['nombres']} {camper_info['apellidos']} (ID: {camper_id})")
                        else:
                            print("  No hay campers asignados.")
                    ut.pause()
                
                case "6":
                    ut.clear_screen()
                    print("CAMPUSLANDS ADMIN")
                    print("-" * 50)
                    print("\n>> Reporte por módulo <<\n")
                    nombre_modulo = ut.validador_input("\t> Nombre del módulo a listar:  ").title().strip()
                    aprobados = []
                    reprobados = []
                    for cod, info in usuarios.items():
                        if info['rol'] == 'camper' and info.get('calificaciones') and nombre_modulo in info['calificaciones']:
                            cal = info['calificaciones'][nombre_modulo]
                            if cal['estado_modulo'] == 'Aprobado':
                                aprobados.append(f"{info['nombres']} {info['apellidos']} (ID: {cod}) - Nota Final: {cal['nota_final']}")
                            else:
                                reprobados.append(f"{info['nombres']} {info['apellidos']} (ID: {cod}) - Nota Final: {cal['nota_final']}")
                    print(f"\nMódulo: {nombre_modulo}\n")
                    print(f"Aprobados ({len(aprobados)}):")
                    if aprobados:
                        print("\n".join(aprobados))
                    else:
                        print("No hay aprobados.")
                    print(f"\nReprobados ({len(reprobados)}):")
                    if reprobados:
                        print("\n".join(reprobados))
                    else:
                        print("No hay reprobados.")
                    ut.pause()
                    
                case "0":
                    break
                case _:
                    print("\n⚠️ ERROR: Debe ingresar un número entre 0 y 6.")
                    ut.pause()
        except ValueError:
            print("\n⚠️ ERROR INESPERADO.")
            ut.pause()

def consultas():
    global usuarios
    ut.clear_screen()
    print("CAMPUSLANDS ADMIN")
    print("-" * 50)
    print("\n>> Consultar camper en 'riesgo alto' <<\n")
    try:
        cod_camper = input("\t> Número de identificación del camper: ").strip()
        if cod_camper not in usuarios or usuarios[cod_camper]["rol"] != "camper":
            print("\nEste número de identificación no ha sido registrado. Intente de nuevo.")
        else:
            if usuarios[cod_camper]['riesgo_camper'] == "Alto":
                print(f"\n❌ El camper '{usuarios[cod_camper]['nombres']} {usuarios[cod_camper]['apellidos']}' está en RIESGO ALTO.\n")
            else:
                print(f"\n✅ El camper '{usuarios[cod_camper]['nombres']} {usuarios[cod_camper]['apellidos']}' no está en riesgo alto.\n")
    except ValueError:
        print("\n⚠️ ERROR INESPERADO.")
    ut.pause()

def ver_ruta_asignada():
    global usuarios, cod_camper
    ut.clear_screen()
    print("CAMPUSLANDS CAMPER")
    print("-" * 50)
    print("\n>> Ruta asignada <<\n")
    try:
        cod_camper = input("\t> Número de identificación del camper: ").strip()
        if cod_camper not in usuarios or usuarios[cod_camper]["rol"] != "camper":
            print("\nEste número de identificación no ha sido registrado. Intente de nuevo.")
        else:
            print(f"\t> Camper: {usuarios[cod_camper]['nombres']} {usuarios[cod_camper]['apellidos']}\n")
            print("-" * 25)
            if usuarios[cod_camper]['ruta']:
                print("RUTA ASIGNADA:\n")
                print("\n".join(usuarios[cod_camper]['ruta']))
                print(f"\nSalón asignado: {usuarios[cod_camper].get('salon', 'No asignado')}")
            else:
                print("Aún no tiene una ruta asignada.")
    except ValueError:
        print("\n⚠️ ERROR INESPERADO.")
    ut.pause() 

def ver_calificaciones():
    global usuarios, cod_camper
    ut.clear_screen()
    print("CAMPUSLANDS CAMPER")
    print("-" * 50)
    print("\n>> Calificaciones <<\n")
    try:
        cod_camper = input("\t> Número de identificación del camper: ").strip()
        if cod_camper not in usuarios or usuarios[cod_camper]["rol"] != "camper":
            print("\nEste número de identificación no ha sido registrado. Intente de nuevo.")
        else:
            print(f"\t> Camper: {usuarios[cod_camper]['nombres']} {usuarios[cod_camper]['apellidos']}\n")
            print("-" * 25)
            if usuarios[cod_camper].get('calificaciones'):
                for mod, cal in usuarios[cod_camper]['calificaciones'].items():
                    print(f"Módulo: {mod}")
                    print(f"  - Nota Teoría: {cal['nota_teoria']}")
                    print(f"  - Nota Práctica: {cal['nota_practica']}")
                    print(f"  - Nota Quices/Trabajos: {cal['nota_quices']}")
                    print(f"  - Nota Final: {cal['nota_final']}")
                    print(f"  - Estado del Módulo: {cal['estado_modulo']}\n")
            else:
                print("Aún no tiene calificaciones registradas.")
    except ValueError:
        print("\n⚠️ ERROR INESPERADO.")
    ut.pause()

def cargar_datos():
    global usuarios, areas, matriculas, evaluaciones

    if not ut.os.path.exists("data"):
        ut.os.makedirs("data")

    try:
        with open("data/usuarios.json", "r", encoding="utf-8") as f:
            usuarios = json.load(f)
    except FileNotFoundError:
        print("⚠️ El archivo 'usuarios.json' no se encuentra. Se inicializarán con datos vacíos.")
        usuarios = {}
    except json.JSONDecodeError:
        print(f"⚠️ Error al leer el archivo 'usuarios.json'.")
        usuarios = {}

    if "cordcamp2025" not in usuarios:
        print("El usuario 'cordcamp2025' no existe. Creando usuario por defecto...")
        usuarios["cordcamp2025"] = {
            "nombres": "Jorge Alberto",
            "apellidos": "Gomez Chaparro",
            "rol": "coordinador"
        }

    try:
        with open("data/areas.json", "r", encoding="utf-8") as f:
            areas = json.load(f)
    except FileNotFoundError:
        print("⚠️ El archivo 'areas.json' no se encuentra. Se inicializarán con datos vacíos.")
        areas = {}
    except json.JSONDecodeError:
        print(f"⚠️ Error al leer el archivo 'areas.json'.")
        areas = {}

    try:
        with open("data/matriculas.json", "r", encoding="utf-8") as f:
            matriculas = json.load(f)
    except FileNotFoundError:
        print("⚠️ El archivo 'matriculas.json' no se encuentra. Se inicializarán con datos vacíos.")
        matriculas = []
    except json.JSONDecodeError:
        print(f"⚠️ Error al leer el archivo 'matriculas.json'.")
        matriculas = []

    try:
        with open("data/evaluaciones.json", "r", encoding="utf-8") as f:
            evaluaciones = json.load(f)
    except FileNotFoundError:
        print("⚠️ El archivo 'evaluaciones.json' no se encuentra. Se inicializarán con datos vacíos.")
        evaluaciones = []
    except json.JSONDecodeError:
        print(f"⚠️ Error al leer el archivo 'evaluaciones.json'.")
        evaluaciones = []

    print("Datos cargados exitosamente.")

def guardar_datos():
    global usuarios, areas, matriculas, evaluaciones

    try:
        with open("data/usuarios.json", "w", encoding="utf-8") as f:
            json.dump(usuarios, f, ensure_ascii=False, indent=4)
    except Exception:
        print(f"⚠️ Error al guardar usuarios.")

    try:
        with open("data/areas.json", "w", encoding="utf-8") as f:
            json.dump(areas, f, ensure_ascii=False, indent=4)
    except Exception:
        print(f"⚠️ Error al guardar áreas.")

    try:
        with open("data/matriculas.json", "w", encoding="utf-8") as f:
            json.dump(matriculas, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"⚠️ Error al guardar matrículas.")

    try:
        with open("data/evaluaciones.json", "w", encoding="utf-8") as f:
            json.dump(evaluaciones, f, ensure_ascii=False, indent=4)
    except Exception:
        print(f"⚠️ Error al guardar evaluaciones.")


def ver_trainer_ruta():
    ut.clear_screen
    print("CAMPUSLANDS ADMIN")
    print("-" * 50)
    print("Visualizar trainers y rutas")
    reporte_trainers_rutas = {
    "id trainer" : {
        "1999" : {
            "nombres" : "Jorge Gomez",
            "ruta" : "NodeJS (C#, MySQL, PostgreSQL)",
            "salon" : "Sputnik",
            "horario" : "06:00 - 10:00",
            "rol" : "trainer"
        }},
    "id trainer" : {
        "2000" : {
            "nombres" : "Juan David Vesga",
            "ruta" : "Java (JavaScript, MySQL, MongoDB)",
            "salon" : "Artemis",
            "horario" : "06:00 - 10:00",
            "rol" : "trainer"
        }},
    "id trainer" : {
        "2001" : {
            "nombres" : "Brayan Espinosa",
            "ruta" : "NetCore (JavaScript, MongoDB, PostgreSQL)",
            "salon" : "Apolo",
            "horario" : "10:00 - 14:00",
            "rol" : "trainer"
        }},
    "id trainer" : {
        "2002" : {
            "nombres" : "Caroline Gomez",
            "ruta" : "Spring Boot (Java, PostgreSQL, MySQL)",
            "salon" : "Sputnik",
            "horario" : "10:00 - 14:00",
            "rol" : "trainer"
        }},
    "id trainer" : {
        "2003" : {
            "nombres" : "Silvia Silva",
            "ruta" : "Express (C#, MongoDB, MySQL)",
            "salon" : "Artemis",
            "horario" : "14:00 - 18:00",
            "rol" : "trainer"
        }}
    }
    if not reporte_trainers_rutas:
        print("No hay trainers registrados a la fecha.")
    else:
        print("TRAINERS DISPONIBLES Y RUTAS ASIGNADAS")
        for trainer, info in reporte_trainers_rutas:
            print(f"Trainer: {info['nombre']} | Ruta: {info['ruta']} - Salón: {info['salon']}")
    ut.pause()