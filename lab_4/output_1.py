class Animal:
    def speak(self):
        pass

    def move(self):
        pass


class Dog():
    animal = Animal()

    def speak(self):
        return self.animal.speak()

    def move(self):
        return self.animal.move()


def main():
    dog = Dog()
    dog.speak()
    dog.move()


if __name__ == '__main__':
    main()
