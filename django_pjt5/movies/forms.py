from django import forms
from .models import *

# Create your models here.
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'