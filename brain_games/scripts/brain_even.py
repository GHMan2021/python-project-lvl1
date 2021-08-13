#!/usr/bin/env python
from brain_games import user_name, games_even


def main():
    print('Welcome to the Brain Games!')
    name = user_name.welcome_user()
    games_even.is_even(name)


if __name__ == '__main__':
    main()
