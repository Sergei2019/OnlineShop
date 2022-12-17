from django.shortcuts import render


def store_view(request):
    context = {}
    return render(request, 'store.html')

def cart_view(request):
    context = {}
    return render(request, 'cart.html')


def main_view(request):
    context = {}
    return render(request, 'main.html')




