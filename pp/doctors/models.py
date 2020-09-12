from django.db import models


class Doctor(models.Model):
    RATINGS = [('1', '1'), ('2','2'), ('3','3'), ('4','4'), ('5','5')]
    SPECIALIZATIONS = [
        ('', ''),
        ('CD','Cardiologist'),
        ('GE','Gastroenterologist'),
        ('GN','Gynecologist'),
        ('OB','Obstetrician'),
        ('PS','Psychiatrist')
    ]
    name = models.CharField(max_length=100, null=False)
    specialization = models.CharField(
        max_length=2,
        choices=SPECIALIZATIONS,
        default=' ',
        null=False
    )
    rating = models.CharField(
        max_length=1,
        choices=RATINGS,
        null=True
    )
