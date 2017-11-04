from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from Osori_rpg.forms import UserForm

class User_List(View):
    def get(self, request):
        user_list = User.objects.all()
        return render(request, 'list.html', {'user_list': user_list})

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

class Login_counter(View)
    def get(self, request):
        pass

class Level(View):
    def get(self, request):
        pass

class Exp(View):
    def get(self, request):
        pass