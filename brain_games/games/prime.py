from random import randint
import prompt
import math


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def prime_game():
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')

    print(f'Hello, {name}!')

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    correct_answers = 0
    question_number = 0

    while question_number < 3:
        number = randint(1, 1000)
        print(f'Question: {number}')

        if is_prime(number):
            right_answer = 'yes'
        else:
            right_answer = 'no'

        user_answer = prompt.string('Your answer: ')
        if user_answer.lower() == right_answer:
            print('Correct!')
            question_number += 1
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'.\n"
                  f"Let's try again, {name}!")
            break
    if correct_answers == 3:
        print(f'Congratulations, {name}!')
