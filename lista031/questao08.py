'''
Fazer um programa que calcule e apresente a quantidade de litros que um automóvel gastará em uma viagem. O
programa deve coletar as seguintes informações: Distância a percorrer na viagem, em quilômetros; qual é o
valor do consumo médio do automóvel, em quilômetros por litro.
'''

dis = float(input("Qual distância será percorrida durante a viagem, em quilômetros? "))

cons = float(input("Qual o consumo médio do automóvel, em quilômetros por litro? "))

litro = dis/cons

print(f"Seu carro vai consumir: {litro:.0f} litros")