from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.'
                )
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    order_date = order.date
    ddmmmyy = order_date.strftime("%d %b %Y")

    messages.warning(request, (
        f'This is a COPY of confirmation for order number {order_number}.',
        f'An email with these details was sent to you on the {ddmmmyy}'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


# Return list of email addresses for users who have subscribed to newsletter
def subscribed_users_list(request):
    subscribed_users = User.objects.filter(
        userprofile__subscribe_newsletter=True
        )
    email_list = ', '.join([user.email for user in subscribed_users])
    return render(
        request,
        'profiles/subscribed_users_list.html',
        {'email_list': email_list}
        )
