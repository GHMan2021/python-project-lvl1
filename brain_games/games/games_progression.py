from random import randint
from ..check_answer import f_check_answer


def is_progression():
    print('What number is missing in the progression?')
    counter = 1
    while counter <= 3:
        start_number = randint(0, 100)
        num_progress = randint(1, 10)
        x_number = randint(1, 10)
        counter_1 = 1
        result = ''
        while counter_1 <= 10:
            if counter_1 == x_number:
                start_number += num_progress
                right_answer = str(start_number)
                result += '..' + ' '
                counter_1 += 1
            else:
                start_number += num_progress
                result += str(start_number) + ' '
                counter_1 += 1
        print('Question: ', result)
        user_answer = str(input('Your answer: '))
        if f_check_answer(right_answer, user_answer):
            counter += 1
        else:
            return False
    return True
