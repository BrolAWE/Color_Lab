from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
SEX_CHOICES = [
    ('мужской', 'male(мужской)'),  # male, female, other
    ('женский', 'female(женский)'),
    ('другой', 'other(другой)')
]
EDU_CHOICES = [
    ('да', 'yes(да)'),
    ('нет', 'no(нет)'),
]

class Client_Color1(models.Model):
   Client_id = models.AutoField(primary_key=True)
   Client_Year = models.IntegerField(validators=[MinValueValidator(1940),MaxValueValidator(2020)])
   Client_sex = models.CharField(max_length=10, choices=SEX_CHOICES)
   Client_country1 = models.CharField(max_length=50)
   Client_country2 = models.CharField(max_length=50)
   Client_lang = models.CharField(max_length=50)
   Client_edu = models.CharField(max_length=10, choices=EDU_CHOICES)
   Client_shade = models.CharField(max_length=10, choices=EDU_CHOICES)
   color1 = models.CharField(max_length=20)
   color2 = models.CharField(max_length=20)
   color3 = models.CharField(max_length=20)
   color4 = models.CharField(max_length=20)
   color5 = models.CharField(max_length=20)
   left1 = models.CharField(max_length=20)
   left2 = models.CharField(max_length=20)
   left3 = models.CharField(max_length=20)
   left4 = models.CharField(max_length=20)
   left5 = models.CharField(max_length=20)
   left6 = models.CharField(max_length=20)
   left7 = models.CharField(max_length=20)
   left8 = models.CharField(max_length=20)
   left9 = models.CharField(max_length=20)
   left10 = models.CharField(max_length=24)
