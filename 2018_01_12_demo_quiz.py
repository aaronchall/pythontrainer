from __future__ import print_function
import random

def main():
    difficulty_level = get_difficulty()
    run_quiz(difficulty_level)

def get_difficulty():
    """ask the user for what difficulty level
    return easy, medium, or hard
    """
    print("Welcome to the program")
    while True:
        print("Please give the difficulty level")
        print("easy, medium, or hard")
        user_input = raw_input('> ')
        if user_input in QUESTIONS:
            break
        else:
            print('I did not understand, try again')
    return user_input

def run_quiz(difficulty_level):
    """given 'easy', 'medium', or 'hard',
    quiz the user
    """
    questions_dict = QUESTIONS[difficulty_level]
    counter = {'wrong': 0, 'right': 0}
    while True:
        question = pick_a_random_question(questions_dict)
        users_answer = ask(question)
        if users_answer == 'quit':
            break
        if questions_dict[question] == users_answer:
            counter['right'] += 1
            print('right')
        else:
            counter['wrong'] += 1
            print('wrong')
    print('results:')
    print(counter)

QUESTIONS = {
    'easy': {
        'a cat says': 'meow',
        "a dog says": 'woof',
    },
    'medium': {
        "a cat says": 'meow',
        "a dog says": 'woof',
    },
    'hard': {
        "cat species": 'feline',
        "dog species": 'canine',
    },
}

def pick_a_random_question(questions_dict):
    keys = list(questions_dict)
    question = random.choice(keys)
    return question

def ask(question):
    print(question)
    answer = raw_input('> ')
    return answer

# if this module is the entry point for a python program
if __name__ == '__main__':
    main()
