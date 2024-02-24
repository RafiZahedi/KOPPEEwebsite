from django import forms
from .models import Reservation


class ReserveFrom(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control bg-transparent border-primary p-4',
                       'style': 'color: white'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control bg-transparent border-primary p-4',
                       'style': 'color: white'}),
            'date': forms.DateInput(
                attrs={'class': 'form-control bg-transparent border-primary p-4',
                       'style': 'color: white'}),
            'time': forms.TimeInput(
                attrs={'class': 'form-control bg-transparent border-primary p-4',
                       'style': 'color: white'}),
            'number_of_people': forms.NumberInput(
                attrs={'class': 'form-control bg-transparent border-primary p-4',
                       'style': 'color: white'}),
        }
