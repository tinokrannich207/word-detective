"""A small terminal word game for the Codecademy CS 101 portfolio project."""

import random

WORDS = {
    "animals": [
        ("otter", "A playful mammal that swims in rivers and oceans."),
        ("falcon", "A fast bird of prey."),
        ("badger", "A burrowing mammal with a striped face."),
    ],
    "space": [
        ("comet", "A small icy object with a bright tail near the Sun."),
        ("nebula", "A huge cloud of gas and dust in space."),
        ("orbit", "The path one object follows around another in space."),
    ],
}

class WordRound:
    def __init__(self, category, word, hint, attempts=6):
        self.category = category
        self.word = word
        self.hint = hint
        self.attempts_left = attempts
        self.guessed_letters = set()

    def display_word(self):
        return " ".join(letter if letter in self.guessed_letters else "_" for letter in self.word)

    def guess(self, letter):
        if letter in self.guessed_letters:
            return "You already tried that letter."
        self.guessed_letters.add(letter)
        if letter not in self.word:
            self.attempts_left -= 1
            return "No match."
        return "Good guess!"

    def is_won(self):
        return all(letter in self.guessed_letters for letter in self.word)

    def __repr__(self):
        return f"WordRound(category={self.category!r}, attempts_left={self.attempts_left})"

class WordDetective:
    def __init__(self, player_name):
        self.player_name = player_name
        self.score = 0
        self.rounds_played = 0

    def play_round(self, category):
        word, hint = random.choice(WORDS[category])
        current_round = WordRound(category, word, hint)
        print(f"Category: {category.title()} | Hint: {hint}")
        while current_round.attempts_left > 0 and not current_round.is_won():
            print(f"Word: {current_round.display_word()} | Attempts left: {current_round.attempts_left}")
            letter = input("Guess one letter (or type 'hint' to see the clue again): ").strip().lower()
            if letter == "hint":
                print(current_round.hint)
                continue
            if len(letter) != 1 or not letter.isalpha():
                print("Enter one letter, please.")
                continue
            print(current_round.guess(letter))
        self.rounds_played += 1
        if current_round.is_won():
            self.score += current_round.attempts_left
            print(f"Solved! The word was {current_round.word!r}. You earned {current_round.attempts_left} points.")
            return True
        print(f"Out of attempts. The word was {current_round.word!r}.")
        return False

    def __repr__(self):
        return f"{self.player_name}: {self.score} points across {self.rounds_played} round(s)"

def choose_category():
    while True:
        choice = input("Choose a category (animals/space): ").strip().lower()
        if choice in WORDS:
            return choice
        print("Please choose animals or space.")

def main():
    print("=== Word Detective ===")
    name = input("What's your name? ").strip() or "Detective"
    player = WordDetective(name)
    print(f"Welcome, {player.player_name}! Solve words before your attempts run out.")
    while True:
        category = choose_category()
        player.play_round(category)
        print(f"Scoreboard: {player}")
        play_again = input("Play another round? (y/n): ").strip().lower()
        if play_again != "y":
            break
    print(f"Thanks for playing, {player.player_name}! Final score: {player.score}.")

if __name__ == "__main__":
    main()
