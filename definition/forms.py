from django import forms

from .models import Definition

class DefinitionForm(forms.ModelForm):
    class Meta: 
        model = Definition
        fields = [
          'title',
          'description'
    ]

    class RawDefinitionForm(forms.Form):
         title  = forms.CharField(max_length=50)
    description = forms.CharField(max_length=1000)