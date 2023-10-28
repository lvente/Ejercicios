# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 08:19:53 2023

@author: Usuario
"""

'''1)	Dada una cadena de texto imprimirla de forma invertida, 
Ejemplo ingresa “Automovil” salida "livomotuA

2)	Dada una cadena de texto y un carácter contar cuantas veces lo contiene
Ejemplo ingresa “Automovil Automovil Automovil”, carácter ‘A’ salida "3"

3)	Calcular la distancia Hamming para las cadenas: “AutomovilW”, “Aotumovilr”, salida "3"
Lanzar una excepción si las cadenas tienen diferente longitud

4)	Dada una cadena de texto contar cuantos números contiene
Ejemplo ingresa “ada123456789DDDD11231D”, salida "14"

5)	Dada una cadena de texto contar cuantas palabras contiene
Ejemplo ingresa “  Automovil Automovil Automovil Automovil ”, salida "4"

Condiciones
Cada programa debe permitir el ingreso de la información requerida solicitando al usuario los valores
Las respuestas deben ser realizadas en una solución con al menos un proyecto de consola y una librería de clases 
La solución se debe entregada en un repositorio GitHub, donde se evidencie el uso de al menos 2 commits 
y 2 ramas una main otra de desarrollo y su respectiva integración"'''


#1)
print("Ingresa por favor la palabra que deasea invertir")
entrada = str(input())

tamaño =  len(entrada)
lista = []
for x in entrada:
    lista.append(x)

print(lista)

segundalista= []

contador=1

print(len(lista))

for x in lista:    
    
    segundalista.append(lista[len(lista)-contador])
    contador = contador+1
    
print(segundalista)

    
#2
palabra = "Este Automovil, es muy veloz y puede llegar a 330KM/H. Este Automovil es de color rojo, debes comprar este Automovil"
segundapalabra= ""
contador = 0
longitud = len(palabra)
for x in range(1):
    
    if palabra.count("Automovil"):
        contador=palabra.count("Automovil")
        
print(contador)
        
            
        

segundocontador = 0

for x in range(1):
    
    
    if palabra.count("A"):
        
        segundocontador = palabra.count("A")
        

print(segundocontador)



#3
lista = ['AutomovilW', 'Aotumovilr']

palabra1, palabra2 = lista


'''try:

except ValueError("Error"):'''
    

#4

print("Por favor ingrese el codigo AlfaNumerico")

codigo = input()

contadorcodigo = 0
contadorcodigo2 = 0
contadorcodigo3 = 0
contadorcodigo4 = 0
contadorcodigo5 = 0
contadorcodigo6 = 0
contadorcodigo7 = 0
contadorcodigo8 = 0
contadorcodigo9 = 0
contadorcodigo0 = 0

if codigo.find("1"):
    contadorcodigo=codigo.count('1')

if codigo.find("2"):
    contadorcodigo2=codigo.count('2')
if codigo.find("3"):
    contadorcodigo3=codigo.count('3')
if codigo.find("4"):
    contadorcodigo5=codigo.count('4')
if codigo.find("5"):
    contadorcodigo6=codigo.count('5')
if codigo.find("6"):
    contadorcodigo6=codigo.count('6')
if codigo.find("7"):
    contadorcodigo7=codigo.count('7')
if codigo.find("8"):
    contadorcodigo8=codigo.count('8')
if codigo.find("9"):
    contadorcodigo9=codigo.count('9')
if codigo.find("0"):
    contadorcodigo0=codigo.count('0')
    
print(contadorcodigo2 + contadorcodigo+ contadorcodigo3+ contadorcodigo4+ contadorcodigo5+ contadorcodigo6+ contadorcodigo7+ contadorcodigo8+ contadorcodigo9+ contadorcodigo0)
    
    
#5



    
    