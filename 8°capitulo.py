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
