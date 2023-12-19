from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)

from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    engrave_text = ""
    engrave_message = ""
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    if 'engrave_text' in request.POST and 'engrave_checkbox' in request.POST:
        engrave_text = request.POST['engrave_text'] 
        engrave_message = (f' engraved with ({engrave_text}) ')
    size_only = size
    if size and engrave_text:
        size = size_only + "_" + engrave_text
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                # same size and same engraving already in bag
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(request,
                                (f'Updated quantity of {product.name} Size: {size_only.upper()}'
                                f'{engrave_message} to {bag[item_id]["items_by_size"][size]}'
                                ))
            else:
                # add to bag : product already in bag but new size &/or engraving (new key)
                bag[item_id]['items_by_size'][size] = quantity 
                messages.success(request,
                                 (f'Added {product.name}'
                                  f' Size : {size_only.upper()}'
                                  f' to your bag {engrave_message}'))
        else:
            # Product not in bag until now 
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request,
                                (f'Added {product.name}'
                                 f' Size : {size_only.upper()}'
                                 f' to your bag {engrave_message}'))
                          
    else:
        # Product without sizing or engraving
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request,
                             (f'Updated {product.name} '
                              f'quantity to {bag[item_id]}'))
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
        if "_" in size:
            engrave_split = size.split('_')
            size_only = engrave_split[0]
        else:
            size_only = size
                
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(
                request, f'Changed quantity of {product.name} Size {size_only.upper()}\
                    to {bag[item_id]["items_by_size"][size]}'
                    )
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(
                request, f'Removed {product.name} Size {size_only.upper()} \
                    from your bag'
                    )
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    product = get_object_or_404(Product, pk=item_id)
    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})
        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(
                request, f'Removed {product.name} Size {size.split("_")[0].upper()} \
                    from your bag'
                    )
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
