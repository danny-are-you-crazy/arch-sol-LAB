import random

class RockPaperScissors:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0

    def play_game(self):
        while True:
            user_choice = self.get_user_choice()
            if user_choice == 'вихід':
                self.end_game()
                break

            computer_choice = self.get_computer_choice()
            print(f"Комп'ютер показав: {computer_choice}")

            self.determine_winner(user_choice, computer_choice)

    def get_user_choice(self):
        return input("Напишіть ваш вибір (камінь, ножиці, папір) або напишіть 'вихід' щоб вийти: ").lower()

    def get_computer_choice(self):
        return random.choice(['камінь', 'ножиці', 'папір'])

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            print("=====Нічия!=====")
        elif (user_choice == 'камінь' and computer_choice == 'ножиці') or \
             (user_choice == 'папір' and computer_choice == 'камінь') or \
             (user_choice == 'ножиці' and computer_choice == 'папір'):
            print("=====Ти виграв!=====")
            self.player_score += 1
        else:
            print("=====Комп'ютер виграв...=====")
            self.computer_score += 1

    def end_game(self):
        print("Гра закінчена!")
        print("Результат:")
        print(f"Гравець: {self.player_score}")
        print(f"Комп'ютер: {self.computer_score}")

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()
