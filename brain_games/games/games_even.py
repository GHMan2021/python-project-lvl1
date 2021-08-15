from random import randint
from ..check_answer import f_check_answer


def is_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 1
    result = True
    while result is True and counter <= 3:
        number = randint(0, 100)
        print('Question:', number)

        right_answer = 'yes' if number % 2 == 0 else 'no'
        user_answer = input('Your answer: ')

        if f_check_answer(right_answer, user_answer):
            counter += 1
        else:
            return False
    return True
