from random import randint
from ..check_answer import f_check_answer


def is_gcd():
    print('Find the greatest common divisor of given numbers.')
    counter = 1
    while counter <= 3:
        number1 = randint(0, 25)
        number2 = randint(0, 25)
        print('Question:', number1, number2)
        user_answer = str(input('Your answer: '))
        right_answer = str(gcd(number1, number2))

        if f_check_answer(right_answer, user_answer):
            counter += 1
        else:
            return False
    return True


def gcd(number1, number2):
    while number1 != number2:
        if number1 > number2:
            number1 = number1 - number2
        else:
            number2 = number2 - number1
    return number1
