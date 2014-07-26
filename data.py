from __future__ import print_function
import sys
import keyword
import string
import pkgutil
import pydoc_data.topics
import collections # Container or Sized
import numbers # Number
import inspect # getdoc

if not isinstance(__builtins__, dict):
    __builtins__ = vars(__builtins__)

data = {}
data['functions'] = dict((k, inspect.getdoc(v)) for k, v in __builtins__.items() 
                                    if k[0].islower() 
                                       and k not in ('copyright', 'credits'))

data['datatypes'] = dict(('{}.{}'.format(k,attr), inspect.getdoc(method)) #.__doc__) 
                           for k, v in __builtins__.items()
                             if isinstance(v, type) and 
                                issubclass(v, (collections.Sized, numbers.Number))
                             #if k[0].islower() and (hasattr(v, '__len__')
                              #                      or hasattr(v, '__bool__'))
                               for attr, method in vars(v).items()
                                 if attr[0].islower())
data['keywords'] = dict((k, pydoc_data.topics.topics[k])  for k in set(keyword.kwlist) & set(pydoc_data.topics.topics))

data['exceptions'] = dict((k,v) for k,v in __builtins__.items()
                          if k[0].isupper() 
                          and type(v) == type 
                          and issubclass(v, BaseException)
                         )
data['modules'] = [i[1] for i in pkgutil.iter_modules()
                            if i[1][0] != '_']

def main():
    import pprint
    pprint.pprint(data)
    
if __name__ == '__main__':
    main()
