print("EXERCICIO 6.1 – Gato\n")
gato = {'first_name': 'Ze',
        'last_name': 'da Manguinha',
        'age': '2' ,
        'apelido': ' tigrezo'}

print(gato)

print("\n----------------Fim do exercicio----------------\n")



# EXERCICIO 6.2– Numero favorito
print("EXERCICIO 6.2– Numero favorito\n")

numeroFavorito =   {'salem': '14',
                    'nagine': '23',
                    'tigrezo': '45',
                    'victor': '78',
                    'nina': '10'}

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

