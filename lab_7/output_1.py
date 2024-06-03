class Product:
    def __init__(self, product_id, name, category, price):
        self.__product_id = product_id
        self.__name = name
        self.__category = category
        self.__price = price

    @property
    def product_id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        self.__category = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value
        else:
            raise ValueError("Price cannot be negative")

class InventoryManagement:
    def __init__(self, products):
        self.__products = products

    def print_product_details(self, product_id):
        for product in self.__products:
            if product.product_id == product_id:
                print(f"Product ID: {product.product_id}, Name: {product.name}, Category: {product.category}, Price: {product.price}")

# Приклад використання
product1 = Product(1, "Laptop", "Electronics", 1500)
product2 = Product(2, "Smartphone", "Electronics", 800)

inventory = InventoryManagement([product1, product2])
inventory.print_product_details(1)
