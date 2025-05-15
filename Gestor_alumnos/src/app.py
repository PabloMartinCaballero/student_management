from src.data.db_students import students_list #importo mi lista 
from src.helpers.menu import show_menu, clear_console
from src.controllers.student_controller import create_student,add_student,delete_student,modify_student,show_students
def run():
    clear_console()
    while True:
        show_menu()
        option:int = int(input('Elige una opción [1-4]'))
        match option: 
            case 1 :
                print('Opción 1 seleccionada')
                show_students(students_list)
            case 2 :
                print('Opción 2 seleccionada')
                course: str = input('Ingrese el curso')
                modify_student(course)
            case 3 :
                print('Opción 3 seleccionada')
                print('Para agregar un nuevo alumno, cargue todos los datos indicados a continuación')
                new_student = create_student()
                add_student(new_student,students_list)
            case 4 : 
                print('Opción 4 seleccionada')
                print('Ingrese el curso del estudiante que desea eliminar')
                course: str = input('Ingrese el curso')
                delete_student(course)
            case 0:
                print('Gracias por utilizar el gestor, hasta luego')
            case _:
                print('Opción no valida, vuelva a intentarlo')
