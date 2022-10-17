"""Esto es una prueba de git control de versiones ;) """

"""
imagina que te encuentras en un salón de videojuegos, que necesita un desarrollador. El grupo de trabajo
ha decidido contratarte para que mejores su juego de alienígenas en el espacio. Necesitan saber cuántos
puntos deberá ganar el jugador dependiendo del color del alienígena que derribe incluyendo la cantidad,
en caso de que sea rojo, el jugador obtendrá  10 puntos, en caso de que sea verde obtendrá 5 puntos y en el
caso de que sea azul obtendrá solamente 2 puntos. El puntaje final se definirá por la cantidad de alienígenas
dependiendo del color y su puntaje respectivo, todo esto sumado. Si el jugador derriba más de 10 rojos se le dará un bonus del 10%
 sobre el puntaje final, si derriba más de 5 verdes se le da un bonus del 5%, y para los azules si derribó
más de 2 uno del 2%, tenga en cuenta que el valor del puntaje final debe mostrase de tipo entero, es decir
si el resultado 32.78 debe mostrase 32. Diseñe un programa que le permita al usuario saber cuántos puntos
en total ganó luego de una partida dependiendo del color de los alienígenas que haya
derribado, y la cantidad.

Nota: Ten en cuenta que es un solo intento, el programa deberá (a través de consola) obtener el color y
el número de naves que derribo.

Por ejemplo:

Ingrese la cantidad de rojos derribados:  2
Ingrese la cantidad de verdes derribados: 5
Ingrese la cantidad de azules derribados: 12
Puntaje total: 70
"""

print("Juego de alienígenas")

#Declarando variables: puntos que vale cada alienigena por su color
rojo = 10
verde = 5
azul = 2

#Solicitando cantidades de alienigenas al usuario
num1 = int(input("Ingrese la cantidad de rojos derribados: "))
num2 = int(input("Ingrese la cantidad de verdes derribados: "))
num3 = int(input("Ingrese la cantidad de azules derribados: "))

#Hallando el valor total en puntos
PuntajeRojo = rojo * num1
PuntajeVerde = verde * num2
PuntajeAzul = azul * num3
suma = PuntajeRojo + PuntajeVerde + PuntajeAzul

if num1 >= rojo:
    puntosA = rojo * suma
    porcentaje = puntosA / 100
    suma = porcentaje + suma
if num2 >= verde:
    puntosB = verde * suma
    porcentaje1 = puntosB / 100
    suma = porcentaje1 + suma
if num3 >= azul:
    puntosC = azul * suma
    porcentaje2 = puntosC / 100
    suma = porcentaje2 + suma
total = int(suma)
print(f'Puntaje total es: {total}')
