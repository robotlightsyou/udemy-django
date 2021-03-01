from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


class CBView(View):
    def  get(self, request):
       return HttpResponse("Class Based Views are cool!") 

# Create your views here.
# def index(request):
#     return render(request, 'basicapp/index.html') 