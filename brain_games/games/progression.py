from random import randint
import prompt


def progression():
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')

    print(f'Hello, {name}!')

    print('What number is missing in the progression?')

# обозначаем колличесвто вопросов
    correct_answer = 0
    quastion_number = 0
    while quastion_number < 3:
        first_number = randint(1, 50)
        step = randint(1, 10)

# создаем прогрессию
        progression = [first_number]
        for _ in range(10):
            next_value = progression[-1] + step
            progression.append(next_value)

# скрываем одину из цифр
        secret_number = randint(0, 9)
        right_answer = progression[secret_number]
        progression[secret_number] = '..'

        print('Question: ' + ' '.join(map(str, progression)))

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
