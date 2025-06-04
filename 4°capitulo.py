


# EXERCICIO 4.1 Pizzas
empadas = [ "Calabreza", "Bacon","Frango"]

for empada in empadas:
    print(f"Eu gosto de empada de {empada}")
    
print("Eu realmente gosto de empada")

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 4.2 Animais

animais = ["Gato","Cachorro","Cabra"]

for animal in animais:
    print(f"Um {animal} seria um bom animal de estimacao")
print("Qualquer um desses animais seria um ótimo animal de estimação")

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 4.3 Contando até vinte

numeros = []

for numero in range(1,21):
    numeros.append(numero)
print(numeros)

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 4.4 Um milhão

#numerosX = []

#for numero in range(1,1000001):
    #numerosX.append(numero)
#print(numerosX)

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 4.5

numerosX = []

for numero in range(1,1000001):
    numerosX.append(numero)
print(min(numerosX))
print(max(numerosX))
print(sum(numerosX))



print("\n----------------Fim do exercicio----------------\n")
# EXERCICIO 4.6 Numeros Ímpares

numerosI = []

for numero in range(1,21,2):
    numerosI.append(numero)
print(numerosI)

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 4.7 Três

multiplos = []

for numero in range(3,31):
    if numero % 3 == 0:
        multiplos.append(numero)

print(multiplos)

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 4.8 Cubos

cubos = []

for cubo in range(1,11):
    print(cubo**3)
    cubos.append(cubo**3)
    
print(cubos)

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 4.9 Comprehension de cubos

quadrados = [valor**3 for valor in range(1,11)]
print(quadrados)

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 4.10 Fatias

print(f"Os 3 primeiros itens da lista são: {cubos[:3]}")
print(f"Os 3 itens do meio da lista são: {cubos[4:7]}")
print(f"Os 3 ultimos itens da lista são: {cubos[-3:]}")

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 4.11 Minhas pizzas, suas pizzas
empadas = [ "Calabreza", "Bacon","Frango"]

friends_empadas = empadas[:]

empadas.append("Peperoni")
friends_empadas.append("Gergilin")

print("Minhas empadas favoritas são:\n")
for empada in empadas:
    print(empada)
    
print("\n As empadas favoritas do meu amigo são: \n")
for friend in friends_empadas:
    print(friend)

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 4.12 Mais laços

my_foods = ['Pizza', 'falafel','carrot cake']
friend_food = my_foods[:]

print("My favorite foods are: \n")

for foods in my_foods:
    print(foods)
    
print("\n My friend's favorite foods are: \n")

for foods in friend_food:
    print(foods)
    
print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 4.13 – Buffet

pratos = ("arroz", "feijão", "frango", "salada", "batata frita")
print("Cardápio original:")

for prato in pratos:
    print(prato)


pratos[1] = "lentilha"
print(pratos)


pratos = ("arroz", "lentilha", "frango", "salada de frutas", "batata frita")

print("\nCardápio revisado:")
for prato in pratos:
    print(prato)

print("\n----------------Fim do exercicio----------------\n")
