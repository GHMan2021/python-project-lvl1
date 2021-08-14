#!/usr/bin/env python
from brain_games import user_name
from ..games.games_gcd import is_gcd


def main():
    print('Welcome to the Brain Games!')
    name = user_name.welcome_user()
    if is_gcd():
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()
