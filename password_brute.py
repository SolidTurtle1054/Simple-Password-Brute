import random
import string
import itertools
import time

Password = []
Length = 4 #Password length

def generatePassword(Length = Length, Letters = string.ascii_uppercase + string.digits):
    global Password
    Password = ''.join(random.choice(Letters) for _ in range(Length))
    print('Password:', Password)
    time.sleep(2)

def bruteCracker(Length = Length + 1, Letters = string.ascii_uppercase + string.digits):
    Attempts = 0
    Guess = []
    for password_Lenght in range(1, Length):
        for Guess in itertools.product(Letters, repeat=password_Lenght):
            Attempts += 1
            Guess = ''.join(Guess)
            print(Guess, Attempts)
            if Guess == Password:
                print('Guess:', Guess, ', Num of Attempts', Attempts)
                quit()
            
generatePassword()
bruteCracker()