# 1. Realiza un programa en python que permita tomar dos datos de entrada el cual viene siendo el producto de una ferretería, cada producto contiene cinco tipos de productos en almacén. Calcular la cantidad total de productos en almacén

nombre_producto = input("Ingrese el nombre del producto: ")
cantidad_producto = int(input(f"Ingrese la cantidad del producto {nombre_producto}: "))

tipo1 = "RAM DDR4"
cantidad_tipo1 = 5

tipo2 = "SSD M.2 NvME"
cantidad_tipo2 = 2

tipo3 = "Monitor 25'"
cantidad_tipo3 = 9

tipo4 = "Case MicroATX"
cantidad_tipo4 = 19

tipo5 = "Teclado Mecánico"
cantidad_tipo5 = 14

total_almacen = cantidad_producto + cantidad_tipo1 + cantidad_tipo2 + cantidad_tipo3 + cantidad_tipo4 + cantidad_tipo5

print(f"La cantidad total de productos en almacén es: {total_almacen}")



