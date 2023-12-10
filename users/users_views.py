from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import ShoppingCartItem
from movies.models import Movie
from musics.models import Music
from games.models import Game

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
            redirect_url = request.session.get('cart_redirect', None)
            if redirect_url:
                del request.session['cart_redirect']
                return redirect(redirect_url)
            else:
                return redirect('my_profile')
        else:
            messages.error(request, 'Usuário ou senha incorretos')
        return render(request, 'users/login.html')

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('home')


class SignUp(View):
    def get(self, request):
        return render(request, "users/signup.html")
    
    def post(self,request):
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if name == '':
            return redirect(reverse("signup") + "?error=O Nome não pode ser vazio")
        
        if username == '':
            return redirect(reverse("signup") + "?error=O Username não pode ser vazio")
        
        if password != password2:
            return redirect(reverse("signup") + "?error=As senhas não são iguais")
        
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            
            first_name, *last_name= name.split(" ", 1)
            user.first_name = first_name
            if last_name:
                user.last_name = last_name[0]
            user.email = email
            user.save()
            
            return redirect(reverse("login") + "?success=true")
        except IntegrityError:
            return redirect(reverse("signup") + "?error=O Username já está em uso")
        except Exception as e:
            return redirect(reverse("signup") + f"?error={e}")
    

def signup(request):
    return render(request, "users/signup.html")

def checkout(request):
    return render(request, "users/checkout.html")

def cart(request):
     if request.user.is_authenticated:
        cart_items = ShoppingCartItem.objects.filter(user=request.user, purchase_date__isnull=True)
        if request.method == 'POST':
            item_id = request.POST.get('item_id')
            if item_id:
                ShoppingCartItem.objects.filter(id=item_id, user=request.user).delete()
                return redirect('cart')
        context = {
            'cart': [
                {
                    'id': item.id,
                    'type': item.product_type,
                    'name': item.product_name,
                    'price': "{:,.2f}".format(item.product_price).replace('.', ','),
                    'img': item.product_image.url,
                }
                for item in cart_items
            ],
            'total_price': "{:,.2f}".format(sum(item.product_price for item in cart_items)).replace('.', ','),
        }        
        return render(request, "users/cart.html", context)
     else:
        request.session['cart_redirect'] = reverse('cart')
        return redirect('login')
     
def add_movie_to_cart(request, slug):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, slug=slug)
        cart_item = ShoppingCartItem.objects.create(
            user=request.user,
            product_type='Filme',
            product_name=movie.title,
            product_price=movie.price,
            product_image=movie.img,
        )
    else:
        request.session['cart_redirect'] = reverse('add_movie_to_cart', args=[slug])
        return redirect('login')

    return redirect('movie_details', slug=slug)

def add_music_to_cart(request, slug):
    if request.user.is_authenticated:
        music = get_object_or_404(Music, slug=slug)
        cart_item = ShoppingCartItem.objects.create(
            user=request.user,
            product_type='Música',
            product_name=music.title,
            product_price=music.price,
            product_image=music.img,
        )
    else:
        request.session['cart_redirect'] = reverse('add_music_to_cart', args=[slug])
        return redirect('login')

    return redirect('music_details', slug=slug)

def add_game_to_cart(request, slug):
    if request.user.is_authenticated:
        game = get_object_or_404(Game, slug=slug)
        cart_item = ShoppingCartItem.objects.create(
            user=request.user,
            product_type='Jogo',
            product_name=game.title,
            product_price=game.price,
            product_image=game.img,
        )
    else:
        request.session['cart_redirect'] = reverse('add_game_to_cart', args=[slug])
        return redirect('login')

    return redirect('game_details', slug=slug)
