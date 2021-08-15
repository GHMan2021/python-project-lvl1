from random import randint
from ..check_answer import f_check_answer


def is_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    counter = 1
    result = True
    while result is True and counter <= 3:
        number = randint(0, 100)        
        print('Question: ', number)
        right_answer = 'yes' if f_is_prime(number) else 'no'
        user_answer = input('Your answer: ')

        if f_check_answer(right_answer, user_answer):
            counter += 1
        else:
            return False
    return True


def f_is_prime(number):
    if number % 2 == 0:
        return number == 2
    d = 3
    while d * d <= number and number % d != 0:
        d += 2
        return d * d > number
