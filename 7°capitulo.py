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
    
print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 7.4 Ingredientes para pizza
print("EXERCICIO 7.4 Ingredientes para pizza\n")

prompt = ("\nPor favor, digite os ingredientes para a pizza")
prompt += ("\nDigite 'quit' para encerrar\n")

active = True
while active:
    ingrediente = input(prompt)

    if ingrediente == "quit":
        active = False
    else:
        print(f"\nO ingrediente {ingrediente} será adcionado! ")
        
print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 7.5 - Ingressos para cinema
print("EXERCICIO 5 - Ingressos para cinema")


promptNew = "\nDigite sua idade para calculo de valores"
promptNew += "\nPara sair, digite 'sair' \n"


while True:
    resposta = input(promptNew)
    
    if resposta == "sair":
        print("\nObrigado por participar! Adeus!")
        break


    resposta = int(resposta)


    if resposta <= 3:
        print("\nO seu ingresso é gratis")
        
    elif resposta <= 12:
        print("\nO seu ingresso custa R$10,00 ")
        
    elif resposta > 12:
        print("\nO seu ingresso custa R$15,00")
        

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 7.7 - infinito
print("EXERCICIO 7.7 - infinito")

# numero = 2
# infinito = 0
# while numero < 5:
#     infinito += 1
#     print(infinito)
    
    
print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 7.8 - lanchonete
print("EXERCICIO 7.8 - lanchonete")
    
sandwich_orders  = ["natural","vegano", "bacon" ]
finished_sandwich = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    
    finished_sandwich.append(sandwich)
    print(f"Seu sandwich de {sandwich} esta pronto")
    
print(finished_sandwich)

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 7.9 - sem pastrami
print("EXERCICIO 7.9 - sem pastrami")

sandwich_orders = ["pastrami", "natural","pastrami","vegano", "pastrami","bacon", "pastrami"]

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
    
print(sandwich_orders)

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 7.10 - Ferias dos sonhos
print("EXERCICIO 7.10 - Ferias dos sonhos")

prompt = "Se pudesse visitar um lugar do mundo, para onde você iria? "
resultado = {}
ativo = True

while ativo:
    nome = input("Qual o seu nome? ")
    resposta_user = input(prompt)
    
    resultado[nome] = resposta_user
    
    continuar = input("sair? S/n")
    
    if continuar == "s":
        ativo = False
        
for nome, local in resultado.items():
    print(f"O {nome} quer ir à {local}")