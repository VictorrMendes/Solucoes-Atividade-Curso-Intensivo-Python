# EXERCICIO 9.1-Restaurante
print("EXERCICIO 9.1-Restaurante")

class Restaurante():
    def __init__(self,restaurant_name, cuisile_type, estado):
        self.name = restaurant_name
        self.type = cuisile_type
        self.estado = estado
        self.number_served = 0
        
    def describle_restaurant(self):
        print(f"O restaurante {self.name.title()}, é do tipo {self.type}")
    
    def open_restaurant(self):
        print(f"O restaurante {self.name.title()} se encontra {self.estado}")
    
    def served_read(self):
        print(f"O numero de pessoas servidas no restaurante {self.name} é de " + str(self.number_served))
        
    def set_number_served(self, number):
        self.number_served = number
        self.served_read()
        
    def increment_number_served(self,set_number):
        self.number_served += set_number
        self.served_read()
        
restaurante_1 = Restaurante("polegar","rustico","aberto")
restaurante_2 = Restaurante("abacaxi","asiatico","fechado")


restaurante_1.describle_restaurant()
restaurante_1.open_restaurant()

restaurante_2.describle_restaurant()
restaurante_2.open_restaurant()

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 9.2 - Trez restaurantes
print("EXERCICIO 9.2 - Trez restaurantes")

restaurante_1 = Restaurante("polegar","rustico","aberto")
restaurante_2 = Restaurante("abacaxi","asiatico","fechado")
restaurante_3 = Restaurante("frango","brasileiro","fechado")
restaurante_4 = Restaurante("são longuinho", "mitico", "aberto")

restaurante_1.describle_restaurant()
restaurante_2.describle_restaurant()
restaurante_3.describle_restaurant()
restaurante_4.describle_restaurant()

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 9.2 - Usuarios
print("EXERCICIO 9.2 - Usuarios")

class User():
    def __init__(self, first_name, last_name, age, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.pet = pet
        
    def describle_user(self):
        nome_completo = self.first_name + " " + self.last_name
        print(f"\nNome completo: {nome_completo.title()}")
        print(f"Idade: {str(self.age)}")
        print(f"Pet:{self.pet}\n")
        
    def greet_user(self):
        print(f"Olá {self.first_name.title()}, sejá bem vindo ao petshop")
        
usuario = User("victor", "mendes", "20", "gato")

usuario.greet_user()
usuario.describle_user()

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 9.4- Pessoas atendidas
print("EXERCICIO 9.4- Pessoas atendidas")

restaurante_1.served_read()

restaurante_2.served_read()
restaurante_2.set_number_served(4)

restaurante_3.served_read()
restaurante_3.increment_number_served(2)
restaurante_3.increment_number_served(60)

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 9.5 Tentativas de login
print("EXERCICIO 9.5 Tentativas de login")

