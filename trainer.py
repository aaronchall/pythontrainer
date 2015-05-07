#! /usr/bin/env python 
from __future__ import print_function, division

import collections
import data
import inspect
import random
import sys
import time
import re

if sys.version_info < (3, ):
    input = raw_input

MEMORY = collections.deque(maxlen=10)


def doc_quiz(quiz_type):
    list_of_names = list(data.DATA[quiz_type])
    while True:
        name = random.choice(list_of_names)
        if name in MEMORY:
            continue
        MEMORY.append(name)
        try:
            if quiz_type == 'modules':
                mod = __import__(name, globals(), locals())
                doc = inspect.getdoc(mod)
            elif quiz_type == 'keywords':
                doc = data.DATA['keywords'][name]
            elif quiz_type == 'datatypes':
                doc = data.DATA['datatypes'][name]
            else:
                doc = inspect.getdoc(eval(name))
            if doc is None:
                print('skipping {0} because no docs'.format(name))
                continue
            doc = smart_replace(doc, name)
            doc = smart_replace(doc, name.capitalize())

            # Handle the case of `list.extend` when the doc says `L.extend`
            #   then make it `L.*****`
            if '.' in name:
                _, _, last_part = name.partition('.')
                doc = smart_replace(doc, last_part)

            print('(Ctrl-C to quit)\n\nTo which name '
                  'does this documentation belong?:\n')
            inp = input(doc + '\n\n> ')
        except KeyboardInterrupt:
            return
        except Exception as error:
            print(error)
            raise
        time.sleep(.3)
        correct, answer = check_answer(quiz_type, inp, name)
        if correct:
            print('Very good.  Next!')
        else:
            print('No, it is ' + answer)
        time.sleep(.5)

def check_answer(quiz_type, inp, name):
    """Checks the input against the answer. Returns a tuple with first item
    being True/False for correct/wrong answer while second item is string
    containing correct answer
    When quiz_type=datatype, we format the answers to fit the * we
    replaced the answer with. E.g. for str.split, the question
    contained S.***** , logically, ***** will be the answer (i.e. split).
    """
    if quiz_type == 'datatypes':
        answer = name.split('.').pop()
    else:
        answer = name
    return (inp == answer, answer)


def smart_replace(string, name):
    """Looks for any spaces before and after the string we are trying to
    replace to avoid situations where "The string" is replaced with
    "The ***ring" for docstrign of str
    """
    pattern = re.compile(r'\b%s\b' % name)
    return pattern.sub('*' * len(name), string)


def main():
    try:
        while True:
            inp = input('\nWhat Python names would you like to study?: \n'
                        'Functions, Exceptions, Keywords, Datatypes, or '
                        'Modules? \n> ')
            if inp.lower() not in data.DATA:
                print('I did not understand that')
            else:
                doc_quiz(inp.lower())
    except (KeyboardInterrupt, EOFError):
        quit(0)

if __name__ == '__main__':
    main()
