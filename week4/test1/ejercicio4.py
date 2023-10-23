# 4. Realizar un ejercicio que permita ingresar y calcular el área y volumen de un cilindro sabiendo que el volumen es pi * Radio por altura y el area es 2 por pi por radio, mostrar el resultado del volumen y del área.

from math import pi

altura = float(input("Ingrese la altura del cilindro: "))
radio = float(input("Ingrese el radio del cilindro: "))

volumen = pi * (radio ** 2) * altura
area = 2 * pi * radio * (radio + altura)

print(f"Área del cilindro: {area}\nVolumen del cilindro: {volumen}")