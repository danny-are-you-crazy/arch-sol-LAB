class User:
    def __init__(self, name, age, gender, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
    
    def is_adult(self):
        return self.age >= 18

def calculate_score(user, scores):
    total_score = sum(scores)
    
    print("Name:", user.name)
    print("Age:", user.age)
    print("Gender:", user.gender)
    print("Height:", user.height)
    print("Weight:", user.weight)
    print("Total Score:", total_score)
    print("Adult:", user.is_adult())

#Приклад визову функції
john = User("John", 25, "Male", 175, 70)
scores = [85, 90, 75, 88, 92]
calculate_score(john, scores)
