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

while True:
    n = input_integer(">Ingrese la catnidad de estudiantes")
    if n > 0: break

for i in range(n):
    print("-"*10+f"ESTUDIANTE {i+1}"+"-"*10)
