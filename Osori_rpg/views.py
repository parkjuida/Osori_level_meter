from django.shortcuts import render
from django.views import View
from .models import Profile


# Create your views here.
def index(request):
    if request.method == "GET":
        member_infos = Profile.objects

    return render(request, 'index.html', {'member_infos': member_infos})


# Create your views here.
def index(request):
    if request.method == "GET":
        member_infos = Profile.objects.filter(created_date__lte=timezone.now())\

    return render(request, 'index.html', {'member_infos': member_infos})


class Room_visit(View):
    def get(self, request):
        pass

    def post(self, request):
        pass

    def put(self, request):
        pass


class Event_visit(View):
    def get(self, request):
        pass

    def post(self, request):
        pass

    def put(self, request):
        pass


class Contribution(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


class Login_counter(View):
    def get(self, request):
        pass


class Level(View):
    def get(self, request):
        pass


class Exp(View):
    def get(self, request):
        pass
