from django.shortcuts import render
from .models import Topic, Webpage, AccessRecord


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, "first_app/index.html", context=date_dict)

def help(request):
    temps = {'help': 'Help Page'}
    return render(request, 'first_app/help.html', context=temps)