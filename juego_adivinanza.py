
import random

cant_intentos = 0
cant_max_intentos = 5
numero_secreto = random.randint(1,100)
adivinado = False

print ("Bienvenido al juego de adivinar el número secreto")

while not adivinado: 

    if not cant_intentos < cant_max_intentos:
        print ("¡Game over!")
        print ("El número secreto era:", numero_secreto)
        break

    entrada = input("Introduce un número del 1 al 99: ") # input trae un string, hay que castearlo a int
    numero = int(entrada)

    if numero == numero_secreto:
        print ("Felicitaciones, adivinaste el número secreto!")
        adivinado = True
    elif numero < numero_secreto:
        print ("El número es mayor al ingresado")
    else:
        print ("El número es menor al ingresado")
    
    cant_intentos += 1

