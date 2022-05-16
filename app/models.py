from django.db import models
SEX_CHOICES = [
    ('мужской', 'мужской'),
    ('женский', 'женский'),
    ('другой', 'другой')
]
EDU_CHOICES = [
    ('да', 'да'),
    ('нет', 'нет'),
]

class Client_Color1(models.Model):
   Client_id = models.AutoField(primary_key=True)
   Client_Year = models.IntegerField()
   Client_sex = models.CharField(max_length=10, choices=SEX_CHOICES)
   Client_country1 = models.CharField(max_length=50)
   Client_country2 = models.CharField(max_length=50)
   Client_lang = models.CharField(max_length=50)
   Client_edu = models.CharField(max_length=10, choices=EDU_CHOICES)
   Client_shade = models.CharField(max_length=10, choices=EDU_CHOICES)
   color1 = models.CharField(max_length=10)
   color2 = models.CharField(max_length=10)
   color3 = models.CharField(max_length=10)
   color4 = models.CharField(max_length=10)
   color5 = models.CharField(max_length=10)
   left1 = models.CharField(max_length=5)
   left2 = models.CharField(max_length=5)
   left3 = models.CharField(max_length=5)
   left4 = models.CharField(max_length=5)
   left5 = models.CharField(max_length=5)
   left6 = models.CharField(max_length=5)
   left7 = models.CharField(max_length=5)
   left8 = models.CharField(max_length=5)
   left9 = models.CharField(max_length=5)
   left10 = models.CharField(max_length=5)




