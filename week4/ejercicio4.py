# Calc the area and volume

from math import pi

cilindre_rad = float(input('Enter the radius of the cilindre'))
cilindre_height = float(input('Enter the height of the cilindre'))

cilindre_area = 2 * pi * cilindre_rad * (cilindre_rad + cilindre_height)
cilindre_volume = pi * (cilindre_rad ** 2) * cilindre_height

print(f'El volumen del cilindro es igual a: {cilindre_volume}')
print(f'El área del cilindro es igual a: {cilindre_area}')