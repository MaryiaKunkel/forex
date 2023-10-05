# from unittest import TestCase
# from app import app

# class HomePage(TestCase):
#     def test_forex_form(self):
#         with app.test_client() as client:
#             res=client.get('/')
#             html=res.get_data(as_text=True)

#             self.assertEqual(res.status_code, 200 )
#             self.assertIn('<h1>Forex Converter</h1>', html)

#     def test_result_page(self):
#         with app.test_client() as client:
#             res=client.post('/result', data={'convert_to': 'USD'})
#             html=res.get_data(as_text=True)
 
#             self.assertEqual(res.status_code, 200 )
#             self.assertIn('<h3>The result is $', html)

