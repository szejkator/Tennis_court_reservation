from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class TennisCourt(models.Model):
    CITY = [
        ("Białystok", "Białystok"),
        ("Gdańsk", "Gdańsk"),
        ("Kraków", "Kraków"),
        ('Lublin', 'Lublin'),
        ("Olsztyn", "Olsztyn"),
        ("Poznań", "Poznań"),
        ("Warszawa", "Warszawa"),
        ("Wrocław", "Wrocław"),
    ]

    city = models.CharField(choices=CITY, max_length=24)
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    open_hour = models.TimeField()
    close_hour = models.TimeField()
    hire_price = models.IntegerField()
    equipment_rent = models.BooleanField()
    equipment_cost = models.IntegerField(default=0)
    short_description = models.CharField(max_length=1024, default='')

    def __str__(self):
        return f'{self.city} - {self.name} - {self.address}'


class Reservations(models.Model):
    court = models.ForeignKey(
        TennisCourt,
        on_delete=models.CASCADE,
        related_name="reservations",
        blank=False,
        null=False
    )

    reservation_date = models.DateField()
    reservation_start = models.TimeField()
    reservation_end = models.TimeField()

    # class Meta:
    #     ordering = ['object']

    # reservation_status = models.BooleanField(default=False)
    # reservation_cost = models.IntegerField()

    def __str__(self):
        return f'{self.court}'


# class Profile(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)


class AdminPanel(models.Model):
    pass


if __name__ == '__main__':
    pass
