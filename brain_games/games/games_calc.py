from random import randint, choice


def result_expression(name):
    print('What is the result of the expression?')
    counter = 1
    result = True
    while result is True and counter <= 3:
        number1 = randint(0, 25)
        number2 = randint(0, 25)
        operation_signs = choice('+-*')
        print('Question: ', number1, operation_signs, number2)
        if operation_signs == '+':
            right_answer = str(number1 + number2)
        elif operation_signs == '-':
            right_answer = str(number1 - number2)
        else:
            right_answer = str(number1 * number2)
        user_answer = input('Your answer: ')

        if right_answer == user_answer:
            print('Correct!')
            counter += 1
        else:
            r_a = right_answer
            u_a = user_answer
            print(f"'{u_a}' is wrong answer ;(. Correct answer was '{r_a}'.")
            print(f"Let's try again, {name}!")
            result = False

    if result is True:
        print(f'Congratulations, {name}!')
