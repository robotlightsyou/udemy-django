from django.contrib import admin
# from .models import User
from .models import Topic, Webpage, AccessRecord, User

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(User)