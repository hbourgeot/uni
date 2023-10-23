# 2. Realizar un ejercicio que permita calcular el valor a pagar de un producto, si se tiene los datos de entrada la cantidad de docenas que compra el cliente y el costo por unidad de este producto.

cantidad_docenas = int(input("Ingrese la cantidad de docenas que desea: "))
precio_producto = int(input("Ingrese el precio por unidad de producto que desea: "))

total_pagar = (cantidad_docenas * 12) precio_producto

print(f"El precio total a pagar es: {total_pagar}")