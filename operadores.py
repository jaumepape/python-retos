num1 = input ("Di un número: ")
num2 = input("Di otro número: ")
num1 = int(num1)
num2 = int(num2)
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
division_entero = num1 // num2
modulo = num1 % num2
potencia = num1 ** num2

output_string = f'La suma de estos valores es {suma}, la resta {resta}, la multiplicación {multiplicacion}, la división {division}, la divisón con números enteros {division_entero}, el módulo {modulo} y la potencia {potencia}.'
print(output_string)

print(f'La suma de estos valores es {suma}')
print(f'La resta de estos valores es {resta}')
print(f'La multiplicación de estos valores es {multiplicacion}')
print(f'La división de estos valores es {division}')
print(f'La división con números enteros de estos valores es {division_entero}')
print(f'El módulo de estos valores es {modulo}')
print(f'La potencia de estos valores es {potencia}')