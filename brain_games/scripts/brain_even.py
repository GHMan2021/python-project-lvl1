#!/usr/bin/env python
from brain_games import user_name
from ..games.games_even import is_even


def main():
    print('Welcome to the Brain Games!')
    name = user_name.welcome_user()
    if is_even():
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()
