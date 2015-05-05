# Python Trainer

This project is intended to use Python 2 or Python 3's internal documentation to
help people who use Python to learn it. It pulls from every category
of names in the Python language (except names in modules at the moment)
to quiz the user. The quiz shows the documentation with the name
obscured, and asks for the name. The name must be typed in with correct
spelling and capitalization to qualify as correct.

There are currently five classes of names:

* keywords: pulled from the `keyword` module and `pydo_data.topics`. 
* functions: builtin functions, essentially everything in `builtins` that
  starts with a lowercase letter (excluding `copyright` and `credits`)
* datatypes: perhaps a poor name. These are methods on the builtin objects.
  Not well tested either.
* exceptions: `builtin` names that are subclassing `BaseException`
* modules: every module listed in `pkgutil`. Maybe this is too much. 
  Maybe we should enumerate particular packages to try.

So, to add to this, we could add in the names inside modules, 
and we could try to inspect the operators that work on builtins 
and names in other modules.

## Usage:

If you have git, in theory, you're up and running with:

```
git clone https://github.com/aaronchall/pythontrainer
python pythontrainer
```

Ctrl-C (keyboard interrupt) to back out and exit. Please let me know if that doesn't work. Tweet at me at @aaronchall or @PythonNYC

## Constraints:

We want this package to be compatible with Python 2 and 3. 
Please no workarounds for Pythons below 2.4, though. This
is untested with 2.6, but I'd like to make sure it works for it.
So that means passing generator expressions to dict constructors 
instead of dict comprehensions, etc.

Also, we want this to work with a bare-bones install as much
as possible. So please no requirements that aren't in the 
standard library, (perhaps unless there's a fallback mechanism to standard 
library.)

Also, no custom object creation unless you can demonstrate the need for it
or the need is obvious. If needed, subclass object, and no metaclasses.

Follow PEP 8 and also read the Google Python style guide.

## TODO: 

* create a web ui that could be delivered with a local server
  perhaps with simplehttpserver?
* create a `tkinter` ui
* consider deleting modules loaded only for the docs from `sys.modules` to 
  better manage memory (if it is determined that it matters)
* add operators
* add names in modules (particularly `collections` and other 
  standard library datatypes)
* improve the documentation
* continue to improve style

Pull requests are welcome!

Cheers!
