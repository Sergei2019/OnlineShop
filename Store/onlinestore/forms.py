from django.forms import ModelForm

from .models import Customer


class SignUpForm(ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "email"]
