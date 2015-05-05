import data
import unittest


class DataTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = data.DATA

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
