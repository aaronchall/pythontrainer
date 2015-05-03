from __future__ import print_function
import data
import sys
import random
import time
import collections

if sys.version_info < (3,):
    input = raw_input

memory = collections.deque(maxlen=10)

def doc_quiz(quiz_type):
    while True:
        fn = random.choice(list(data.data[quiz_type]))
        if fn in memory:
            continue
        memory.append(fn)
        try:
            inp = input('\nTo which function does this documentation belong?\n\n' +
              eval(fn).__doc__.replace(fn, 'foo').replace(fn.capitalize(), 'Foo') + '\n\n> ')
        except Exception as e:
            print(e)
            raise
        time.sleep(.3)
        if inp == fn:
             print('Very good.  Next!')
        else:
             print('No, it is ' + fn)
        time.sleep(.5)

def main():
    try:
        while True:
            inp = input('What core Python would you like to focus on today?: \n'
                        'Functions, Exceptions, Keywords, Datatypes, or Modules? \n> ').lower()
            if inp not in ['functions', 'exceptions', 'keywords', 'modules', 'datatypes']:
                print('I did not understand that')
            else:
                # doc_quiz(inp.rstrip('s'))
                doc_quiz(inp)

    except (KeyboardInterrupt, EOFError):
        quit(0)

if __name__ == '__main__':
    main()
