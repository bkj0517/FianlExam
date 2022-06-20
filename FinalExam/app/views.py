from django.shortcuts import render
from .models import Menu


def blog(request):
    menulist = Menu.objects.all()
    return render(request,'app/blog.html', {'menulist':menulist})

def posting(request, pk):
    menu = Menu.objects.get(pk=pk)
    return render(request, 'app/posting.htiml',{'menu':menu})