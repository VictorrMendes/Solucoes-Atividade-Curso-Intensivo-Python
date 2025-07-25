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

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 8.9 – Mágicos
print("EXERCICIO 8.9 – Mágicos")


magicos = ["Salem","Nagine","Tigrezo"]

def show_magicans(mago):
    for magico in mago:
        print(f"O {magico} é um magico")
        
show_magicans(magicos)

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 8.10 grandes magicos
print("EXERCICIO 8.10 grandes magicos")



def make_great(magicos, master_magic):
    for mago in magicos:
        grande = "O grande " + mago
        master_magic.append(grande)
    
master_magic = []

make_great(magicos, master_magic)

for mago in master_magic:
    print(mago)
    
    
print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 8.11- Magicos inaltedados
print("EXERCICIO 8.11- Magicos inaltedados")

magos = ["Salem","Nagine","Tigrezo"]

def make_great(magos, master_magos):
    
    while magos:
        corrent_mago = magos.pop()
    
        alteracao = "O grande " + corrent_mago
        master_magos.append(alteracao)
    
master_magos = []



make_great(magos[:], master_magos)

print(magos)

print(master_magos)


for mago in master_magos:
    print(mago)


print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 8.12 - Sanduiches
print("EXERCICIO 8.12 - Sanduiches")

def sandwich(*acrescimos):
    print("\n O seu sanduiche vai ter: \n")
    for item in acrescimos:
        print(f" - {item}")

    
sandwich("batata","tomate","uva")
sandwich("alface","gergilin","couve flor")
sandwich("oregano")

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 8.13 - perfil usuario
print("EXERCICIO 8.13 - perfil usuario")

def build_profile(first, last, **infoUser):
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    
    for key, value in infoUser.items():
        profile[key] = value
    return profile

user_profile = build_profile("victor","mendes",location="casa",idade="50")

print(user_profile)

