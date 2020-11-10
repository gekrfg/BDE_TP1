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
			'sentence': 'I love Big Data Engineering!',
			"form_type": "get_sentiment"
		}
		responce = requests.post('http://localhost:5000', data=params)
		self.assertEqual(responce.status_code, 200)
		self.assertEqual(responce.text[333]+responce.text[334]+responce.text[335], 'Pos')

	
	def test_c_get_sentiment(self):
		
		params = {
			'sentence': 'I hate smurf!',
			"form_type": "get_sentiment"
		}
		responce = requests.post('http://localhost:5000', data=params)
		self.assertEqual(responce.status_code, 200)
		self.assertEqual(responce.text[333]+responce.text[334]+responce.text[335], 'Neg')


	def test_d_get_sentiment(self):
		
		params = {
			'sentence': 'May the force be with you.',
			"form_type": "get_sentiment"
		}
		responce = requests.post('http://localhost:5000', data=params)
		self.assertEqual(responce.status_code, 200)
		self.assertEqual(responce.text[333]+responce.text[334]+responce.text[335], 'Neu')
		
		
if __name__ == '__main__':
	unittest.main()		
