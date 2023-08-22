from django import forms
from .models import Advertisement


class MyModelForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['titel','description', 'photo', 'price', 'auction']
        widgets = {
            'titel' : forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'photo': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
            'price': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'auction': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_titel(self):
        titel = self.cleaned_data.get('titel')
        if titel and titel.startswith('?'):
            raise forms.ValidationError("Заголовок не может начинаться с вопросительного знака")
        return titel
