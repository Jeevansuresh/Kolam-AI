# from twilio.rest import Client
# import smtplib
# from email.mime.text import MIMEText
from utils.config import *

# Commented out Twilio client
# twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_whatsapp_message(body, to=MAID_PHONE_NUMBER):
    print(f"WhatsApp message sent to {to}: '{body}'")
    # message = twilio_client.messages.create(
    #     body=body,
    #     from_='whatsapp:' + TWILIO_PHONE_NUMBER,
    #     to='whatsapp:' + to
    # )
    # print(f"Twilio response: {message.sid}")
    return "WhatsApp message sent."

def send_booking_email(user_query):
    print(f"Booking email sent with message: '{user_query}'")
    # try:
    #     msg = MIMEText(f"New booking request: '{user_query}'")
    #     msg['Subject'] = "New Booking Request"
    #     msg['From'] = EMAIL_USERNAME
    #     msg['To'] = RESERVATION_EMAIL
    #
    #     with smtplib.SMTP("smtp.gmail.com", 587) as server:
    #         server.starttls()
    #         server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
    #         server.sendmail(EMAIL_USERNAME, [RESERVATION_EMAIL], msg.as_string())
    # except:
    #     pass
    return "Booking email sent."
