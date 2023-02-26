# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
    def __init__(self, word):
        self.word = word
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.guessed_characters_index = []
        self.enumerated_characters = list(enumerate(self.word))

    def guess(self, char):
        if self.get_status() == 'lose' or len(self.word) == len(self.guessed_characters_index):
            raise ValueError('The game has already ended.')
        if char not in self.word:
            self.remaining_guesses -= 1
        else:
            for index, character in self.enumerated_characters:
                if character == char:
                    if index in self.guessed_characters_index:
                        self.remaining_guesses -= 1
                        break
                    self.guessed_characters_index.append(index)

    def get_masked_word(self):
        masked_word = ''
        for index, character in self.enumerated_characters:
            if index in self.guessed_characters_index:
                masked_word += character
            else:
                masked_word += '_'
        return masked_word

    def get_status(self):
        if len(self.word) == len(self.guessed_characters_index):
            return 'win'
        if self.remaining_guesses < 0:
            return 'lose'
        return 'ongoing'
