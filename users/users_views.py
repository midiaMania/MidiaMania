from django.shortcuts import render, redirect
from django.views import View

class My_profile(View):
    context= {
        'user':
        {
            'name': "Joe",
            'username': "Joe",
            'email': "joe@joe.com",
            'phone_number': "123",
            'shopping':[
                {
                    'type':'Música',
                    'name':'Kid Abelha',
                    'price': "{:,.2f}".format(14).replace('.', ','),
                    'img': "musics/images/1.jpg",
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
    }

    def get(self, request):
        return render(request, "users/my_profile.html", self.context)

    def post(self, request):
        new_name = request.POST.get('name')
        new_username = request.POST.get('username')
        new_email = request.POST.get('email')
        new_phone_number = request.POST.get('phone_number')
        new_password = request.POST.get('password')

        if new_username:
            self.context['user']['username'] = new_username
        if new_name:
            self.context['user']['name'] = new_name
        return redirect('my_profile')


def login(request):
    return render(request, "users/login.html")

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
     return render(request, "users/cart.html", context)

