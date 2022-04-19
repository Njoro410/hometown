from django.shortcuts import redirect, render
from requests import request
from django.contrib.auth.decorators import login_required
from accounts.models import Neighbourhood
from hood.email import send_welcome_email
from .forms import UserRegistrationForm, UserProfileForm, ProfileUpdateForm, UpdateNeighbourhoodForm
from django.views.generic.edit import CreateView
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']

            form.save()
            send_welcome_email(name,email)
            return redirect('profile')
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/registration.html', {'form': form})

@login_required
def user_info(request):
    if request.method == 'POST':
        address = request.POST['address']
        loc = Neighbourhood.objects.create(address=address,user=request.user)
        location = Neighbourhood.objects.filter(user=request.user)
        for result in location:
            loc = result.id
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        


        if p_form.is_valid():
            profile = p_form.save(commit=False)
            profile.location_id = loc
            profile.save()
            return redirect('home')
    else:
        # n_form = UpdateNeighbourhoodForm(instance = request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'p_form': p_form

    }

    return render(request, 'accounts/profile.html', context)



