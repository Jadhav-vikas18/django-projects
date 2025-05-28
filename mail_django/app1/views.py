from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

def x(request):
    send_mail(
        subject='hey python developer',
        message='keep hands on pratices',
        from_email='vikasjadhav9505@gmail.com',
        recipient_list=['velpulabhanuprasad@gmail.com','hifivijay87@gmail.com'],
        fail_silently=False

    )
    return HttpResponse("Email send sucessfully...")