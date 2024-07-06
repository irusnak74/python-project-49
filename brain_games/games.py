import prompt

from brain_games.randnum import generate_rand_num


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print(f'Hello {name}!')
    return name


if __name__ == '__main__':
    welcome_user()

    print(f'Answer "yes" if the number is even, otherwise answer "no".\nQuestion:')


generate_rand_num()
