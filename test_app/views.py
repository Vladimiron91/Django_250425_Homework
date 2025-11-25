from django.http import HttpResponse


def home_page(request):
    return HttpResponse("Hello from our first endpoint!!!!!")

# Create your views here.
