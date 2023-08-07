'''
Elaborar um programa que pergunte quatro valores inteiros e apresente 2 resultados:
a) Resultado de suas adições
b) Resultado de suas multiplicações
'''

print("Abaixo, escreva quatro valores inteiros")

valor1 = int(input("Insira o primeiro valor inteiro:"))
valor2 = int(input("Insira o segundo valor inteiro:"))
valor3 = int(input("Insira o terceiro valor inteiro:"))
valor4 = int(input("Insira o quarto valor inteiro:"))

soma = valor1 + valor2 + valor3 + valor4

multi = valor1 * valor2 * valor3 * valor4

print("A adição desses números é =", soma, "e a multiplicação entre esses números é =", multi)