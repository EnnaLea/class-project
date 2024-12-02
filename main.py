class User:

    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear


    def get_name(self):
        return self.name.upper()


    def age(self, current_year):
        age = current_year - self.birthyear
        return age


user1 = User("john", 1999)
user_age = user1.age(2024)
user_name = user1.get_name()
print(user_age)
print(user_name)