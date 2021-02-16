from django.shortcuts import render
from .models import Topic, Webpage, AccessRecord, User
# from forms import FormName

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, "first_app/index.html", context=date_dict)

def help(request):
    temps = {'help': 'Help Page'}
    return render(request, 'first_app/help.html', context=temps)

def users(request):
    user_list = User.objects.order_by('first')
    user_dict = {'userinfo': user_list}
    return render(request, 'first_app/user.html', context=user_dict)

# def form_name_view(request):
#     form = forms.FormName()
#     return render(request, 'first_app/form.html', context={'form': form})