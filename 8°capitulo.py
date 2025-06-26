# EXERCICIO 8.1 - Mensagem 
print("EXERCICIO 8.1 - Mensagem ")

def display_message():
    print("Hello word, estou aprendendo função")
display_message()

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 8.2 - Livro favorito
print("EXERCICIO 8.2 - Livro favorito")

def favorite_book(title):
    print(f"Meu livro favorito é {title}")
favorite_book("Percy Jacson")

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 8.3 - Camiseta
print("EXERCICIO 8.3 - Camiseta")

def make_shirt(tamanho, texto_estampa):
    print(f"A camisa será do tamanho {tamanho} com a estampa escrito {texto_estampa}.")

make_shirt("G", "Ateu dispor")
make_shirt(tamanho="G", texto_estampa="Ateu dispor")

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 8.4 - Camisetas Grandes
print("EXERCICIO 8.4 - Camisetas Grandes")

def make_shirt(tamanho="G", texto_estampa="Eu amo Python"):
    print(f"A camisa será do tamanho {tamanho} com a estampa escrito {texto_estampa}.")

make_shirt()
make_shirt(tamanho="M")
make_shirt(tamanho="p", texto_estampa="Ateu dispor")

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 8.5 - Cidades
print("EXERCICIO 8.5 - Cidades")

def describe_city(cidade, pais="desconhecido"):
    print(f"{cidade.title()} está localizada em {pais.title()}")
    
describe_city("mexico")
describe_city("Brasilia", "Brasil")
describe_city("Tokio", "Japão")



print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 8.6 Nomes de cidades
print("EXERCICIO 8.6 Nomes de cidades")

def city_country(cidade, pais):
    print(f"{cidade.title()}, {pais.title()}")
    
city_country("santiago", "Chile")
city_country("Argentina", "Mexico")
city_country("Dinamarca", "peru")

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 8.7 Álbum
print("EXERCICIO 8.7 Álbum")

def make_album(nome, titulo_album, nFaixas=""):
    album = { "artista" : nome, "album_titulo": titulo_album}
    if nFaixas:
        album["numero_faixas"] = nFaixas
    
    
    return album

print(make_album("victor", "Apaixonado"))
print(make_album("victor", "voando", "3"))
print(make_album("victor", "Aprendendo python"))
print(make_album("victor", "Luxando","2"))
print(make_album("victor", "Sei la"))


print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 8.8 Álbuns dos usuários
print("EXERCICIO 8.8 Álbuns dos usuários")

ativo = True
while ativo:
    nArtista = input("Qual o nome do artista? \n Para sair digite q:  ")
    nAlbum = input("Qual o nome do album? \n Para sair digite q:  ")
    faixa = input("Se possui um numero de faixas informe, caso não tenha pressione enter \n Para sair digite q: ")
    
    if nArtista == "q":
        break
    elif nAlbum == "q":
        break
    elif faixa == "q":
            break

    make_album(nArtista,nAlbum,faixa)
    print(make_album(nArtista,nAlbum,faixa))
