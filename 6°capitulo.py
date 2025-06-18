# EXERCICIO 6.1 – Gato
print("EXERCICIO 6.1 – Gato\n")
gato = {
    "first_name": "Ze",
    "last_name": "da Manguinha",
    "age": "2",
    "apelido": " tigrezo",
}

print(gato)

print("\n----------------Fim do exercicio----------------\n")


# EXERCICIO 6.2– Numero favorito
print("EXERCICIO 6.2– Numero favorito\n")

numeroFavorito = {
    "salem": "14",
    "nagine": "23",
    "tigrezo": "45",
    "victor": "78",
    "nina": "10",
}

for name, number in numeroFavorito.items():
    print(f"{name} gosta do numero {number}")

print("\n----------------Fim do exercicio----------------\n")


# EXERCICIO 6.3– Numero favorito
print("EXERCICIO 6.3– Numero favorito\n")

glossario = {}
glossario["chapter_1"] = "numbers"
glossario["chapter_2"] = "names_cases"
glossario["chapter_3"] = "list"
glossario["chapter_4"] = "for"
glossario["chapter_5"] = "if"

for chapter, result in glossario.items():
    print(f"Eu aprendi no {chapter} sobre: {result}\n")

print("\n----------------Fim do exercicio----------------\n")


# EXERCICIO 6.4– Glossario 2
print("EXERCICIO 6.4– Glossario 2\n")

glossario2 = {
    "chapter_1": "numbers",
    "chapter_2": "names_cases",
    "chapter_3": "list",
    "chapter_4": "for",
    "chapter_5": "if",
    "chapter_5": "else",
}

glossario2["chapter_6_1"] = "dicionario"
glossario2["chapter_6_2"] = "items()"
glossario2["chapter_6_3"] = "key()"
glossario2["chapter_6_4"] = "value()"

for key, value in glossario2.items():
    print(f"Eu aprendi no {key} sobre: {value}\n")

print("\n----------------Fim do exercicio----------------\n")


# EXERCICIO 6.5– Rios
print("EXERCICIO 6.5– Rios\n")

rios_importantes = {"nilo": "Egito", "amazonas": "Brasil", "sena": "Franca"}

for rio, pais in rios_importantes.items():
    print(f"O {rio} corre pelo {pais}")

print("Os rios são: \n")
for rio in rios_importantes.keys():
    print(rio.title())

print("Os paises são: \n")
for pais in rios_importantes.values():
    print(pais.title())

print("\n----------------Fim do exercicio----------------\n")


# EXERCICIO 6.6– Enquete
print("EXERCICIO 6.6– Enquete\n")

favorite_languages = {
    "salem": "Python",
    "nagine": "C",
    "tigrezo": "Java",
    "victor": "Python",
    "nina": "C#",
}

pessoas = ["salem", "nagine", "tigrezo", "victor", "nina", "paloma", "patonguinha"]

for pessoa in pessoas:
    if pessoa in favorite_languages:
        print(f"{pessoa.title()}, obrigado por ter votado em")
    else:
        print(f"{pessoa.title()}, por favor faça sua escolha")


print("\n----------------Fim do exercicio----------------\n")


# EXERCICIO 6.7 - Pessoas
print("EXERCICIO 6.7 - Pessoas\n")

tigrezo = {
    "first_name": "Ze",
    "last_name": "da Manguinha",
    "age": "2",
    "apelido": " tigrezo",
}
salem = {
    "first_name": "salem",
    "last_name": " de souza",
    "age": "3",
    "apelido": " sarem",
}
nagine = {
    "first_name": "nagine",
    "last_name": " de souza",
    "age": "3",
    "apelido": " naguisninha",
}
people = [tigrezo, salem, nagine]

for pessoa in people:
    nome_completo = pessoa["first_name"] + " " + pessoa["last_name"]
    print(
        f"Conhecido como{pessoa["apelido"].title()}, mas na verdade seu nome é {nome_completo.title()} e possui apenas {pessoa["age"]} anos de idade"
    )

print("\n----------------Fim do exercicio----------------\n")


# EXERCICIO 6.8 - Animais de estimacao
print("EXERCICIO 6.8 - Animais de estimacao\n")

mango = {"tipo": "periquito", "dono": "victor"}
nina = {"tipo": "cachorro", "dono": "paloma"}
robsun = {"tipo": "gato", "dono": "nagine"}

pets = [mango, nina, robsun]

for pet in pets:
    print(f"O {pet["tipo"]} é do {pet["dono"].title()}")

print("\n----------------Fim do exercicio----------------\n")


# EXERCICIO 6.9 - Lugares favoritos
print("EXERCICIO 6.9 - Lugares favoritos\n")

favorite_places = {
    "victor": ["escritorio", "cama", "quintal"],
    "paloma": ["cama", "sala"],
    "salem": ["guarda roupa", "sofa", "janela"],
}
for pessoa, lugares in favorite_places.items():
    print(f"\nPara {pessoa.title()} o melhor lugar é: ")
    for lugar in lugares:
        print(lugar.title())

print("\n----------------Fim do exercicio----------------\n")


# EXERCICIO 6.10 - Numeros favoritos
print("EXERCICIO 6.10 - Numeros favoritos\n")

numeroFavorito = {
    "salem": ["14","15"],
    "nagine": ["25","45"],
    "tigrezo": ["02","11"],
    "victor": ["19","10"],
    "nina": ["80","02"],
}

for pessoa, numeros in numeroFavorito.items():
    print(f"\n O {pessoa} gosta dos numeros:")
    for numero in numeros:
        print("\t - " + numero)
        
print("\n----------------Fim do exercicio----------------\n")


# EXERCICIO 6.11 - Cidades
print("EXERCICIO 6.11 - Cidades\n")

citties = { 
    "Brasilia":{
                "country":"Brasil",
                "population":"3.094.325",
                "fact":"Brasília é a capital do Brasil e foi planejada por Lúcio Costa e Oscar Niemeyer."
                },

    "Betim":{
            "country":"Brasil",
            "population":"439.340",
            "fact":"Betim é um importante polo industrial de Minas Gerais, conhecido pela fábrica da Fiat."
            },

    "Juatuba":{
            "country":"Brasil",
            "population":"27.392",
            "fact":"Juatuba é uma cidade da Região Metropolitana de Belo Horizonte, conhecida por suas áreas verdes e tranquilidade."
            }
}

for cidade, dados in citties.items():
    print(f"\nCidade: {cidade.title()} ")

    pais = dados['country']
    populacao = dados['population']
    info = dados['fact']   
    print(f"Pais:{pais.title()}")
    print(f"Populacão: {populacao.title()}")
    print(f"Info: {info}")


print("\n----------------Fim do exercicio----------------\n")


# EXERCICIO 6.12 - Extensões
print("EXERCICIO 6.12 - Extensões\n")

citties = { 
    "Brasilia":{
                "country":"Brasil",
                "population":"3.094.325",
                "fact":"Brasília é a capital do Brasil e foi planejada por Lúcio Costa e Oscar Niemeyer."
                },

    "Betim":{
            "country":"Brasil",
            "population":"439.340",
            "fact":"Betim é um importante polo industrial de Minas Gerais, conhecido pela fábrica da Fiat."
            },

    "Juatuba":{
            "country":"Brasil",
            "population":"27.392",
            "fact":"Juatuba é uma cidade da Região Metropolitana de Belo Horizonte, conhecida por suas áreas verdes e tranquilidade."
            }
}

for cidade, dados_cidade in citties.items():
    print(f"\nCidade: {cidade.title()} ")
    
    for dado, info in dados_cidade.items():
        print(f"{dado.title()} : {info}")