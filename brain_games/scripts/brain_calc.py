#!/usr/bin/env python
from brain_games import user_name, games_calc


def main():
    print('Welcome to the Brain Games!')
    name = user_name.welcome_user()
    games_calc.result_expression(name)


if __name__ == '__main__':
    main()
