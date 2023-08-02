'''
Fazer um programa que pergunte o salário de um funcionário e apresente este salário com um aumento de 15%.
'''

print("Qual o seu salário?")

sal = float(input("Insira o seu salário:"))

aum = sal * 15 / 100

sal = aum + sal

print("Com o acréscimo de 15%, o seu salário é R$", sal)
