import unittest
import os
import requests

class FlaskTests(unittest.TestCase):

	def setUp(self):
		os.environ['NO_PROXY'] = '0.0.0.0'
		self.text = {
			'sentence': "I love you!",
		}
		pass
		
	def tearDown(self):
		pass
	
	
	def test_a_index(self):
		responce = requests.get('http://localhost:5000')
		self.assertEqual(responce.status_code, 200)
		
	def test_b_get_sentiment(self):
		
		params = {
			'sentence': self.text['sentence'],
			"form_type": "get_sentiment"
		}
		responce = requests.post('http://localhost:5000', data=params)
		self.assertEqual(responce.status_code, 200)
		self.assertEqual(responce.content, 'Positive'.encode())
		
		
if __name__ == '__main__':
	unittest.main()		




