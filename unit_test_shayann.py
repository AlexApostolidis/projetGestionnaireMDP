import unittest
import librairies


class Unittest(unittest.TestCase):

    def test_account_init(self):
        password = "password"
        self.assertRaises(ValueError, librairies.Account, None)
        self.assertRaises(ValueError, librairies.Account, "")
        self.assertEqual(bool(librairies.Account(password)), True)

    def test_verify_account(self):
        account = librairies.Account('password')
        password = "password"
        password2 = "bonjour"
        self.assertRaises(ValueError, account.verify_account, None)
        self.assertRaises(ValueError, account.verify_account, "")
        self.assertEqual(bool(account.verify_account(password)), True)
        self.assertEqual(bool(account.verify_account(password2)), False)

    def test_save_account(self):
        self.assertRaises(ValueError, librairies.save_account, None)
        self.assertRaises(ValueError, librairies.save_account, "")

    def test_username_init(self):
        self.assertRaises(ValueError, librairies.Username, None)
        self.assertRaises(ValueError, librairies.Username, "")

    def test_website_init(self):
        self.assertRaises(ValueError, librairies.Website, None)
        self.assertRaises(ValueError, librairies.Website, "")

    def test_testing_password(self):
        password = librairies.Password("AZErtyg*¨//][12345")
        password2 = librairies.Password("zebi")
        self.assertRaises(ValueError, password.testing_password, None)
        self.assertRaises(ValueError, password.testing_password, "")
        self.assertEqual(password.testing_password(password.password), 1)
        self.assertEqual(password2.testing_password(password2.password), 0)
