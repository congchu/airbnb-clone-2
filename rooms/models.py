from django.db import models
from core import models as core_models
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
    class Meta:
        verbose_name_plural ="Room Types"
        ordering = ["name"]



class Amenity(AbstractItem):
    """ Amenity Type Model Definition """
    class Meta:
        verbose_name_plural ="Amenities"


class Facility(AbstractItem):
    """ Factility Type Model Definition """
    class Meta:
        verbose_name_plural ="Facilities"


class HouseRule(AbstractItem):
    """ House Rule Type Model Definition """
    class Meta:
        verbose_name_plural ="House Rules"

class Photo(core_models.TimeStampledModel):
    """ Photo Model Definition """
    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

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
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room_types= models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
    amenities= models.ManyToManyField("Amenity", blank=True)
    facilities= models.ManyToManyField("Facility", blank=True)
    house_rules= models.ManyToManyField("HouseRule", blank=True)

    def __str__(self):
        return self.name
        




    