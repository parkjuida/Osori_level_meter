from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from Osori_rpg.forms import UserForm
from .models import Profile


# Create your views here.
def index(request):
    if request.method == "GET":
        member_infos = Profile.objects

    return render(request, 'index.html', {'member_infos': member_infos})


# Create your views here.
def contribute_info(request):
    if request.method == "GET":
        pass

    return render(request, 'index.html', {'member_info': member_info})


class User_List(View):
    def get(self, request):
        user_list = User.objects.all()
        username = None
        if request.user.is_authenticated():
            username = request.user.username
        return render(request, 'list.html', {'user_list': user_list, 'username': username})


class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'signup.html', {'form': form})


class Signin(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect('/')
        else:
            return "Invalid User"


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
