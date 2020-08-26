import random


class PasswordGenerator:
    letters_alphabet = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    digits_alphabet = '123456789'
    symbols_alphabet = '!"№;%:?*()_+-=\/.'

    def __init__(self, length=16, use_letters=True, use_digits=True, use_symbols=False):
        self.length = length
        self.use_letters = use_letters
        self.use_digits = use_digits
        self.use_symbols = use_symbols
        print(length, use_letters, use_digits, use_symbols)

    def generate_password(self):
        alphabet = ''
        if self.use_letters:
            alphabet += self.letters_alphabet
        if self.use_digits:
            alphabet += self.digits_alphabet
        if self.use_symbols:
            alphabet += self.symbols_alphabet
        if not alphabet:
            print('empty alphabet')
            return

        password = ''
        for i in range(self.length):
            password += random.choice(alphabet)
        return password
