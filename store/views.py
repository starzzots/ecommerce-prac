from django.shortcuts import render

# Create your views here.

def store(request):
    content={

    }
    return render(request, 'store/store.html',content)

def checkout(request):
    content={

    }
    return render(request, 'store/checkout.html',content)

def cart(request):
    content={

    }
    return render(request, 'store/cart.html',content)

def main(request):
    content={

    }
    return render(request, 'store/main.html',content)
