import unittest

import aos_methods as methods


class AosAppPositiveTestCases(unittest.TestCase):  # create class

    @staticmethod  # signal to unittest that this is a static method
    def test_create_aos():
        methods.setUp()
        methods.create_user()
        methods.logout()
        methods.login()
        methods.logout()
        methods.tearDown()


if __name__ == "__main__":
    unittest.main()
