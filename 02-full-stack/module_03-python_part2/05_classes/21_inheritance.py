# INHERITANCE -> HERENCIA DE CLASES

# parent class
class User:
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def greeting(self):
        return f"Hi {self.first_name} {self.last_name}"


# child class -> 'User' is its parent
class AdminUser(User):
    def active_users(self):
        return '500'


tiffany = AdminUser("tiffany@devcamp.com", "Tiffany", "Hudgens")
kristine = User("kristine@devcamp.com", "Kristine", "Hudgens")

print(tiffany.active_users())           # 500
#print(kristine.active_users())         # AttributeError

print(tiffany.greeting())               # Hi Tiffany Hudgens
print(kristine.greeting())              # Hi Kristine Hudgens

"""
las clases hijas pueden acceder a los atributos y métodos de las clases madre,
pero no al revés

para crear una clase hija, si la clase madre tenía algún tipo de constructor,
necesitan los atributos del constructor para ser creadas
"""