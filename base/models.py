from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import datetime, timedelta

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    number_of_people = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    def clean(self):
        # Check if date is not in the past
        if self.date < timezone.now().date():
            raise ValidationError("Reservation date cannot be in the past.")

        # Check if date is within the next 7 days
        if self.date > timezone.now().date() + timedelta(days=7):
            raise ValidationError("Reservation date cannot be more than 7 days in the future.")

        # Check if time is within coffee shop hours
        opening_time = datetime.combine(self.date, datetime.min.time()).replace(hour=8, minute=0, second=0, microsecond=0)
        closing_time = datetime.combine(self.date, datetime.min.time()).replace(hour=20, minute=0, second=0, microsecond=0)

        if self.date.weekday() >= 5:
            opening_time = opening_time.replace(hour=14)  # Saturday-Sunday opening time

        reservation_time = datetime.combine(self.date, self.time)
        if not (opening_time <= reservation_time <= closing_time):
            raise ValidationError("Reservation time is outside of coffee shop hours.")

        # Check if number of people is within limit
        if self.number_of_people > 4:
            raise ValidationError("Maximum number of people for a reservation is 4.")
