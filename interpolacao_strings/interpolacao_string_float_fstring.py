valor1 = 8.75217
valor2 = 73932.6
valor3 = 11.349

#formatação apenas com valores float

print(f"valor 1: {valor1:f}")

#formatação float com decimal em 2 números

print(f"valor 1: {valor1:.2f}")
print(f"valor 2: {valor2:.2f}")
print(f"valor 3: {valor3:.2f}")

#formatação float com separdor de milhares e decimal em 2 digitos

print(f"Valor 2: {valor2:,.2f}")

#formatação float, com total de 10 dígitos (números e ponto), sendo 2 decimais

print(f"valor 1: {valor1:10.2f}")
print(f"valor 2: {valor2:10.2f}")
print(f"valor 3: {valor3:10.2f}")

#semelhante ao anterio, mas preenche casas antes do ponto com zero quando necessário

print(f"valor 1: {valor1:010.2f}")
print(f"valor 2: {valor2:010.2f}")
print(f"valor 3: {valor3:010.2f}")



valor4 = 0.7536

#formatção float exibindo em percentual com decimal em 1 digito
print(f"Valor 4: {valor4:.1%}")

#incluindo R$ antes do valor e substituindo a virgula do milhar por underline
texto_valor2 = f"R$ {valor2:_.2f}"
print(f"Texto valor 2: {texto_valor2}")

#substituindo o que é ponto por virgula e o que é underline por ponto
texto_valor_br = texto_valor2.replace(".",",").replace("_",".")
print(f"Texto valor BR: {texto_valor_br}")