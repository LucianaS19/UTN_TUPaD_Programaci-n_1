#ejercicio1
print("Hola mundo!")

#ejercicio2
nombre = input("Ingrese su nombre:")
print(f"Hola {nombre}!")

#ejercicio3
nombre = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido:")
edad = input("Ingrese su edad:")
lugar = input("Ingrese su lugar de residencia:")
print(f"Hola, soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")

#ejercicio4
pi = 3.14159
radio = float(input("Ingrese el radio del círculo: "))
area = pi * radio ** 2
perimetro = 2 * pi * radio
print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

#ejercicio5
segundos = int(input("Ingrese el tiempo en segundos: "))
horas = segundos / 3600
print(f"Los segundos ingresados en horas son: {horas:.2f}")

#ejercicio6
numero = int(input("Ingrese un número y podrá saber su tabla de multiplicar: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

#ejercicio7
num1 = int(input("Ingrese el primer número (distinto de 0): "))
num2 = int(input("Ingrese el segundo número (distinto de 0 ): "))
suma = num1 + num2
resta = num1 - num2
division = num1 / num2
multiplicacion = num1 * num2
print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"La división es: {division}")
print(f"La multiplicación es: {multiplicacion}")

#ejercicio8
altura = float(input("Ingrese la altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
imc = peso / (altura ** 2)
print(f"Su índice de masa corporal es: {imc}")

#ejercicio9
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")

#ejercicio10
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))   
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los tres números es: {promedio}")