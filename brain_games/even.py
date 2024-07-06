from brain_games.randnum import generate_rand_num


def is_even(num):
    return num % 2 == 0


def get_num_and_even_answer():
    num = generate_rand_num()
    correct_answer = 'yes' if is_even(num) else 'no'
    return num, correct_answer
