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



def add_student (student):
    
