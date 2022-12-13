import unittest
from loguin import *


class Unitest(unittest.TestCase):

    def test_account_class(self):
        self.assertRaises(ValueError, Account, None)
        self.assertRaises(ValueError, Account, "")
        self.assertRaises(ValueError, save_account, "")
        self.assertRaises(ValueError, save_account, None)

    def test_password_class(self):
        self.assertRaises(ValueError, Password, "")
        self.assertRaises(ValueError, Password, None)
        self.assertRaises(ValueError, Password.testing_password, None)
        self.assertRaises(ValueError, Password.testing_password, "")

    def test_user_class(self):
        self.assertRaises(ValueError, User, "", "a", "a")
        self.assertRaises(ValueError, User, None, "a", "a")
        self.assertRaises(ValueError, User, "a", "", "a")
        self.assertRaises(ValueError, User, "a", None, "a")
        self.assertRaises(ValueError, User, "a", "a", "")
        self.assertRaises(ValueError, User, "a", "a", None)
        self.assertRaises(ValueError, write_names, "", "b", "b")
        self.assertRaises(ValueError, write_names, None, "b", "b")
        self.assertRaises(ValueError, write_names, "b", "", "b")
        self.assertRaises(ValueError, write_names, "b", None, "b")
        self.assertRaises(ValueError, write_names, "b", "b", "")
        self.assertRaises(ValueError, write_names, "b", "b", None)

    def test_username_class(self):
        self.assertRaises(ValueError, Username, "")
        self.assertRaises(ValueError, Username, None)

    def test_wallet_class(self):
        self.assertRaises(ValueError, Wallet, "qdsf")
        self.assertRaises(ValueError, Wallet, None)
        self.assertRaises(ValueError, Wallet, 1)
        self.assertRaises(ValueError, Wallet, 1.0)
        new_wallet = Wallet([])
        self.assertRaises(ValueError, new_wallet.add_new_logs, "a", "", "a")
        self.assertRaises(ValueError, new_wallet.add_new_logs, None, "", "")
        self.assertRaises(ValueError, new_wallet.edit_site_password, None, "my_new_password")
        self.assertRaises(ValueError, new_wallet.edit_site_password, "qdf", "my_new_password")
        self.assertRaises(ValueError, new_wallet.edit_site_password, 1, "")
        self.assertRaises(ValueError, new_wallet.edit_site_password, 1, None)
        self.assertRaises(ValueError, new_wallet.delete_site_password, "qds")
        self.assertRaises(ValueError, new_wallet.delete_site_password, None)

    def test_website_class(self):
        self.assertRaises(ValueError, Website, "")
        self.assertRaises(ValueError, Website, None)
