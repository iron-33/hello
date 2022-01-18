from .models import Name
from django.forms import ModelForm, fields, widgets, TextInput

class NameForm (ModelForm):
    class Meta:
        model = Name
        fields = ['name']
        widgets = {
            "name": TextInput(attrs={
                'class':'form-control',
                'placeholder' : 'введи имя'
            })}
    
    