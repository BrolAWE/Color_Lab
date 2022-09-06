from django import forms
from .models import Client_Color1

class Client_ColorForm(forms.ModelForm):
    class Meta:
        model = Client_Color1
        fields = ('Client_id', 'Client_Year','Client_sex','Client_country1','Client_country2','Client_lang','Client_edu','Client_shade')
        labels = {
                     'Client_Year':('Год Вашего рождения :'), 'Client_sex':('Ваш пол :'), 'Client_country1':('Страна рождения :'),
                     'Client_country2':('Страна постоянного проживания :'), 'Client_lang':('Родной язык :'),
                     'Client_edu':('Художественное образование :'),
                     'Client_shade':('Испытываете ли Вы сложности с восприятием каких-либо оттенков?')
        }
        error_messages = {
            'Client_name': {
                'max_length': ("Значение слишком длинное"),
            'Client_Year': ("Значение слишком длинное"),
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Client_Year'] = forms.IntegerField(max_value=2010, min_value=1940, label = 'Год Вашего рождения :')

class Client_ColorForm_en(forms.ModelForm):
    class Meta:
        model = Client_Color1
        fields = ('Client_id', 'Client_Year','Client_sex','Client_country1','Client_country2','Client_lang','Client_edu','Client_shade')
        labels = {
                     'Client_Year':('Year of birth :'), 'Client_sex':('Gender :'), 'Client_country1':('Country of birth :'),
                     'Client_country2':('Country of residence :'), 'Client_lang':('Mother tongue :'),
                     'Client_edu':('Art Education :'),
                     'Client_shade':('Do you have difficulties seeing certain colours?')
        }
        error_messages = {
            'Client_name': {
                'max_length': ("Value is too long"),
            'Client_Year': ("Value is too long"),
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Client_Year'] = forms.IntegerField(max_value=2010, min_value=1940, label = 'Year of birth :')