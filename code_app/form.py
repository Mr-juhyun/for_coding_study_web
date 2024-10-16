from django import forms
from .models import Code

class CodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = ['name', 'code']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
