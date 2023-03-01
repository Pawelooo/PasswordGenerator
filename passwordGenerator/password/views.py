import random
import string

from django.forms import Form
from django.shortcuts import render


def main(request):
    if request.method == "POST":
        form = Form(request.POST)
        
        if form.is_valid():
            password_generate = ''
            signs = list(string.ascii_lowercase)
            if request.POST.get('uppercase'):
                signs.extend(string.ascii_uppercase)

            if request.POST.get('digits'):
                signs.extend(string.digits)

            if request.POST.get('punctuation'):
                signs.extend(string.punctuation)

            length_of_password = request.POST.get('length')
            for _ in range(int(length_of_password)):
                password_generate += random.choice(signs)

            return render(request, 'password.html',
                          {'password': password_generate})

    return render(request, 'main.html')
