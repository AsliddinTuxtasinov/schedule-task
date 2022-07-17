from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from main.models import SendMessage


def hello(request):
    a = SendMessage.objects.first()
    t = a.send_at

    content = {
        "title": a.title,
        "body": a.body,
        "date": t.date(),
        "time": t.time(),
    }
    return JsonResponse(data=content)
