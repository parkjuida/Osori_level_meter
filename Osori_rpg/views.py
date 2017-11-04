from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q

import requests
import json

from Osori_rpg.forms import UserForm
from .models import ExpRequest as ExpRequestModel
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

    print(id)

    return render(request, 'contribute_info.html')


# Create your views here.
def update_info(request):

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
        member = Profile.objects.get(username=contribute_info['login'])
        member.git_commit = commit_counts[contribute_info['login']]
        member.save()

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


class ExpRequest(View):
    def get(self, request):
        user = None
        if request.user.is_authenticated():
            user = request.user
        if user is None:
            return "User is None"

        return render(request, 'exp_request.html', {'user': user})

    def post(self, request):
        option = request.POST['option']
        spec = request.POST['spec']

        expRequest = ExpRequestModel.objects.create(owner=request.user, options=option, spec=spec)
        expRequest.save()
        return redirect('/')


class ExpRequestAccept(View):
    def get(self, request):
        expRequests = ExpRequestModel.objects.filter(~Q(owner=request.user))

        return render(request, 'exp_request_list.html', {'expRequestList':expRequests})

    def post(self, request):
        pk = request.POST['pk']
        owner = request.POST['owner']
        option = request.POST['option']
        user = User.objects.get(username=owner)
        profile = Profile.objects.get(user=user)
        print(profile)
        print(option)
        if option == 'Room_Visit':
            print('RV')
            profile.room_visit = profile.room_visit + 1
            profile.save()
        if option == 'Event_Visit':
            print('EV')
            profile.event_visit = profile.event_visit + 1
            profile.save()
        if option == 'Contribution':
            print('CB')
            profile.contribution = profile.contribution + 1
            profile.save()
        expRequest = ExpRequestModel.objects.get(pk=pk)
        expRequest.delete()
        return redirect('/exp_request_list')

    def delete(self, request):
        pk = request.GET['pk']
        expRequest = ExpRequestModel.objects.get(pk=pk)
        expRequest.delete()
        return redirect('/exp_request_list')
