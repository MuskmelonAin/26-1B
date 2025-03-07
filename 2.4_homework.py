import random

class GuessNumberGame:
    def __init__(self, min_value=1, max_value=100):
        self.min_value = min_value
        self.max_value = max_value
        self.secret_number = random.randint(self.min_value, self.max_value)
        self.attempts = 0
        self.is_running = True

    def make_guess(self, guess):
        self.attempts += 1
        if guess < self.secret_number:
            return "Загаданное число больше."
        elif guess > self.secret_number:
            return "Загаданное число меньше."
        else:
            self.is_running = False
            return f"Поздравляю! Вы угадали число {self.secret_number} за {self.attempts} попыток."

    def play(self):
        print(f"Добро пожаловать в игру 'Угадай число'! Угадайте число от {self.min_value} до {self.max_value}.")
        while self.is_running:
            try:
                guess = int(input("Введите число: "))
                print(self.make_guess(guess))
            except ValueError:
                print("Пожалуйста, введите целое число.")


if __name__ == "__main__":
    game = GuessNumberGame(1, 100)  
    game.play()
