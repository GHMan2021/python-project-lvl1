#!/usr/bin/env python
from brain_games import user_name
from ..games.games_prime import is_prime


def main():
    print('Welcome to the Brain Games!')
    name = user_name.welcome_user()
    if is_prime():
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()
