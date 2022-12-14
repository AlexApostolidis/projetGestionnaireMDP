import unittest

import librairies
from loguin import *


class Unitest(unittest.TestCase):

    def test_wallet_init(self):
        self.assertRaises(ValueError, Wallet, None)
        self.assertRaises(ValueError, Wallet, "Hello")
        self.assertRaises(ValueError, Wallet, 1)

    def test_wallet_new_logs(self):
        wallet_test = Wallet([])
        password_obj = Password("my_password")
        username_obj = Username("my_username")
        website_obj = Website("my_website")
        self.assertRaises(ValueError, wallet_test.add_new_logs, "A", "B", "C")
        self.assertRaises(ValueError, wallet_test.add_new_logs, None, username_obj, password_obj)
        self.run(wallet_test.add_new_logs(website_obj, username_obj, password_obj))

    def test_wallet_edit_password(self):
        wallet_test_2 = Wallet([{"index": 1, "site": "qsdfdsqf", "id": "sqdfqsdf", "password": "ftv5{@4mH=&u8GB"}])
        password_obj = Password("my_password")
        self.assertRaises(ValueError, wallet_test_2.edit_site_password, "A", "B")
        self.assertRaises(ValueError, wallet_test_2.edit_site_password, 1, "B")
        self.assertRaises(ValueError, wallet_test_2.edit_site_password, None, password_obj)
        self.run(wallet_test_2.edit_site_password(1, password_obj))

    def test_wallet_delete(self):
        wallet_test_3 = Wallet([{"index": 1, "site": "qsdfdsqf", "id": "sqdfqsdf", "password": "ftv5{@4mH=&u8GB"}])
        self.assertRaises(ValueError, wallet_test_3.delete_site_password, None)
        self.assertRaises(ValueError, wallet_test_3.delete_site_password, "Crash")
        self.run(wallet_test_3.delete_site_password(0))
        password_obj = Password("my_password")
        username_obj = Username("my_username")
        website_obj = Website("my_website")
        wallet_test_3.add_new_logs(website_obj, username_obj, password_obj)
        self.assertRaises(ValueError, wallet_test_3.delete_site_password, 0.0)

    def test_wallet_save(self):
        self.assertRaises(ValueError, librairies.save_wallet, "Crash")
        self.assertRaises(ValueError, librairies.save_wallet, 1)
        self.run(librairies.save_wallet([{"index": 1,
                                          "site": "qsdfdsqf", "id": "sqdfqsdf", "password": "ftv5{@4mH=&u8GB"}]))

    def test_user_init(self):
        self.assertRaises(ValueError, User, "", None, "Hello")

    def test_user_write_name(self):
        self.assertRaises(ValueError, librairies.write_names, "", None, "Hello")


if __name__ == "__main__":
    unittest.main()
