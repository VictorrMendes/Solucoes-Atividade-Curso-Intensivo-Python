# EXERCICIO 7.1 - Locação de automóveis
print("EXERCICIO 7.1 - Locação de automóveis\n")



print("Bem vindo a nossa loja")
escolha = input("\n Qual tipo de carro você esta buscando? ")

print(f"\nOk, deixe-me ver se consigo um {escolha.title()} para você")

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 7.2 - lugares em um restaurante
print("EXERCICIO 7.2 - lugares em um restaurante\n")

lugares = input("Mesa para quantos senhor: ")
lugares = int(lugares)

if lugares >= 8:
    print("Desculpe, no momento não temos lugares. Favor aguardar")
else:
    print("Sua mesa esta pronta")
    
print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 7.3 - multiplos de dez
print("EXERCICIO 7.3 - multiplos de dez\n")

numero = input("Por favor digite um numero ")
numero = int(numero)

if numero % 10 == 0:
    print("Esse numero é divisivel por 10")
else:
    print("Esse numero não é divisivel por 10")