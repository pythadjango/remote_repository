from django import forms
from multiselectfield import MultiSelectFormField

class EnquiryForm(forms.Form):
    name=forms.CharField(
        label="Enter Your Data ",
        widget=forms.TextInput(
            attrs={
                'placeholder':'Your name',
                'class':'form-control'
            }
        )
    )
    mobile=forms.IntegerField(
        label="Enter Your Mobile NO",
        widget=forms.NumberInput(
            attrs={
                'placeholder':'your mobile no',
                'class':'form-control'
            }
        )
    )
    email=forms.EmailField(
        label="Your Email ID",
        widget=forms.EmailInput(
            attrs={
                'placeholder':'youe Email',
                'class':'form-control'
            }
        )
    )
    COURSE_CHOICES = (
        ('PTYHON', 'Python'),
        ('DJANGO', 'Django'),
        ('UI', 'Ui'),
        ('REST API', 'Rest Api')
    )
    courses = MultiSelectFormField(choices=COURSE_CHOICES, label="select Required Field")

    TRAINERS_CHOICES = (
        ('SAI', 'Sai'),
        ('NANI', 'Nani'),
        ('SATYA', 'Satya')
    )
    trainers = MultiSelectFormField(choices=TRAINERS_CHOICES,label="select Required Trainer")

    BRANCHES_CHOICES = (
        ('HYD', 'Hyd'),
        ('BANG', 'Bang'),
        ('CHENNAI', 'Chennai')
    )
    branches=MultiSelectFormField(choices=BRANCHES_CHOICES,label="Select Your Branches")
    GENDER_CHOICES=(
        ('MALE','Male'),
        ('FEMALE','Female')
    )
    gender=forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=GENDER_CHOICES,
        label="select your Gender "
    )
    start_date=forms.DateField(
        widget=forms.SelectDateWidget()
    )