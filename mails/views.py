from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from mails.models import Mail


def index(request):
    return render(request, "layout.html", {'mails': Mail.objects.all()})


@csrf_exempt
def destroy(request, mail_id):
    mail = Mail.objects.get(pk=mail_id)
    mail.delete()
    return redirect(index)

@csrf_exempt
def read(request, mail_id):
    mail = Mail.objects.get(pk=mail_id)
    mail.mail_is_read = True
    mail.save()
    return redirect(index)