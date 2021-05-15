from math import ceil
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models


def all_rooms(request):
    page = request.GET.get("page")
    room_list = models.Room.objects.all()
    pagenator = Paginator(room_list, 10)
    rooms = pagenator.get_page(page)
    print(vars(rooms.paginator))

    return render(
        request,
        "rooms/home.html",
        context={
            "rooms": rooms,
        },
    )
