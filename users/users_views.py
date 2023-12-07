from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout

class My_profile(View):
    context= {
        'phone_number': "(99) 9 9999-9999",
        'shopping':[
            {
                'type':'Música',
                'name': "The Beatles",
                'price': "{:,.2f}".format(5).replace('.', ','),
                'img': "musics/images/2.jpg",
                'date': '13/04/2020'
            },
            {
                'type': 'Filme',
                'name': "MIB",
                'price': "{:,.2f}".format(14).replace('.', ','),
                'img': "movies/images/2.jpg",
                'date': '13/04/2020'
            },
            {
                'type':'Jogo',
                'name': "Watch Dogs",
                'price': "{:,.2f}".format(40).replace('.', ','),
                'img': "games/images/3.jpg",
                'date': '13/04/2020'
            },
        ]
    }

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "users/my_profile.html", {
                'data': self.context,
                'user': request.user
            })
        else:
            return redirect('login')

    def post(self, request):
        user = request.user
        
        new_name = request.POST.get('name')
        new_username = request.POST.get('username')
        new_email = request.POST.get('email')
        new_phone_number = request.POST.get('phone_number')
        new_password = request.POST.get('password')

        if new_name != '':
            first_name, *last_name= new_name.split(" ", 1)
            user.first_name = first_name
            if last_name:
                user.last_name = last_name[0]
                
        if new_username != '':
            user.username = new_username
            
        if new_email != '':
            user.email = new_email
        
        if new_password != '':
            user.set_password(new_password)
            
        user.save()
        return redirect('my_profile')


class Login(View):
    def get(self,request):
        return render(request, "users/login.html")
    
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('my_profile')
        return redirect('login')

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('home')



def signup(request):
    return render(request, "users/signup.html")

def checkout(request):
    return render(request, "users/checkout.html")

def cart(request):
     context= {
                'cart':[
                    {
                        'type': 'Filme',
                        'name': "MIB",
                        'price': "{:,.2f}".format(14).replace('.', ','),
                        'img': "movies/images/2.jpg",
                    },
                    {
                        'type':'Jogo',
                        'name': "Watch Dogs",
                        'price': "{:,.2f}".format(40).replace('.', ','),
                        'img': "games/images/3.jpg",
                    },
                    {
                        'type':'Música',
                        'name':'Kid Abelha',
                        'price': "{:,.2f}".format(14).replace('.', ','),
                        'img': "musics/images/1.jpg",
                    },
                ],
                'total_price': "{:,.2f}".format(68).replace('.', ','),
            }
     if request.user.is_authenticated:
        return render(request, "users/cart.html", context)
     else:
         return redirect('login')

