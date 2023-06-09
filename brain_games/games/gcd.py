from random import randint
import prompt
import math


def gcd_game():
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')

    print(f'Hello, {name}!')

    print('Find the greatest common divisor of given numbers.')

    correct_answer = 0
    quastion_number = 0
    while quastion_number < 3:
        first_number = randint(1, 100)
        second_number = randint(1, 100)

        print(f'Question: {first_number} {second_number}')

        right_answer = math.gcd(first_number, second_number)

        user_answer = prompt.string('Your answer: ')
        if int(user_answer) == right_answer:
            print('Correct!')
            quastion_number += 1
            correct_answer += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'.\n"
                  f"Let's try again, {name}!")
            break
    if correct_answer == 3:
        print(f'Congratulations, {name}!')
