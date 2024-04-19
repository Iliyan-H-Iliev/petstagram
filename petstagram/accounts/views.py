from django.shortcuts import render


# Create your views here.

def signup_profile(request):
    context = {}
    return render(request, 'accounts/signup_profile.html', context)


def signin_profile(request):
    context = {}
    return render(request, 'accounts/signin_profile.html', context)


def signout_profile(request):
    return None


def details_profile(request):
    context = {}
    return render(request, 'accounts/details_profile.html', context)


def edit_profile(request):
    context = {}
    return render(request, 'accounts/edit_profile.html', context)


def delete_profile(request):
    context = {}
    return render(request, 'accounts/delete_profile.html', context)
