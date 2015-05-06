import data
import unittest
import sys


class BackportTestCase(unittest.TestCase):
    """
    Helper class to provide backport support for `assertIn` and `assertIsInstance`
    for python 2.6
    """
    MAX_LENGTH = 80

    def __init__(self, *args, **kwargs):
        super(BackportTestCase, self).__init__(*args, **kwargs)
        if sys.version_info < (2, 7):
            self.assertIn = self.assert_in
            self.assertIsInstance = self.assert_is_instance

    def safe_repr(self, obj, short=False):
        """
        Backport of unittest.util.safe_repr from python 2.7 for 2.6
        https://github.com/python/cpython/blob/cc14aa98797433709230c5522261b0e42d9fb284/Lib/unittest/util.py
        """
        try:
            result = repr(obj)
        except Exception:
            result = object.__repr__(obj)
            if not short or len(result) < self.MAX_LENGTH:
                return result
            return result[:self.MAX_LENGTH] + ' [truncated]...'

    def assert_in(self, member, container, msg=None):
        """
        Just like self.assertTrue(a in b), but with a nicer default message.

        Backported from python 2.7 for python 2.6
        https://github.com/python/cpython/blob/cc14aa98797433709230c5522261b0e42d9fb284/Lib/unittest/case.py
        """
        if member not in container:
            standard_msg = '%s not found in %s' % (self.safe_repr(member),
                                                   self.safe_repr(container))
            self.fail(self._formatMessage(msg, standard_msg))

    def assert_is_instance(self, obj, cls, msg=None):
        """
        Same as self.assertTrue(isinstance(obj, cls)), with a nicer
        default message.

        backported from python 2.7 for python 2.6
        https://github.com/python/cpython/blob/cc14aa98797433709230c5522261b0e42d9fb284/Lib/unittest/case.py
        """
        if not isinstance(obj, cls):
            standard_msg = '%s is not an instance of %r' % (self.safe_repr(obj), cls)
            self.fail(self._formatMessage(msg, standard_msg))


class DataTest(BackportTestCase):
    data = data.DATA

    def test_data(self):
        self.assertIsInstance(self.data, dict)

    def test_data_keys(self):
        self.assertIn('keywords', self.data)
        self.assertIn('exceptions', self.data)
        self.assertIn('functions', self.data)
        self.assertIn('modules', self.data)
        self.assertIn('datatypes', self.data)

    def test_functions(self):
        funcs = self.data['functions']
        self.assertIn('min', funcs)
        self.assertIn('type', funcs)
        self.assertIn('enumerate', funcs)

    def test_keywords(self):
        kw = self.data['keywords']
        self.assertIn('with', kw)
        self.assertIn('if', kw)

    def test_modules(self):
        mods = self.data['modules']
        self.assertIn('os', mods)
        # self.assertIn('os.path', mods)
        self.assertIn('string', mods)

    def test_datatypes(self):
        datatypes = self.data['datatypes']
        # self.assertIn('str.maketrans', datatypes) # not in Python 2
        self.assertIn('str.lower', datatypes)

    def test_exceptions(self):
        exceptions = self.data['exceptions']
        self.assertIn('BaseException', exceptions)
        self.assertIn('OSError', exceptions)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
