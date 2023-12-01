from django.shortcuts import render

def my_profile(request):
    context= {
        'user':
            {
            'name': "Joe",
            'username': "Joe",
            'email': "joe@joe.com",
            'phone_number': "123",
            }
    }
    return render(request, "users/my_profile.html", context)

def login(request):
    return render(request, "users/login.html")
