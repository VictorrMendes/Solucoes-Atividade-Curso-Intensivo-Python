from collections import OrderedDict

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

# EXERCICIO 9.3 - Usuarios
print("EXERCICIO 9.3 - Usuarios")

class User():
    def __init__(self, first_name, last_name, age, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.pet = pet
        self.login_attempst = 0
        
    def describle_user(self):
        nome_completo = self.first_name + " " + self.last_name
        print(f"\nNome completo: {nome_completo.title()}")
        print(f"Idade: {str(self.age)}")
        print(f"Pet:{self.pet}\n")
        
    def greet_user(self):
        print(f"Olá {self.first_name.title()}, sejá bem vindo ao petshop")
        
    def read_login_user(self):
        print(str(self.login_attempst))
        
    def increment_login_attempts(self):
        self.login_attempst += 1    
        self.read_login_user()
        
    def reset_login_attempts(self):
        self.login_attempst = 0
        self.read_login_user()
    
        
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

usuario.read_login_user()
usuario.increment_login_attempts()
usuario.reset_login_attempts()
usuario.increment_login_attempts()
usuario.increment_login_attempts()
usuario.increment_login_attempts()
usuario.increment_login_attempts()
usuario.increment_login_attempts()
usuario.reset_login_attempts()

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 9.6 - Sorveteria
print("EXERCICIO 9.6 - Sorveteria")

class IceCreamStand(Restaurante):
    def __init__(self,restaurant_name, cuisile_type, estado,):
        super().__init__(restaurant_name, cuisile_type, estado)
        self.flavors = ["maracuja", "chocolate", "manga"]
        
    def show_flavors(self):
        for sabor in self.flavors:
            print(f"O restaurante {self.name} tem servetes de {sabor}")
            
sorveteria = IceCreamStand("Ice", "sorvetes", "aberto")

sorveteria.describle_restaurant()
sorveteria.open_restaurant()
sorveteria.show_flavors()

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 9.7 - Admin
print("EXERCICIO 9.7 - Admin")

class Admin(User):
    def __init__(self,first_name, last_name, age, pet):
        super().__init__(first_name, last_name, age, pet)
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
    def show_privileges(self):
        print(f"O {self.first_name} está como administrador e tem os seguintes privilegios:")
        
        for privilegio in self.privileges:
            print(f"- {privilegio}")
            
adm = Admin("Victor", "Mendes", "18", "gato")

adm.describle_user()
adm.show_privileges()

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 9.13-Reescrevendo o programa com OrdenedDict
print("EXERCICIO 9.13-Reescrevendo o programa com OrdenedDict")

glossario2 = OrderedDict()

glossario2["chapter_1"] = "numbers"
glossario2["chapter_2"] = "dicnames_casesionario"
glossario2["chapter_3"] = "list"
glossario2["chapter_4"] = "for"
glossario2["chapter_5"] = "if"
glossario2["chapter_6"] = "else"
glossario2["chapter_6_1"] = "dicionario"
glossario2["chapter_6_2"] = "items()"
glossario2["chapter_6_3"] = "key()"
glossario2["chapter_6_4"] = "value()"

for key, value in glossario2.items():
    print(f"Eu aprendi no {key} sobre: {value}\n")

print("\n----------------Fim do exercicio----------------\n")

# EXERCICIO 9.14 - Dados
print("EXERCICIO 9.14 - Dados")
from random import randint


class Die():
    def __init__(self,sides=6):
        self.sides = sides
        
    def roll_die(self):
        numero_aleatorio = randint(1, self.sides)
        print(f"O numero é {numero_aleatorio}")
            
luck_number = Die()

luck_number.roll_die()

print("\n----------------Fim do exercicio----------------\n")
