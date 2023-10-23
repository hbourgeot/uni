# 3. Realizar un programa que permita tomar como entrada 5 notas de estudiantes, que son Matemática, Física, Programación, Inglés y Química y calcular el promedio a ese estudiante.

nota1 = float(input("Ingrese la nota de Matemática: "))
nota2 = float(input("Ingrese la nota de Física: "))
nota3 = float(input("Ingrese la nota de Programación: "))
nota4 = float(input("Ingrese la nota de Inglés: "))
nota5 = float(input("Ingrese la nota de Química: "))

promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print(f"El promedio del estudiante es igual a: {promedio}")