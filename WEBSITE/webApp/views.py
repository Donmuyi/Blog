from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'webApp/home.html')


def about(request):
    from webApp.namer import bob
    return render(request, 'webApp/about.html', {"my_stuff": bob})


def contact(request):
    return render(request, 'webApp/contact.html')


def pricing(request):
    return render(request, 'webApp/pricing.html')


def dailyquotes(request):
    return render(request, 'webApp/dailyquotes.html')


def news(request):
    return render(request, 'webApp/news.html')


def religion(request):
    return render(request, 'webApp/religion.html')


def food(request):
    return render(request, 'webApp/food.html')


def sports(request):
    return render(request, 'webApp/sports.html')


def fashion(request):
    return render(request, 'webApp/fashion.html')


