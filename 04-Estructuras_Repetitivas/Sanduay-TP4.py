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

