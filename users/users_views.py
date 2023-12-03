from django.shortcuts import render

def my_profile(request):
    context= {
        'user':
        {
            'name': "Joe",
            'username': "Joe",
            'email': "joe@joe.com",
            'phone_number': "123",
            'address':[
                ['Centro', 'Rua 1', 25],
                ['Areia Branca', 'Rua 2', 27],
            ], 
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
    return render(request, "users/my_profile.html", context)

def login(request):
    return render(request, "users/login.html")

def signup(request):
    return render(request, "users/signup.html")

def checkout(request):
    return render(request, "users/checkout.html")

def cart(request):
    return render(request, "users/cart.html")

