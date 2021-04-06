from django.db import models
from core import models as core_models
import core
from users import models as user_models
from django_countries.fields import CountryField


class AbstractItem(core_models.TimeStampledModel):
    """ Abstract Item Model Definition"""
    name = models.CharField(max_length=80)
    class Meta:
        abstract = True
    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """ Room Type Model Definition"""
    pass


class Room(core_models.TimeStampledModel):
    """ Room Model Definition"""
    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms= models.IntegerField()
    baths= models.IntegerField()
    bathrooms= models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    room_types= models.ManyToManyField(RoomType, blank=True)

    def __str__(self):
        return self.name




    