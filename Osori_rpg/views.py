from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

import requests
import json

from Osori_rpg.forms import UserForm
from .models import Profile


# Create your views here.
def index(request):
    if request.method == "GET":
        member_infos = Profile.objects.all()

        print(member_infos)

    return render(request, 'index.html', {'member_infos': member_infos})


# Create your views here.
def contribute_info(request):
    id = request.GET['id']

    list_osori_repo_url = 'https://api.github.com/orgs/HyOsori/repos?\
        access_token=6a49e18d2cf83edf2d8717b42517fccec77d1e6f'

    # GET
    response = requests.get(list_osori_repo_url)
    repo_infos = json.loads(response.text)

    commit_counts = {}

    print("총 Repository 개수 : %d" % len(repo_infos))

    for repo_info in repo_infos:
        try:
            print(repo_info['name'])
        except:
            continue

        contribute_info_url = "https://api.github.com/repos/HyOsori/%s/contributors?access_token=\
            6a49e18d2cf83edf2d8717b42517fccec77d1e6f" % repo_info['name']
        response = requests.get(contribute_info_url)

        contribute_infos = json.loads(response.text)
        for contribute_info in contribute_infos:
            try:
                commit_counts[contribute_info['login']] += contribute_info['contributions']
                # print(contribute_info['login'])
                # print(contribute_info['contributions'])
            except:
                try:
                    commit_counts.update({contribute_info['login']: contribute_info['contributions']})
                except:
                    continue

    for id in commit_counts:
        print(id + ":" + str(commit_counts[id]))

    return render(request, 'contribute_info.html')


# Create your views here.
def update_info(request):

    # 업데이트 하자

    return redirect('index_page')


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
