import unittest
import random10

class TestMain(unittest.TestCase):
	def setup(self):
		print('about to test a function')

	def test_inpt(self):
		guess = 5 
		answer = 5
		result = random10.run_guess(guess, answer)
		self.assertTrue(result)

	def test_wrong_guess(self):
		guess = 5 
		answer = 6
		result = random10.run_guess(guess, answer)
		self.assertFalse(result)

	def test_wrong_guess(self):
		guess = 5 
		answer = 6
		result = random10.run_guess(guess, answer)
		self.assertFalse(result)


	def tearDown(self):
		print('cleaning up')

if __name__ == "__main__":
	unittest.main()