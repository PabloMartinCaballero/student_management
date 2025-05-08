students_list: list[dict] = [
    {"1°1°": []},
    {"1°2°": []},
    {"2°": []},
    {"3°": []},
    {"4°": []},
    {"5°": []},
    {"6°": []},
]

# Función para saber si existe el curso y retornar la lista de estudiantes si hay.
# Aplicación del patron Guard Clausule.

course_number = input('Elija un curso : ')

def check_db(course_number: str) -> list:
    for course_dict in students_list:
        for key, value in course_dict.items():
            print(f"Valor de la clave: {key}")
            if key == course_number:
                print(f"El curso {course_number} existe")
                if value:  
                    print(f"Hay {len(value)} alumnos en este curso.")
                    return value  
                else:
                    print("No hay alumnos en este curso.")
                    return []  

    print("El curso no se encontro")
    return None  # Retornamos None si el curso no se encuentra

