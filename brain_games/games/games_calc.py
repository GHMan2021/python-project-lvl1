from random import randint, choice
from ..check_answer import f_check_answer


def result_expression():
    print('What is the result of the expression?')
    counter = 1
    while counter <= 3:
        number1 = randint(0, 25)
        number2 = randint(0, 25)
        operation_signs = choice('+-*')
        print('Question:', number1, operation_signs, number2)
        if operation_signs == '+':
            right_answer = str(number1 + number2)
        elif operation_signs == '-':
            right_answer = str(number1 - number2)
        else:
            right_answer = str(number1 * number2)
        user_answer = input('Your answer: ')

        if f_check_answer(right_answer, user_answer):
            counter += 1
        else:
            return False
    return True
