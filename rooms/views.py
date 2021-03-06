from django.utils import timezone
from math import ceil
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models

class HomeView(ListView):
    """ RoomView Definition """ 
    model = models.Room
    paginate_by=10
    paginate_orphans = 5
    page_kwarg = "page"
    ordering = "created"
    context_object_name="rooms"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context

class RoomDetail(DetailView):
    """Room Detail View Definition"""
    model = models.Room



def search(request):
    city = request.GET.get("city")
    print(str.capitalize(city))
    return render(request, "rooms/search.html",{"city":city})
