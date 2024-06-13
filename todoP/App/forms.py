from django.forms import ModelForm
from . models import *

class TODOForm(ModelForm):
    class Meta:
        model = TODO
        fields = ['title','status','priority']