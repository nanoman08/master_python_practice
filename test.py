import unittest
import main

class TestMain(unittest.TestCase):
	def setup(self):
		print('avout to test a function')

	def test_do_stuff(self):
		test_param = 10
		result = main.do_stuff(test_param)
		self.assertEqual(result, 15)

	def test_do_stuff2(self):
		test_param = 'sh'
		result = main.do_stuff(test_param)
		self.assertTrue(isinstance(result, ValueError))

	def test_do_sfuf3(self):
		test_param = None
		result = main.do_stuff(test_param)
		self.assertEqual(result, "please enter number")

	def test_do_sfuf4(self):
		test_param = ''
		result = main.do_stuff(test_param)
		self.assertEqual(result, "please enter number")

	def test_do_stuff5(self):
		print('\n'+'6')

	def tearDown(self):
		print('cleaning up')

if __name__ == "__main__":
	unittest.main()