from typing import Optional
#Importo la DB y su controlador para realizar los controles utilizo un path absoluto para traerla
from src.data.db_students import students_list,check_db
from src.students.student import Student

#* Aplicación de CRUD para manejar la DB 
#*----------------------------------------------------------------------------------------------------------
#* Función para crear un estudiante a partir de la clase Student



def create_student() -> Student:
    name: str = input("Ingrese el nombre del alumno: ")
    last_name: str = input("Ingrese el apellido del alumno: ") 
    dni: str = input("Ingrese el DNI del alumno: ")
    home_address: str = input("Ingrese la dirección del alumno: ")

    # Validar que el curso exista usando check_db
    while True:
        course: str = input("Ingrese el curso del alumno (ej: 3A): ")
        existing_students = check_db(course)
        if existing_students is not None:  
            break
        else:
            print("El curso ingresado no existe. Por favor, intente nuevamente.")

    behavior: str = input("Ingrese el comportamiento del alumno: ")
    punctuality: str = input("Ingrese la puntualidad del alumno: ")
    nee: str = input("¿El alumno posee algún NEE? (si o no): ").lower() # Paso a minuscula la entrada

    if nee == 'si':
        type_nee: str = input("Ingrese el tipo de NEE que posee: ")
    else:
        type_nee = None

    new_student = Student(
        name, last_name, dni, home_address, course,
        behavior, punctuality, nee, type_nee
    )

    return new_student

#*-----------------------------------------------------------------------------------------------------------
#**  Añadir estudiante
        #Objeto = estudiante   #Lista
def add_student(student, db_students):
    student_course = student.course
    for course_dict in db_students:
        for division, students in course_dict.items():
            if division == student_course:
                students.append(student)
                print(f"Alumno agregado correctamente al curso {division}.")
                return True
    print(f"No se encontró la división '{student_course}'. No se pudo agregar al alumno.")
    return False
                
#*-------------------------------------------------------------------------------------------------------------

#**  Eliminar estudiante                
def delete_student(course_number: str) -> bool:
    for course_dict in students_list:
        for key, value in course_dict.items():
            if key == course_number:
                print(f"El curso {course_number} existe")
                print("Ingrese los datos del alumno que desea eliminar")
                student_name = input("Ingrese el nombre del alumno: ")
                student_last_name = input("Ingrese el apellido del alumno: ")
                found = False
                updated_students_list = []
                for student_obj in value:
                    if student_obj.name == student_name and student_obj.last_name == student_last_name:
                        print("Alumno encontrado y eliminado correctamente")
                        found = True
                    else:
                        updated_students_list.append(student_obj)
                course_dict[key] = updated_students_list # Actualizamos la lista de estudiantes del curso
                return found # Retornamos True si se eliminó al menos un alumno

    print("El curso no se encontro")
    return False

#*-----------------------------------------------------------------------------------------------------------------
#* Modificar alumno

def modify_student(course_number: str) -> list:
    for course_dict in students_list: #Itero en todos los diccionarios dentro de la lista [{dic1}, {dic2}, {dic2}]
        for key, value in course_dict.items(): # {"1°1°": [objeto_estudiante1, objeto_estudiante2]} key = 1°1° value = [objeto_estudiante1, objeto estudiante2]
            # print(f"Valor de la clave: {key}")
            if key == course_number: # Si encontro el curso pasa a buscar al studiante
                print(f"El curso {course_number} existe")
                print("Ingrese los datos del alumno que desea modificar")
                student_name = input("Ingrese el nombre del alumno: ")
                student_last_name = input("Ingrese el apellido del alumno: ")
                for student_obj in value:  # Iteramos sobre los objetos Student value = [objeto_estudiante1, objeto estudiante2]
                # Accedemos a los atributos del objeto
                    if student_obj.name == student_name and student_obj.last_name == student_last_name: #Verifico si ambos datos coinciden
                        print("Datos del alumno:")
                        print(f"Nombre: {student_obj.name}")
                        print(f"Apellido: {student_obj.last_name}")
                        print(f"Curso: {student_obj.course}")
                        
                        print("Ingrese los nuevos datos del alumno:")

                        new_name = input("Ingrese el nuevo nombre del alumno: ")
                        new_last_name = input("Ingrese el nuevo apellido del alumno: ")
                        new_course = input("Ingrese el nuevo curso del alumno: ")
                        new_behavior = input("Ingrese el nuevo comportamiento del alumno: ")
                        new_punctuality = input("Ingrese la nueva puntualidad del alumno: ")
                        new_nee = input("¿El alumno posee algun NEE?, ingrese si o no: ")
                        new_type_nee = input("Ingrese el tipo de nee que posee (si aplica): ")
                        
                        # Actualizao los nuevos atributos del objeto
                        student_obj.name = new_name
                        student_obj.last_name = new_last_name
                        student_obj.course = new_course
                        student_obj.behavior = new_behavior
                        student_obj.punctuality = new_punctuality
                        student_obj.nee = new_nee
                        student_obj.type_nee = new_type_nee

                if value:
                    print(f"Hay {len(value)} alumnos en este curso.")
                    return value
                else:
                    print("No hay alumnos en este curso.")
                    return []

    print("El curso no se encontro")
    return None  # Retornamos None si el curso no se encuentra

#Función para mostrar todos los estudiantes en la lista 
def show_students(students_list: list[dict]):
  for course_dict in students_list:
    for course, students in course_dict.items():
      print(f"Curso: {course}")
      if students:
        for student in students:
          student.show_information()
          student.show_private_information()
          print("-------------------------------------------")
      else:
        print("No hay alumnos en este curso.")
  print("----------------------------------------")
