from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51O6jetGQr6TYkHcZ08qfSDkaisfhUxuAVpx2wjyqXHmihTIQKddB1Xo0atZrww7xfwpwoFjBw5n5EigUjMecJQOd0028azmXvT',
        'client_secret': 'sk_test_51O6',
    }

    return render(request, template, context)
