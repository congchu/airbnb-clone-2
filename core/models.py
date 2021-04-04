from django.db import models

class TimeStampledModel(models.Model):
    
    """ TimeStampledModel """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        abstract = True
    
