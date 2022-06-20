from django.shortcuts import render
from .models import Menu


def blog(request):
    menulist = Menu.objects.all()
    return render(request,'app/blog.html', {'menulist':menulist})

