
class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def get_address(self):
        return self.address


class ShippingCalculator:
    def calculate_cost(self, address):
        if "New York" in address:
            return 5.00
        elif "California" in address:
            return 10.00
        else:
            return 15.00


class Order:
    def __init__(self, customer, product, quantity):
        self.customer = customer
        self.product = product
        self.quantity = quantity

    def print_order_details(self):
        print(f"Order for {self.product} x {self.quantity}")
        print(f"Shipping to {self.customer.get_address()}")

    def calculate_shipping_cost(self):
        shipping_calculator = ShippingCalculator()
        return shipping_calculator.calculate_cost(self.customer.get_address())
