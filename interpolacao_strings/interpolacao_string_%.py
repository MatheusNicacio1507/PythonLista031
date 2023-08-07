nome = "Carla Joaquina" #tipo str
idade = 27
altura = 1.759 #tipo float

print("Tipo da var nome: %s " % type(nome))
print("Tipo da var idade: %s " % type(idade))
print("Tipo da var altura: %s " % type(altura))

print("Nome: %s" % nome)
print("Idade: %d" % idade)
print("Altura: %.2f" % altura)
print("%s possui %d anos e tem %.2fm de altura" % (nome, idade, altura))