from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Product, Cart
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


# Create your views here.
#To render Home Page at time of Launch of Program
def index(request):
    phones = Product.objects.filter(category='Tires')
    chargers = Product.objects.filter(category='Rims')
    context = {'products': list(phones)}

    if 'message' in request.session:
        context['message'] = request.session['message']
        del request.session['message']

    return render(request, 'index.html', context)

#To render Tires Page at nav click

def phones(request):
    products = Product.objects.filter(category='Tires')
    return render(request, 'tires.html', {'products': products})

#To render RIms Page at nav click
def accessories(request):
    products = Product.objects.filter(category='Rims')
    return render(request, 'rims.html', {'products': products})

#To render Search Page on Search bar Search Action
def search(request):
    query = request.GET.get('q')
    products = Product.objects.filter(title__icontains=query)
    context = {'products': products}
    return render(request, 'search.html', context)



# TO Show Cart Items on Cart Page
def show_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum([item.product.price for item in cart_items])
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

# TO Clear Cart Item on Cart Page
def clear_cart(request):
    Cart.objects.filter(user=request.user).delete()
    return redirect(show_cart)
# TO add  Item to Cart
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')

        product = get_object_or_404(Product, id=product_id)
        
        cart = Cart.add_to_cart(request.user, product)
        

        if cart:
            return JsonResponse({'status': 'success', 'cart_id': cart.id})
        else:
            return JsonResponse({'status': 'error', 'message': 'Failed to Add Project'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})
