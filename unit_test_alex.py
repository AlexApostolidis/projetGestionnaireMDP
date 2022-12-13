import unittest
from loguin import *


class Unitest(unittest.TestCase):

    def test_wallet_init(self):
        self.assertRaises(ValueError, Wallet, None)
        self.assertRaises(ValueError, Wallet, "Hello")
        self.assertRaises(ValueError, Wallet, 1)

    def test_wallet_new_logs(self):
        wallet = Wallet([])
        wallet.add_new_logs("A", "B", "C")
        self.assertIn(wallet, {"index": 1, "site": "A", "id": "B", "password": "C"})
