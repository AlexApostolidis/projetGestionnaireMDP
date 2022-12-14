import unittest
import librairies


class Unittest(unittest.TestCase):

    def test_account_init(self):
        self.assertRaises(ValueError, librairies.Account, None)
        self.assertRaises(ValueError, librairies.Account, "")

    def test_verify_account(self):
        account = librairies.Account('password')
        self.assertRaises(ValueError, account.verify_account, None)
        self.assertRaises(ValueError, account.verify_account, "")

    def test_save_account(self):
        self.assertRaises(ValueError, librairies.save_account, None)
        self.assertRaises(ValueError, librairies.save_account, "")

    def test_username_init(self):
        self.assertRaises(ValueError, librairies.Username, None)
        self.assertRaises(ValueError, librairies.Username, "")

    def test_website_init(self):
        self.assertRaises(ValueError, librairies.Website, None)
        self.assertRaises(ValueError, librairies.Website, "")
