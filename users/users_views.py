from django.shortcuts import render

def my_profile(request):
    return render(request, "users/my_profile.html")
