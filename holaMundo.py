#los numeros multiplos de 3 = fizz, 5 = buzz y 3,5 = fizzbuzz 
"""n = 30
i = 1
while i <= n:
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz') 
    if i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
    i += 1"""

#verificar si es un anagrama
"""palabra1 = input('introduce la primera palabra: ')
palabra2 = input('indroduce la segunda palabra: ')

r = True
if len(palabra1) != len(palabra2) or palabra1 == palabra2 :
    r = False
    print('¿es un anagrama? :' + str(r))
else:
    i = 0
    p = palabra2
    while len(p) > 0 and r == True:
        if palabra1[i] in p :
            p = p.replace(palabra1[i], "", 1)
            i += 1
        else:
            r == False
    print('¿es un anagrama? :' + str(r))"""

#primeros 50 numeros de la secuencia de fibonacci   
"""a = 0
b = 1
n = 50
print( str(a))
print(str(b))
for _ in range(n-2):
    a, b = b, a + b
    print(str(b))"""
    
#imprimir los numeros primos del 1 al 100
    
"""def esPrimo(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5) + 1):
        if(n % i == 0):
            return False
    return True

for i in range(1,101):
    if esPrimo(i):
        print(i)"""

#calcular area de un poligono
#print("""           triangulo = 1
#          cuadrado = 2
#          rectangulo = 3""")
"""n =int(input("seleccione un poligono : "))
if n == 1:
    a = int(input('base: '))
    b = int(input('altura: '))
    r = (a * b) / 2
    print('el area del triangulo es: ' + str(r))
elif n == 2:
    a = int(input('lado 1: '))
    b = int(input('lado 2: '))
    r = a * b
    print('el area del cuadrado es: ' + str(r))
elif n == 3:
    a = int(input('lado1: '))
    b = int(input('lado2: '))
    r = a * b
    print('el area del rectangulo es: ' + str(r))
else:
    print('desconocido')"""
    
#calcular el aspect ratio de una imagen
"""from PIL import Image
import math
img = Image.open("C:\\Users\\DELL\\OneDrive\\Documentos\\practica-phyton\\caja.jpg")
ancho, alto = img.size
print(f'ancho : {ancho} pixeles')
print(f'alto : {alto} pixeles')

divisor = math.gcd(ancho, alto)
print(f"el aspect ratio es de {ancho//divisor}:{alto//divisor}")"""

#invertir palabras
"""palabra1 = input('introduce una palabra: ')
lista_palabra = list(palabra1)
i = 0
j = len(palabra1) - 1
while i < j:
    lista_palabra[i], lista_palabra[j] = lista_palabra[j], lista_palabra[i]  
    i += 1
    j -= 1
palabra_invertida = ''.join(lista_palabra)
print(f'la palabra invertida es: {palabra_invertida}')"""

#contador de palabras
print('----------CANTIDAD DE PALABRAS POR PALABRA---------')
texto = input('indroduce una oracion: ')

texto = texto.lower()
signos = ".,[]}{)(=&%$#!:,;"
texto_limpio = ""
for caracter in texto:
    if caracter not in signos:
        texto_limpio += caracter

texto = texto_limpio.split()
dic = {}

for palabra in texto:
    if palabra in dic:
        dic[palabra] += 1
    else:
        dic[palabra] = 1

for palabra, cantidad in dic.items():
    print(f"la palabra '{palabra}' se repite {cantidad} veces")
    
#convertir un decimal a binario
"""print("----------convertir un numero decimal a binario----------")
n = int(input('numero: '))
r = ""
while n > 0:
    r, n = str(n % 2) + r, n // 2
print(f'el numero en binario es: {r}')"""

#comprobar que los parenteceis, llaves y corchetes esten cerradas
"""def expresion_equilibrada(expr):
  pila = []
  pares = {")":"(","]":"[", "}":"{"}
  for caracter in expr:
      if caracter in "([{":
          pila.append(caracter)
      elif caracter in ")]}":
          if not pila or pila[-1] != pares[caracter]:
              return False
          pila.pop()
  return not pila

print('----------EXPRESIONES EQUILIBRADAS----------')
expr = input('introduzca un expresion matematica: ')
r = expresion_equilibrada(expr)
print(f"{r}")"""

#eliminar caracteres







