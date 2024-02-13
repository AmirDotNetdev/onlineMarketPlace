from django import forms
from .models import Item


INPUT_CLASSESS = 'w-full py-4 px-6 rounded-xl border'
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('Category' ,'name', 'description', 'price' , 'image')
        widgets = {
            'Category' : forms.Select(attrs={
                'class' : INPUT_CLASSESS
            }),
            'name' : forms.TextInput(attrs={
                'class' : INPUT_CLASSESS
            }),
            'description' : forms.Textarea(attrs={
                'class' : INPUT_CLASSESS
            }),
            'price' : forms.TextInput(attrs={
                'class' : INPUT_CLASSESS
            }),
            'image' : forms.FileInput(attrs={
                'class' : INPUT_CLASSESS
            }),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price' , 'image', 'is_sold')
        widgets = {
            
            'name' : forms.TextInput(attrs={
                'class' : INPUT_CLASSESS
            }),
            'description' : forms.Textarea(attrs={
                'class' : INPUT_CLASSESS
            }),
            'price' : forms.TextInput(attrs={
                'class' : INPUT_CLASSESS
            }),
            'image' : forms.FileInput(attrs={
                'class' : INPUT_CLASSESS
            }),
        }