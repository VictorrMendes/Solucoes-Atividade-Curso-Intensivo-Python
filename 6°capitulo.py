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
    "salem": "14",
    "nagine": "23",
    "tigrezo": "45",
    "victor": "78",
    "nina": "10",
}
participou = []

participou.append(favorite_languages.keys())
