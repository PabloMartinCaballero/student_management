#Defino la clase student (estudiante)
class Student:

    #Atributos de clase
    school: str = "Ing Gabriel del Mazo"
    #Variable de clase que se incrementara cada vez que instancie un objeto estudiante, asignando al mismo su numero
    students_numbers = 0
    
    
    #Atributos de instancia
    def __init__(self,name:str,last_name:str,course:str,behavior:str, punctuality:str, nee:str, type_nee:str = None): #Constructor
        self.name: str = name
        self.last_name: str = last_name
        self.course: str = course
        self.behavior: str = behavior
        self.punctuality: str = punctuality
        self.nee : str = nee
        #Incremento en 1 el atributo de clase
        Student.students_numbers += 1
        #Lo asigno a un atributo de instancia
        self.student_number = Student.students_numbers

        #Condicion para saber si el alumno tiene NEE (alumnos con Necesidades Educativas Específicas) 
        #Verificamos si type_nee sigue siendo None  
          
        """         
                    Codigo con error :
                    Para acceder al valor del atributo de la instancia, debo usar self.nee

                    if nee.lower() == 'si':
                        self.type_nee:str = type_nee
                    else:
                        self.type_NEE:str = 'No posee ningun NEE'

        """
        if self.nee == 'si':
            # verifico si el usuario cargo la discapacidad, si el usuario
            # cargo que el alumno si posee, verifica que este especifico cual es
            # para ello utilizo if not, si el usuario cargo algo, el not negara ese valor
            # de esa manera descarto que el usuario no cargo algo. 
            if not type_nee:         
                raise ValueError("El tipo de NEE es obligatorio para estudiantes con NEE positivo.")                   
                                    #raise se utiliza para indicar que ha ocurrido un error. 
                                    #ValueError es un tipo específico de excepción que se 
                                    #utiliza cuando una función recibe un argumento con el tipo correcto pero con un valor inapropiado.
            self.type_nee: str = type_nee # Si el usuario cargo el tipo de nee, pasa el condicional anterior y carga el valor
        else:
            self.type_nee: str = 'No posee ningún NEE'                            
                                     

    
    #Metodo para mostrar los datos del estudiante
    def show_information(self) -> str:
        print ("Datos del alumno")
        print(f"Nombre : {self.name}")
        print(f"Apellido : {self.last_name}")
        print(f"Curso : {self.course}")
        print(f"Comportamiento del alumno en clase : {self.behavior}")
        print(f"Puntualidad del alumno: {self.punctuality}")
        
        if self.nee == 'si':
            print(f" El estudiante posee NEE de tipo : {self.type_nee}")
        else:
            print("No posee NEE")

    