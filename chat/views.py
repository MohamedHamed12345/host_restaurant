from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, "chat/index.html")
from django.shortcuts import render



def room(request, room_name):
    print(room_name)
    return render(request, "chat/room.html", {"room_name": room_name})