from django import forms
from .models import User

class FormName(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
    # first = forms.CharField()
    # last = forms.CharField()
    # email = forms.EmailField()
    # verify_email = forms.EmailField(label="Enter your email again")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)