from django.db import models
from multiselectfield import MultiSelectField

class EnquieyData(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=100)

    COURSE_CHOICES=(
        ('PTYHON','Python'),
        ('DJANGO','Django'),
        ('UI','Ui'),
        ('REST API','Rest Api')
    )
    courses = MultiSelectField(choices=COURSE_CHOICES, max_length=200)

    TRAINERS_CHOICES =(
        ('SAI','Sai'),
        ('NANI','Nani'),
        ('SATYA','Satya')
    )
    trainers=MultiSelectField(choices=TRAINERS_CHOICES ,max_length=200)

    BRANCHES_CHOICES=(
        ('HYD','Hyd'),
        ('BANG','Bang'),
        ('CHENNAI','Chennai')
    )
    branches = MultiSelectField(choices=BRANCHES_CHOICES,max_length=200)
    gender= models.CharField(max_length=200)
    start_date=models.DateField(max_length=100)