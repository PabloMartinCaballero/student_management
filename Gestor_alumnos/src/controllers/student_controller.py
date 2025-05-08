from typing import Optional
#Importo la DB y su controlador para realizar los controles utilizo un path absoluto para traerla
from src.data.db_students import students_list, check_db
from src.students.student import Student

#Aplicación de CRUD para manejar la DB 

def create_student() -> object:
 #Creo las variables que seran agregadas a la función que creara los objetos
    name:str = input("ingrese el nombre del alumno : ")
    last_name:str = input("ingrese el apellido del alumno : ") 
    dni: str = input("Ingrese el DNI del alumno : ")
    home_adress: str = input("Ingrese la dirección del alumno")
    course: str = input("Ingrese el curso del alumno")
    behavior: str = input("Ingrese la dirección del alumno")
    punctuality: str = ""
    nee: str = input ("¿El alumno posee algun NEE?, ingrese si o no")
    type_nee: str = input ("Ingrese el tipo de nee que posee")

    new_student = Student(name,last_name,dni,home_adress,course,behavior,punctuality,nee,type_nee)
    return new_student

                #Objeto   #Lista
def add_student(student, db_students):
    #Guardo el atributo course en una variable
    student_course = student.course

    for course_dict in db_students:
        for division, students in course_dict.items():
            if division == student_course:
                students.append(Student)  # Agregamos el objeto student a la DB
                return True  # Indicamos que se agregó el estudiante
    print(f"No se encontró la división")
    return False
                
                



    
