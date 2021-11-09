from django.core.mail import send_mail
from django.template.loader import render_to_string


def mail_sender(template, context, subject, recipient_list):
    message = render_to_string(template, context)
    send_mail(subject=subject, message='',
              from_email=settings.FROM_MAIL,
              recipient_list=recipient_list,
              html_message=message)