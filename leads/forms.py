from django import forms
from .models import Student,Studentlogin

class For(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
class For1(forms.ModelForm):
    class Meta:
        model=Studentlogin
        fields="__all__"