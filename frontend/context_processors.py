from users.models import ShoppingCartItem

def amount_cart(request):
    try:
        cart_items = ShoppingCartItem.objects.filter(user=request.user, purchase_date__isnull=True)
        return {'amount_cart': cart_items.count()}
    except:
        return {'amount_cart': 0}