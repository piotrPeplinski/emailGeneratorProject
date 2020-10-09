from django.shortcuts import render
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def email(request):
    letters = "abcdefghijklmnoprstuwxyz"
    lower = list(letters)
    upper = list(letters.upper())
    numbers = list("1234567890")

    length = int(request.GET.get('length'))

    pula = lower + upper

    if request.GET.get('numbers'):
        pula += numbers

    domain = request.GET.get('domain')

    nazwa = ""

    for _ in range(length):
        nazwa += random.choice(pula)

    mail = nazwa+domain

    return render(request, 'generator/email.html', {'mail': mail})


def about(request):
    return render(request, 'generator/about.html')
