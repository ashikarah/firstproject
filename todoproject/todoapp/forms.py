from . models import tasks
from django import forms
class todoform(forms.ModelForm):
    class Meta:
        model=tasks
        fields=['name','priority','date']