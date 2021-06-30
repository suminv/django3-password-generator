from django.shortcuts import render
from django.http import HttpResponse
import random
import string

# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password': '121212121hhhh'})


def about(request):
    return render(request, 'generator/about.html')


def password(request):  
    letters = string.ascii_letters
    digids = string.digits
    special_characters = string.punctuation
    all_symbol = []
    
    lenght = int(request.GET.get('lenght', 12))

    try:

        if request.GET.get('uppercase'):
            all_symbol.extend(letters)
        
        if request.GET.get('mumbers'):
            all_symbol.extend(digids)

        if request.GET.get('special'):
            all_symbol.extend(special_characters)
        
        thepassword = '' 

        for _ in range(lenght):
            thepassword += random.choice(all_symbol)

    except IndexError:
        return render(request, 'generator/error.html')
        # return HttpResponse('<h1>Please choice box!</h1>') 


    return render(request, 'generator/password.html', {'password': thepassword}) 
