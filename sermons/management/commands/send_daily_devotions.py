from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings
from sermons.models import DailyDevotion
from Members.models import Member
from sermons.utils.sms_utils import send_sms
from datetime import date

class Command(BaseCommand):
    help = 'Send daily devotion to all members via SMS and Email'

    def handle(self, *args, **kwargs):
        # Get today's devotion
        today = date.today()
        devotion = DailyDevotion.objects.filter(date=today).first()

        if devotion:
            # Get all members' phone numbers and email addresses
            members = Member.objects.all()
            phone_numbers = []
            email_addresses = []

            # Format phone numbers to E.164 format (e.g., +254742609790)
            for member in members:
                # Collect phone numbers
                phone_number = member.phone_number
                if phone_number and not phone_number.startswith('+'):
                    phone_number = '+254' + phone_number[1:]  # Assuming Kenya's country code
                phone_numbers.append(phone_number)

                # Collect email addresses
                email = member.email
                if email:
                    email_addresses.append(email)

            # Send SMS with the daily devotion content
            sms_message = f"Today's Devotion: {devotion.title}\n{devotion.content}"
            response = send_sms(phone_numbers, sms_message)

            # Check if response is a valid list
            if isinstance(response, list):
                successful_sends = [r for r in response if r.get('status') == 'Success']
                failed_sends = [r for r in response if r.get('status') != 'Success']

                if successful_sends:
                    self.stdout.write(self.style.SUCCESS(f"Successfully sent devotion to {len(successful_sends)} members via SMS"))
                if failed_sends:
                    self.stdout.write(self.style.WARNING(f"Failed to send devotion via SMS to {len(failed_sends)} members"))

            else:
                self.stdout.write(self.style.ERROR(f"Failed to send devotion via SMS: {response}"))

            # Send email with the daily devotion content
            email_subject = f"Today's Devotion: {devotion.title}"
            email_message = devotion.content

            if email_addresses:
                send_mail(
                    email_subject,
                    email_message,
                    settings.DEFAULT_FROM_EMAIL,  # Ensure DEFAULT_FROM_EMAIL is set in settings.py
                    email_addresses,
                    fail_silently=False,
                )
                self.stdout.write(self.style.SUCCESS(f"Successfully sent devotion to {len(email_addresses)} members via Email"))
            else:
                self.stdout.write(self.style.WARNING("No email addresses available for sending emails"))

        else:
            self.stdout.write(self.style.WARNING('No devotion available for today'))
