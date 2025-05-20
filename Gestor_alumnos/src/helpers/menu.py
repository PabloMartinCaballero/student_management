#Archivo que contendra el menu
import os
from termcolor import cprint

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def show_menu():
        cprint('🧑‍🎓  Bienvenido al gestor de alumnos 🧑‍🎓', 'blue', attrs=['bold'])
        cprint('1. Ver Cursos ', 'blue')
        cprint('2. Consultar/Editar Calificaciones y estadisticas', 'blue')
        cprint('3. Agregar alumno', 'blue')
        cprint('4. Eliminar alumno ', 'blue')
        print()
        cprint('0. Salir' , 'red',  attrs=['bold'])