from celery import shared_task
from .models import DailyDevotion
from Members.models import Member
from sermons.utils.sms_utils import send_sms
from django.core.mail import send_mail
from datetime import date

@shared_task
def send_daily_devotion():
    today = date.today()
    devotion = DailyDevotion.objects.filter(date=today).first()

    if devotion:
        # Get all members' phone numbers
        members = Member.objects.all()
        phone_numbers = []

        for member in members:
            phone_number = member.phone_number
            if phone_number and not phone_number.startswith('+'):
                phone_number = '+254' + phone_number[1:]
            phone_numbers.append(phone_number)

        message = f"Today's Devotion: {devotion.title}\n{devotion.content}"

        # Send SMS
        send_sms(phone_numbers, message)

        # Send Email
        email_addresses = [member.email for member in members if member.email]
        send_mail(
            'Daily Devotion',
            f"Today's Devotion: {devotion.title}\n{devotion.content}",
            'from@example.com',
            email_addresses,
            fail_silently=False,
        )

        return f"Devotion sent to {len(phone_numbers)} members and {len(email_addresses)} emails."
    else:
        return 'No devotion available for today.'
