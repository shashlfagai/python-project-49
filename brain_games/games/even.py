from random import randint
import prompt


def even_number_game():
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')

    print('Hello, ' + name + '!')

    print('Answer "yes" if the number is even, otherwise answer "no".')

    question_number = 0
    correct_answers = 0
    while question_number < 3:
        random_number = randint(1, 1000)
        print('Question: ' + str(random_number))
        if random_number % 2 == 0:
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
