import africastalking
from django.conf import settings


def initialize_sdk():
    # Initialize the Africa's Talking SDK with credentials from settings.py
    africastalking.initialize(username=settings.AFRICASTALKING_USERNAME, api_key=settings.AFRICASTALKING_API_KEY)


def send_sms(phone_numbers, message):
    initialize_sdk()

    # Define the SMS service
    sms = africastalking.SMS

    try:
        # Send the SMS to the list of phone numbers
        response = sms.send(message, phone_numbers)
        return response
    except Exception as e:
        return {'error': str(e)}
