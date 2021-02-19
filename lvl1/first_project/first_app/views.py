from django.shortcuts import render
from .models import Topic, Webpage, AccessRecord#, #User
from .forms import FormName
# from first_app.forms import FormName

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, "first_app/index.html", context=date_dict)

def help(request):
    temps = {'help': 'Help Page'}
    return render(request, 'first_app/help.html', context=temps)

def users(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("error: invalid")

    return render(request, 'first_app/user.html', {'form': form})


# def form_name_view(request):
#     form = here.FormName()
#     return render(request, 'first_app/form_page.html', context={'form': form})