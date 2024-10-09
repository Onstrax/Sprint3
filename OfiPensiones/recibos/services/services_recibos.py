from OfiPensiones.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

def check_alarm(value):
    if value >= 42:
        send_email()
    return()

def send_email():
    subject = 'Test Broker OfiPensiones'
    message = 'Creacion de factura'
    recepient = "estudiante@hotmail.com"
    send_mail(subject, message, EMAIL_HOST_USER, [recepient])