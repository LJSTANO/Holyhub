# payments/mpesa.py

import base64
import datetime
import requests
from django.conf import settings
from requests.auth import HTTPBasicAuth

# Credentials for MPesa
class Credentials:
    consumer_key = 'I2jT1lXtJO8bGUqRIdevdGAN4DgXkjENS1MM3EeMURAwb9wJ'  # Your Consumer Key
    consumer_secret = '5YXGIocBCbvmr1jD71zDmqeWTPgUQyDKnyS6JKOqABl1sdGnWANaMjrSGcWnVmWr'  # Your Consumer Secret
    api_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'  # API URL for sandbox
    shortcode = '174379'  # Your shortcode
    
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'  # Your passkey

# AccessToken class to get the token
class AccessToken:
    @staticmethod
    def get_access_token():
        response = requests.get(
            Credentials.api_url,
            auth=HTTPBasicAuth(Credentials.consumer_key, Credentials.consumer_secret)
        )
        if response.status_code == 200:
            return response.json()['access_token']
        else:
            return None  # Handle token retrieval failure

# Generate password for STK Push using base64 encoding
class Password:
    @staticmethod
    def generate_password():
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        to_encode = f'{Credentials.shortcode}{Credentials.passkey}{timestamp}'
        encoded_password = base64.b64encode(to_encode.encode()).decode('utf-8')
        return encoded_password, timestamp
