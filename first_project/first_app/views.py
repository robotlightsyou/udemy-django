from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def index(request):
    my_dict = {'insert_me': "Hello, I am from views.py.", 'second': 'I am the second piece of context.'}
    return render(request, "first_app/index.html", context=my_dict)

