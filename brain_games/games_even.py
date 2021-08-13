from random import randint


def is_even(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 1
    result = True
    while result is True and counter <= 3:
        number = randint(0, 100)
        print('Question: ', number)

        right_answer = 'yes' if number % 2 == 0 else 'no'
        user_answer = input('Your answer: ')

        if right_answer == user_answer:
            print('Correct!')
            counter += 1
        else:
            r_a = right_answer
            u_a = user_answer
            print(f"'{u_a}' is wrong answer ;(. Correct answer was '{r_a}.'")
            print(f"Let's try again, {name}!")
            result = False

    if result is True:
        print(f'Congratulations, {name}!')
