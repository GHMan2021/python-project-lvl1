def f_check_answer(right_answer, user_answer):
    if right_answer == user_answer:
        print('Correct!')
        return True
    else:
        u_a = user_answer
        r_a = right_answer
        print(f"'{u_a}' is wrong answer ;(. Correct answer was '{r_a}'.")
        return False
