from django.db import models
from django.core import validators


class Sensor(models.Model):
    serial_number = models.CharField(
        verbose_name="S/N",
        primary_key=True,
        max_length=64,
        blank=False,
        null=False,
        validators=[validators.RegexValidator(
            regex='^[0-9a-zA-Z-]+$',
            message='numeric, alphabet or hylien'
        )]
    )
    display_name = models.CharField(
        verbose_name="Display Name",
        max_length=128,
        blank=True,
        null=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.serial_number
