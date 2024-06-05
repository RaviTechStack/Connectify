from django.core.mail import send_mail
from django.conf import settings

def email_send(email, token):
    subject = "mail to verify and password changing"
    message = f"click on the link to change password http://127.0.0.1:8000/changePassword/{token}"
    email_from = settings.Email_user
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True