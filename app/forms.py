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


