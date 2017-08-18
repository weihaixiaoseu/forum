import unittest
from forum import create_app

class BasicsTestCase(unittest.TestCase):
	def setUp(self):
		self.app = create_app('testing')
		# self.app_context = self.app.app_context()
		# self.app_context.push()
		# self.app_request_context = self.app.test_request_context()
		# self.app_request_context.push() 

	# def tearDown(self):
		# self.app_context.pop()
		# self.app_request_context.pop() 

	def test_getIndex(self):
		tester = self.app.test_client()
		response = tester.get('/')
		self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()

