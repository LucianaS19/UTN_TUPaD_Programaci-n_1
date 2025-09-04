#Ejercicio1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Eres mayor de edad.")

#Ejercicio2
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobaste la materia.")
else:
    print("No aprobaste la materia.")

#Ejercicio3
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("Por favor ingrese un número par.")

#Ejercicio4
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Eres un niño/a.")
elif 12 <= edad < 18:   
    print("Eres un adolescente.")
elif 18 <= edad < 30:
    print("Eres un adulto/a joven.")
elif 30 <= edad < 60:
    print("Eres un adulto/a.")

#Ejercicio5
contraseña = input("Ingrese la contraseña: ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Contraseña válida.")
else:
    print("Error, por favor ingrese una contraseña de entre 8 y 14 caracteres.")

#Ejercicio6
import random
from statistics import mode, median, mean
num_aleatorios = [random.randint(1, 100) for _ in range(50)]

moda = mode(num_aleatorios)
mediana = median(num_aleatorios)
media = mean(num_aleatorios)

print(f"Números generados: {num_aleatorios}")
print(f"Moda: {moda}")  
print(f"Mediana: {mediana}")
print(f"Media: {media:.2f}")

if media > mediana and mediana > moda:
    print("Distribución sesgada a la derecha.")
elif media < mediana and mediana < moda:
    print("Distribución sesgada a la izquierda.")
elif media == mediana == moda:
    print("Sin sesgo.")
else:
    print("Distribución irregular.")
#tuve varias dificultades para realizar este ejercicio, aún me quedan dudas sobre el resultado final. Pero seguire investigando sobre la función y complementare con las clases.

#Ejercicio7
frase = input("Ingrese una frase: ")
vocales = "aeiouAEIOU"

if frase[-1] in vocales:
    frase_resultado = frase + "!"
    print(frase_resultado)

#Ejercicio8
nombre = input("Ingrese su nombre: ")

print("Seleccione una opción:")
print("1. Nombre en mayúsculas")
print("2. Nombre en minúsculas")
print("3. Nombre con la primera letra en mayúscula")
opcion = int(input("Ingrese el número de la opción deseada (1, 2 o 3): "))

if opcion == 1:
    print(nombre.upper())       
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

#Ejercicio9
magnitud = float(input("Ingrese la magnitud del sismo: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#Ejercicio10
hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper()
mes = int(input("¿Qué mes del año es? (1-12): "))
dia = int(input("¿Qué día es?: "))

if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
    periodo = "dic21-mar20"
elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
    periodo = "mar21-jun20"
elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
    periodo = "jun21-sep20"
else:  # sep21-dic20
    periodo = "sep21-dic20"

if hemisferio == "N":
    if periodo == "dic21-mar20":
        estacion = "Invierno"
    elif periodo == "mar21-jun20":
        estacion = "Primavera"
    elif periodo == "jun21-sep20":
        estacion = "Verano"
    else:
        estacion = "Otoño"
elif hemisferio == "S":
    if periodo == "dic21-mar20":
        estacion = "Verano"
    elif periodo == "mar21-jun20":
        estacion = "Otoño"
    elif periodo == "jun21-sep20":
        estacion = "Invierno"
    else:
        estacion = "Primavera"

print(f"Estación del año: {estacion}")