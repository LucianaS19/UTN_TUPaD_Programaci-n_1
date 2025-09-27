#Ejercicio1
for i in range(101):
    print(i)

#Ejercicio2
num = abs(int(input("Ingrese un número entero: ")))
contador = 0

if num == 0:
    contador = 1
else: 
    while num > 0:
        num //= 10
        contador += 1

print(f"La cantidad de dígitos es: {contador}")

#Ejercicio3
valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
if valor1 > valor2:
    valor1, valor2 = valor2, valor1
suma = 0
for i in range(valor1, valor2 + 1):
    suma += i
print(f"La suma entre {valor1} y {valor2} es: {suma}")

#Ejercicio4
print("Ingrese números enteros (0 para finalizar):")
suma = 0
while True:
    num = int(input())
    if num == 0:
        break
    suma += num
print(f"La suma total es: {suma}")

#Ejercicio5
random = __import__('random')
num_secreto = random.randint(0, 9)
intentos = 0
print("Adivina el número secreto entre 0 y 9.")

while True:
    intento = int(input("Ingrese su intento: "))
    intentos += 1
    if intento == num_secreto:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break
    else:
        print("Número incorrecto. Intenta de nuevo.")     

#Ejercicio6
for i in range(100, -1, -2):
    print(i)           

#Ejercicio7
while True:
    n = int(input("Ingrese un número entero positivo: "))
    if n > 0:
        break
    print("El número debe ser positivo. Intente nuevamente.")

    suma = 0
for i in range(n + 1):  # De 0 a n (inclusive)
    suma += i

print(f"La suma de los números de 0 a {n} es: {suma}")

#Ejercicio8
cantidad = 100
pares = 0
impares = 0
negativos = 0
positivos = 0
ceros = 0

print(f"Ingrese {cantidad} números enteros:")

for i in range(cantidad):
    numero = int(input(f"Número {i+1}: "))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1

print("Resultados:")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

#Ejercicio9
cantidad = 100
suma = 0

print(f"Ingrese {cantidad} números enteros:")

for i in range(cantidad):
    numero = int(input(f"Número {i+1}: "))
    suma += numero

media = suma / cantidad

print(f"La media de los {cantidad} números es: {media:.2f}")

#Ejercicio10
num = int(input("Ingrese un número entero: "))
es_negativo = num < 0
num = abs(num)
num_invertido = 0

while num > 0:
    digito = num % 10  
    num_invertido = num_invertido * 10 + digito  
    num = num // 10  
if es_negativo:
    num_invertido = -num_invertido

print(f"El número con dígitos invertidos es: {num_invertido}") 

