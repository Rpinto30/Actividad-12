students = {}
error_mesagge = '-'*50+'\n'+"✖"*5+"   Lo siento valor no valido, intentelo nuevamente   "+"✖"*5

def input_integer(message): #INGRESAR UN ENTERO Y VERIFICAR QUE SU ENTRADA SEA VALIDA
    while True:
        try:
            value = int(input(message))
            break
        except ValueError: print(error_mesagge)
        except Exception as e: print('-'*50+'\n'+"✖"*5+"   Lo siento, ocurrió un error inesperado, intentelo nuevamente   "+f":{e}"+"✖"*5)
    return value

try:
    while True:
        n = input_integer(">Ingrese la catnidad de estudiantes: ")
        if n > 0: break
        elif n == 0: print("Lo sentimos, debe de ingresar una cantidad de estudiantes mayor a 0")
        else: print(error_mesagge)

    for i in range(n):
        print("-"*10+f"ESTUDIANTE {i+1}"+"-"*10)
        name = input(">Ingrese el nombre: ")
        while True:
            c_notes = input_integer(">Ingrese la catnidad de notas: ")
            if c_notes > 0: break
            elif c_notes == 0: print("Lo sentimos, debe de ingresar una cantidad de notas mayor a 0")
            else: print(error_mesagge)
        notes = []
        for j in range(c_notes):
            note = input_integer(f"   >Ingrese nota {j+1}: ")
            notes.append(note)

        students[name] = notes
    #CALCULAR PROMEDIOS
    print(f"{'Nombre':<30}{'Promedio':<20}")
    for names, values in students.items():
        print(f"{names:<30}{sum(values)/len(values)}")
except ZeroDivisionError: print("Lo sentimos, usted intentó sacar el promedio de cero notas")
except Exception as e: print("Lo sentimos, ocurrió un error inesperado", e)