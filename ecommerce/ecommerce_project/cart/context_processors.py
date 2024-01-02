from . models import Cart,CartItem
from . views import __cart_id

def counter(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart=Cart.objects.filter(cart_id=__cart_id(request))
            cart_item=CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_item:
                item_count += cart_item.quantity
        except Cart.DoesNotExist:
            item_count = 0
    return dict(item_count = item_count)