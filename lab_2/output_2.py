class UserType:
    ENGINEER = "Engineer"
    MANAGER = "Manager"

class PhoneNumber:
    def __init__(self, number, code):
        self.number = number
        self.code = code

    def full_number(self):
        return self.code + self.number

class User:
    def __init__(self, name, age, user_type, phone_number):
        self.name = name
        self.age = age
        self.user_type = user_type
        self.phone_number = phone_number

    def print_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Type:", self.user_type)
        print("Phone:", self.phone_number.full_number())

# Приклад використання класу
phone = PhoneNumber("9379992", "050")
user = User("John", 25, UserType.ENGINEER, phone)
user.print_details()
