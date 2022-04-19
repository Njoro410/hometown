from token import NEWLINE
from django.shortcuts import redirect, render
from accounts.models import Neighbourhood, Profile
from django.contrib.auth.models import User
from hood.models import Hospitals, Police, Posts, Business
from .forms import AddBusinessForm, AddPostForm, UpdateProfileForm
import requests
# Create your views here.


def Index(request):
    return render(request, 'index.html')


def Home(request):

    location = Neighbourhood.objects.filter(user=request.user)
    name = None
    posts = None
    loc = None
    lat = None
    long = None
    for result in location:
        print(result.id)
        loc = result.id
        lat = result.lat
        long = result.long
        name = result.address
        posts = Posts.objects.filter(location_id=loc)
        response = requests.get('http://api.weatherapi.com/v1/current.json?key=561e389cf8ea4557baf50616222702&q={}&aqi=no'.format(name))
        weather = response.json()

    return render(request, 'home.html', {'location': name, 'posts': posts, 'locid':loc,'lat':lat,'long':long,'weather':weather})


def Create_posts(request):

    location = Neighbourhood.objects.filter(user = request.user)
    for result in location:
        loc = result.id
    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.location_id = loc
            data = post.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'addpost.html', {'form': form})


def AddBusiness(request):
    location = Neighbourhood.objects.filter(user = request.user)
    
    for result in location:
        loc = result.id
    if request.method == "POST":
        form = AddBusinessForm(request.POST)
        if form.is_valid():
            business = form.save(commit = False)
            business.owner = request.user
            business.location_id = loc
            data = business.save()
            return redirect('home')
    else:
        form = AddBusinessForm()
    return render(request,'addbusiness.html',{'form':form})



def Businesses(request,id):
    business = Business.objects.filter(location_id=id)
    
    
    return render (request,'business.html',{'businesses':business})

def Hospital(request,id):
    hospital = Hospitals.objects.filter(location_id=id)
    
    
    return render (request,'hospitals.html',{'hospitals':hospital})

def Law(request,id):
    police = Police.objects.filter(location_id=id)
    
    
    return render (request,'police.html',{'police':police})



def UserInfo(request,id):
    data = User.objects.get(id=id)
    posts = Posts.objects.filter(owner=request.user)
    return render(request,'userprofile.html',{'data':data,'posts':posts})
            
def admin(request):
    
    return render(request,'admin.html')