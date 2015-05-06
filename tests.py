import data
import unittest

_MAX_LENGTH = 80


def safe_repr(obj, short=False):
    """
    Backport of unittest.util.safe_repr from python 2.7 for 2.6
    https://github.com/python/cpython/blob/cc14aa98797433709230c5522261b0e42d9fb284/Lib/unittest/util.py
    """
    try:
        result = repr(obj)
    except Exception:
        result = object.__repr__(obj)
        if not short or len(result) < _MAX_LENGTH:
            return result
        return result[:_MAX_LENGTH] + ' [truncated]...'


class DataTest(unittest.TestCase):
    data = data.DATA

    def assert_in(self, member, container, msg=None):
        """
        Just like self.assertTrue(a in b), but with a nicer default message.

        Backported from python 2.7 for python 2.6
        https://github.com/python/cpython/blob/cc14aa98797433709230c5522261b0e42d9fb284/Lib/unittest/case.py
        """
        if member not in container:
            standard_msg = '%s not found in %s' % (safe_repr(member),
                                                   safe_repr(container))
            self.fail(self._formatMessage(msg, standard_msg))

    def assert_is_instance(self, obj, cls, msg=None):
        """
        Same as self.assertTrue(isinstance(obj, cls)), with a nicer
        default message.

        backported from python 2.7 for python 2.6
        https://github.com/python/cpython/blob/cc14aa98797433709230c5522261b0e42d9fb284/Lib/unittest/case.py
        """
        if not isinstance(obj, cls):
            standard_msg = '%s is not an instance of %r' % (safe_repr(obj), cls)
            self.fail(self._formatMessage(msg, standard_msg))

    def test_data(self):
        self.assert_is_instance(self.data, dict)

    def test_data_keys(self):
        self.assert_in('keywords', self.data)
        self.assert_in('exceptions', self.data)
        self.assert_in('functions', self.data)
        self.assert_in('modules', self.data)
        self.assert_in('datatypes', self.data)

    def test_functions(self):
        funcs = self.data['functions']
        self.assert_in('min', funcs)
        self.assert_in('type', funcs)
        self.assert_in('enumerate', funcs)

    def test_keywords(self):
        kw = self.data['keywords']
        self.assert_in('with', kw)
        self.assert_in('if', kw)

    def test_modules(self):
        mods = self.data['modules']
        self.assert_in('os', mods)
        # self.assertIn('os.path', mods)
        self.assert_in('string', mods)

    def test_datatypes(self):
        datatypes = self.data['datatypes']
        # self.assertIn('str.maketrans', datatypes) # not in Python 2
        self.assert_in('str.lower', datatypes)

    def test_exceptions(self):
        exceptions = self.data['exceptions']
        self.assert_in('BaseException', exceptions)
        self.assert_in('OSError', exceptions)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
