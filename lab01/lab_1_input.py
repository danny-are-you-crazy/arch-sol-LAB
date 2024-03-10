#Довгий метод
import random

class RockPaperScissors:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0

    def play_game(self):
        while True:
            user_choice = input("Напишіть ваш вибір (камінь, ножиці, папір) або напишіть 'вихід' щоб вийти: ").lower()
            if user_choice == 'вихід':
                print("Гра закінчена!")
                print("Результат:")
                print(f"Гравець: {self.player_score}")
                print(f"Комп'ютер: {self.computer_score}")
                break

            #Комп'ютер рандомно обирає предмет
            computer_choice = random.choice(['камінь', 'ножиці', 'папір'])
            print(f"Комп'ютер показав: {computer_choice}")

            #Якщо вибір гравця співпадає з комп'ютером
            if user_choice == computer_choice:
                print("=====Нічия!=====")
            #Якщо вибір гравця краще (по правилам) ніж у комп'ютера
            elif (user_choice == 'камінь' and computer_choice == 'ножиці') or \
                 (user_choice == 'папір' and computer_choice == 'камінь') or \
                 (user_choice == 'ножиці' and computer_choice == 'папір'):
                print("=====Ти виграв!=====")
                self.player_score += 1
            else:
            #Якщо вибір гравця хуже комп'ютером
                print("=====Комп'ютер виграв...=====")
                self.computer_score += 1

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()
