from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from timezone_field import TimeZoneField
import datetime


class Country(models.Model):
    name = models.CharField(max_length=32, unique=True)
    timezone = TimeZoneField(default='Europe/Lisbon')

    class Meta:
        verbose_name = "country"
        verbose_name_plural = "countries"

    def __str__(self):
        return self.name


class ChosenCountry(models.Model):
    FORMATS = (
        (1, "%H:%M:%S"),
        (2, "%l:%M:%p"),
        (3, "%r"),
        (4, "%R"),
        (5, "%T")
    )
    # better put this on forms to prevent large generated migrations
    #choices = [
    #    (timezone, timezone)
    #    for timezone in pytz.common_timezones
    #],
    country = models.ForeignKey(
        'Country',
        on_delete=models.CASCADE
    )
    profile = models.ForeignKey(
        'Profile',
        on_delete=models.CASCADE
    )
    format = models.IntegerField(choices=FORMATS, default=1)

    def __str__(self):
        now = self.time.strftime(self.get_format_display())
        return now

    @property
    def time(self):
        timezone = self.country.timezone
        return datetime.datetime.now(timezone)


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    countries = models.ManyToManyField(
        'Country',
        related_name='profiles',
        through=ChosenCountry,
        through_fields=["profile", "country"]
    )

    def __str__(self):
        return self.user.username

    def add_country(self, country):
        total_countries = self.countries.count()
        # check if 5 to 10 different countries
        if total_countries < 5 or total_countries > 10:
            return False

        # creates hascountry preventing duplicates
        ChosenCountry.objects.get_or_create(
            country=country,
            profile=self
        )
        return True

    def del_country(self, country):
        total_countries = self.countries.count()
        # prevents having less than 5 countries
        if total_countries < 6:
            return False
        qs_delete = ChosenCountry.objects.filter(
            country=country,
            profile=self
        )
        if qs_delete.count() == 0:
            return False
        qs_delete.delete()
        return True


@receiver(post_save, sender=User, )
def create_progile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance
        )

