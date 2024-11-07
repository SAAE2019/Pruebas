# Definimos algunas variables simples
nombre = "Juan"
edad = 25
temperaturas = [22, 18, 25, 30, 15]  # Esto es un arreglo (lista) de temperaturas

# Definimos una función para saludar
def saludar(nombre):
    print(f"Hola, {nombre}!")

# Función para sumar dos números
def sumar(a, b):
    return a + b

# Uso de la función saludar
saludar(nombre)

# Mostramos un mensaje si la edad es mayor o igual a 18
if edad >= 18:
    print(f"{nombre} es mayor de edad.")
else:
    print(f"{nombre} es menor de edad.")

# Bucle 'for' para iterar sobre un arreglo de temperaturas y mostrar un mensaje
print("Las temperaturas de la semana son:")
for temp in temperaturas:
    print(temp)

# Bucle 'while' para contar de 1 a 5
contador = 1
print("Contando hasta 5 con 'while':")
while contador <= 5:
    print(contador)
    contador += 1  # Incrementamos el contador

# Bucle 'do while' (en Python, usamos un 'while' con una condición al final)
# Este bloque es más como un 'while', ya que Python no tiene un 'do while' como tal.
# Sin embargo, se puede simular con 'while True' y una condición de salida.
print("Contando hasta 3 con 'do while':")
contador = 1
while True:
    print(contador)
    contador += 1
    if contador > 3:
        break  # Rompe el bucle cuando contador es mayor a 3

# Concatenación de cadenas y uso de variables
mensaje = "La suma de 3 y 5 es: " + str(sumar(3, 5))
print(mensaje)
