Reto #27: Cuenta atras 

  Crea una función que reciba dos parámetros para crear una cuenta atrás.
- El primero, representa el número en el que comienza la cuenta.
- El segundo, los segundos que tienen que transcurrir entre cada cuenta.
- Sólo se aceptan números enteros positivos.
- El programa finaliza al llegar a cero.
- Debes imprimir cada número de la cuenta atrás.

Codigo:
import time

def cuenta_atras(inicio, intervalo):
    if inicio > 0 and intervalo > 0:
        while inicio >= 0:
            print(inicio)
            time.sleep(intervalo)
            inicio -= 1
    else:
        print("Los números deben ser positivos.")

inicio = int(input("Ingresa el número de inicio de la cuenta atrás: "))
intervalo = int(input("Ingresa el intervalo (en segundos) entre cada número: "))

cuenta_atras(inicio, intervalo)
