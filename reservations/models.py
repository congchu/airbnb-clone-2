from django.db import models
from django.utils import timezone
from core import models as core_models


class Reservation(core_models.TimeStampledModel):
    """ Reservation Model Definition"""

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"
    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    )
    status = models.CharField(
        choices=STATUS_CHOICES, default=STATUS_PENDING, max_length=12
    )
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey(
        "users.User", related_name="reservations", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reservations", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.room} - {self.check_in}"

    def in_progress(self):
        # 현재 날짜가 check_in 날짜보다 크고, check_out 날짜보다 작으면 in_progress
        now = timezone.now().date()
        return now > self.check_in and now < self.check_out

    in_progress.boolean = True

    def in_finished(self):
        now = timezone.now().date()
        return now > self.check_out

    in_finished.boolean = True
