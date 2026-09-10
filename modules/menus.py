import utils.utils as ut
import modules.messages as m
import modules.CRUD as c

def main_coordinador():
    isActiveCoordinador = True
    while isActiveCoordinador:
        ut.clear_screen()
        opt_coordinador = m.menu_coordinador()
        try:
            match opt_coordinador:
                case "1":
                    c.registro_campers()
                case "2":
                    c.registro_trainers()
                case "3":
                    c.gestion_rutas()
                case "4":
                    c.gestion_modulos_evaluacion()
                case "5":
                    c.reportes()
                case "6":
                    c.consultas()
                case "0":
                    ut.salir("\nCerrando sesión...\n")
                    isActiveCoordinador = False
                case _:
                    print("\n⚠️ ERROR: Debe ingresar un número entre 0 y 7.")
                    ut.pause()
        except ValueError:
            print("\n⚠️ ERROR INESPERADO.")
            ut.pause()


def main_trainer():
    isActiveTrainer = True
    while isActiveTrainer:
        ut.clear_screen()
        opt_trainer = m.menu_trainer()

        try:
            match opt_trainer:
                case "1":
                    c.gestion_modulos_evaluacion()

                case "2":
                    c.reportes()

                case "0":
                    ut.salir("\nCerrando sesión...\n")
                    isActiveTrainer = False
                case _:
                    print("\n⚠️ ERROR: Debe ingresar un número entre 0 y 2.")
                    ut.pause()
        except ValueError:
            print("\n⚠️ ERROR INESPERADO.")
            ut.pause()


def main_camper():
    isActiveCamper = True
    while isActiveCamper:
        ut.clear_screen()
        opt_camper = m.menu_camper()

        try:
            match opt_camper:
                case "1":
                    c.ver_ruta_asignada()

                case "2":
                    c.ver_calificaciones()

                case "0":
                    ut.salir("\nCerrando sesión...\n")
                    isActiveCamper = False
                case _:
                    print("\n⚠️ ERROR: Debe ingresar un número entre 0 y 2.")
                    ut.pause()
        except ValueError:
            print("\n⚠️ ERROR INESPERADO.")
            ut.pause()