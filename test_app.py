from unittest import TestCase
from app import app

class HomePage(TestCase):
    def test_forex_form(self):
        with app.test_client() as client:
            res=client.get('/')
            html=res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200 )
            self.assertIn('<h1>Forex Converter</h1>', html)

    def test_result_page(self):
        with app.test_client() as client:
            res=client.post('/result', data={'convert_from':'GBP', 'convert_to': 'USD', 'amount': '50'})
            html=res.get_data(as_text=True)
 
            self.assertEqual(res.status_code, 200 )
            self.assertIn('<h3>The result is $', html)

class TestResultPage(TestCase):      
    def test_valid_result_page(self):
        with app.test_client() as client:
            response = client.post('/result', data={'convert_from': 'GBP', 'convert_to': 'USD', 'amount': '50'})
            html=response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<h3>The result is $', html)

        with app.test_client() as client:
            response = client.post('/result', data={'convert_from': 'USD', 'convert_to': 'USD', 'amount': '1'})
            html=response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<h3>The result is $1</h3>', html)

    def test_invalid_amount(self):
        with app.test_client() as client:
            response = client.post('/result', data={'convert_from': 'USD', 'convert_to': 'EUR', 'amount': 'ghghghg'}, follow_redirects=True)
            html=response.get_data(as_text=True)
            print(html)

            self.assertEqual(response.status_code, 200)  
            self.assertIn('<p class="error">Not a valid amount:', html)

    def test_invalid_currency_from(self):
        with app.test_client() as client:
            response = client.post('/result', data={'convert_from': 'AAA', 'convert_to': 'EUR', 'amount': '100'}, follow_redirects=True)
            html=response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200) 
            self.assertIn('<p class="error">Not a valid code:', html)

    def test_invalid_currency_to(self):
        with app.test_client() as client:
            response = client.post('/result', data={'convert_from': 'USD', 'convert_to': 'AAA', 'amount': '100'}, follow_redirects=True)
            html=response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)  # Redirect to home page on error
            self.assertIn('<p class="error">Not a valid code:', html)
