from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Orders
from math import ceil
# Create your views here.


def index(reguest):
    allproducts = []
    category = Product.objects.values('category')
    categories = {item['category'] for item in category}
    for categry in categories:
        products = Product.objects.filter(category=categry)
        nProducts = len(products)
        nSlides = nProducts // 4 + ceil((nProducts/4) - (nProducts // 4))
        allproducts.append([products, range(1, nSlides), nSlides])
    params = {
        'allproducts': allproducts
    }
    return render(reguest, 'shop/index.html', params)


def about(reguest):
    return render(reguest, 'shop/about.html')


def contact(reguest):
    if reguest.method == "POST":
        name = reguest.POST.get('name', '')
        email = reguest.POST.get('email', '')
        cell = reguest.POST.get('cell', '')
        desc = reguest.POST.get('desc', '')
        contact = Contact(name=name, email=email, cell=cell, desc=desc)
        contact.save()
    return render(reguest, 'shop/contact.html')


def search(reguest):
    return HttpResponse('You are at Search')


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + \
            " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'shop/checkout.html')


def tracker(reguest):
    return render(reguest, 'shop/tracker.html')


def products(reguest, qvid):
    product = Product.objects.filter(product_id=qvid)
    return render(reguest, 'shop/products.html', {'product': product[0]})
