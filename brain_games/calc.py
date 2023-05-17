from random import randint, choice
import prompt


def calc_game():
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')

    print('Hello, ' + name + '!')

    print('What is the result of the expression?')

    correct_answer = 0
    quastion_number = 0
    while quastion_number < 3:
        first_number = randint(1, 100)
        second_number = randint(1, 100)
        operator = '+-*'
        randomasing_operator = choice(operator)
        print(f'Question: {first_number} {randomasing_operator} {second_number}')
        if randomasing_operator == '+':
            right_answer = first_number + second_number
        elif randomasing_operator == '-':
            right_answer = first_number - second_number
        else:
            right_answer = first_number * second_number
        user_answer = prompt.string('Your aswer: ')
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
