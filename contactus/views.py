from django.shortcuts import render, redirect
from .forms import ContactUsForm
# Create your views here.


def contact_us(request):

    """ View function for the contact us form """

    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactUsForm()

    context = {
        'form': form
    }

    return render(request, 'contactus/contactus.html', context)


def contact_success(request):

    """ Render the Contact Success HTML page """

    return render(request, 'contactus/contact_success.html')