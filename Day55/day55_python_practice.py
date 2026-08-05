"""
🐍 Day 55: Unit Testing — unittest module
"""

import unittest

# ----------------------------------------------------
# 1. Why test your code?
# ----------------------------------------------------
# Instead of manually checking "does this work?" every time,
# you write TESTS that automatically verify your code behaves
# correctly — and catch bugs BEFORE they reach production.


# ----------------------------------------------------
# 2. The code we want to test
# ----------------------------------------------------

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def is_even(n):
    return n % 2 == 0

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive!")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds!")
        self.balance -= amount
        return self.balance


# ----------------------------------------------------
# 3. Writing tests -> a class that inherits from unittest.TestCase
# ----------------------------------------------------

class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(1, 3), 0.333, places=3)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):    # expects an error to be raised
            divide(10, 0)

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(7))


# ----------------------------------------------------
# 4. Using setUp() to prepare fresh data before EACH test
# ----------------------------------------------------

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        # runs automatically before every single test method
        self.account = BankAccount(balance=100)

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 100)

    def test_deposit(self):
        new_balance = self.account.deposit(50)
        self.assertEqual(new_balance, 150)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

    def test_withdraw(self):
        new_balance = self.account.withdraw(40)
        self.assertEqual(new_balance, 60)

    def test_withdraw_too_much(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(1000)

    def tearDown(self):
        # runs automatically after every single test method (cleanup)
        del self.account


# ----------------------------------------------------
# 5. Common assertion methods (cheat sheet)
# ----------------------------------------------------
# assertEqual(a, b)        -> a == b
# assertNotEqual(a, b)     -> a != b
# assertTrue(x)            -> bool(x) is True
# assertFalse(x)           -> bool(x) is False
# assertIsNone(x)          -> x is None
# assertIn(a, b)           -> a is in b
# assertRaises(Error)      -> code inside raises the given error
# assertAlmostEqual(a, b)  -> a ≈ b (useful for floats)


# ----------------------------------------------------
# 6. Running the tests
# ----------------------------------------------------
# Normally you'd run this file with:  python -m unittest test_file.py
# Here we run it manually so it works inside this script too.

print("--- Running all tests ---\n")
loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTests(loader.loadTestsFromTestCase(TestMathFunctions))
suite.addTests(loader.loadTestsFromTestCase(TestBankAccount))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)


"""
📝 Quick Recap:
- import unittest
- class TestSomething(unittest.TestCase):  -> groups related tests
- Each test method name MUST start with 'test_'
- setUp()    -> runs before EVERY test (fresh setup)
- tearDown() -> runs after EVERY test (cleanup)
- self.assertEqual(), assertTrue(), assertRaises(), etc. -> check results
- Run tests from terminal with: python -m unittest filename.py
- Automated tests catch bugs early and make refactoring safer
"""