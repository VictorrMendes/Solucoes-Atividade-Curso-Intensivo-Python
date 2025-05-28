
# EXERCÍCIO 3.4-Lista de convidados
convidados = ["Paloma","Linda", "Gisele"]
quantidade = len(convidados)

for convidado in convidados:
    print(f"Quero que compareça ao meu evendo {convidado}")


print("\n----------------Fim do exercicio----------------\n")



# EXERCÍCIO 3.5-Alternando a lista de convidados
naoComparece = "Linda"
print(naoComparece)

del convidados[1]
convidados.insert(1, "Elenice")

for convidado in convidados:
    print(f"Quero que compareça ao meu evendo {convidado}")

print("\n----------------Fim do exercicio----------------\n")



# EXERCÍCIO 3.6 Mais convidados

print(convidados)

convidados.insert(0,"Salem")
convidados.insert(1,"tigrezo")
convidados.append("Nagine")

for convidado in convidados:
    print(f"Venha para meu evento {convidado}")
    
print(convidados)

print("\n----------------Fim do exercicio----------------\n")



# EXERCÍCIO 3.7 Reduzindo a lista de convidados
print(convidados)
print("\nSó tenho dois convites")
nConvites = 2

while len(convidados) > nConvites:
    removidos = convidados.pop()
    print(f"\nDesculpe {removidos}, mas não poderar ir")
    
for convidado in convidados:
    print(f"\n {convidado} você esta convidado")
    
del convidados[0]
del convidados[0]
    
print(convidados)



print("\n----------------Fim do exercicio----------------\n")



# EXERCÍCIO 3.8 Conhecendo o mundo

placesDreams = ["irlanda","noruega","espanha","portugal","finlandia","alemanha"]

print(f"Lista original:{placesDreams}")



print("\nLista ordenada com sorted: ", sorted(placesDreams))
print("\nLista inversacom sorted(reverse=True): ", sorted(placesDreams, reverse=True))




placesDreams.sort()
print(f"\nLista com o sort(): {placesDreams}")

placesDreams.sort(reverse=True)
print(f"\nLista retornando ao original:{placesDreams}")


print("\n----------------Fim do exercicio----------------\n")

# EXERCÍCIO 3.9 Convidados para o jantar

convidados.append("Paloma")
convidados.append("Linda")
convidados.append("Gisele")

nParticipantes = len(convidados)
print(f"Serão {nParticipantes} convidados no total")

print("\n----------------Fim do exercicio----------------\n")


# EXERCÍCIO 3.10 Todas as funções




print("\n----------------Fim do exercicio----------------\n")