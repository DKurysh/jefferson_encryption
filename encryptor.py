from constants import CLEAR_ALPHABET, NUMBER_OF_DISCS


class Encryptor:

    def __init__(self):
        self.alphabet = CLEAR_ALPHABET
        self.n = NUMBER_OF_DISCS

    def change_let(self, let, step, alphabet, reverse):
        direction = -1 if reverse else 1
        return alphabet[(alphabet.find(let) + direction * step) % len(alphabet)]

    def jefferson_encryption(self, text, discs, step, reverse=False):
        text = ''.join([a for a in text if a.isalpha()]).upper()
        N = len(text) // self.n + 1  # количество проходов
        result = []

        for i in range(N):
            for j in range(self.n):
                y = i * self.n + j  # Номер буквы в тексте
                if y <= (len(text) - 1):
                    result.append(self.change_let(text[y], step, discs[j], reverse))

        return ''.join(result)
