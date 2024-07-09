import prompt

from brain_games.even import get_num_and_even_answer


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print(f'Hello {name}!')
    return name


if __name__ == '__main__':
    welcome_user()

    print(f'Answer "yes" if the number is even, otherwise answer "no".\nQuestion:')


if __name__ == '__main__':
    get_num_and_even_answer()
