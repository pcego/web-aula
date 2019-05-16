from django.shortcuts import render
from workshop.core.models import Speaker


def home(request):
    return render(request, 'core/index.html')


def speaker(request):

    speakers = Speaker.objects.all()

    return render(request, 'core/speakers.html', {'speakers': speakers})


def about(request):
    return render(request, 'core/about.html')


def news(request):
    return render(request, 'core/news.html')


def events(request):
    return render(request, 'core/events.html')


def contact(request):
    return render(request, 'core/contact.html')