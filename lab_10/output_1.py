class BasicCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

class AdvancedCalculator(BasicCalculator):
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

basic_calculator = BasicCalculator()
print("Addition: ", basic_calculator.add(5, 3))
print("Subtraction: ", basic_calculator.subtract(5, 3))

advanced_calculator = AdvancedCalculator()
print("Multiplication: ", advanced_calculator.multiply(5, 3))
print("Division: ", advanced_calculator.divide(5, 3))
