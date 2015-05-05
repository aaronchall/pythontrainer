from __future__ import print_function, division
import data
import sys
import random
import time
import collections
import inspect

if sys.version_info.major < 3:
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
            else:
                doc = inspect.getdoc(eval(name))
            if doc is None:
                print('skipping {0} because no docs'.format(name))
                continue
            hidden_name = '*' * len(name)
            doc = doc.replace(name, hidden_name)
            doc = doc.replace(name.capitalize(), hidden_name)
            print('(Ctrl-C to quit)\n\nTo which name '
                  'does this documentation belong?:\n')
            inp = input(doc + '\n\n> ')
        except KeyboardInterrupt:
            return
        except Exception as error:
            print(error)
            raise
        time.sleep(.3)
        if inp == name:
             print('Very good.  Next!')
        else:
             print('No, it is ' + name)
        time.sleep(.5)

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
