'''
Fazer um algoritmo que pergunte 1 número e apresente:
a) O próprio número
b) O quadrado deste número
c) A raiz quadrada deste número
'''
import math

num = float(input("Escreva um número:"))

quad = math.pow(num, 2)

raiz = math.sqrt(num)

print("Número:", num,"-","O seu Quadrado é =", quad, "-", " e sua Raíz Quadrada é =", raiz)