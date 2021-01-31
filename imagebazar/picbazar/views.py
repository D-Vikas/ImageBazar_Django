from django.shortcuts import render , redirect
from django.http import HttpResponse
from picbazar.models import *
# Create your views here.

def home(request):
    return redirect('/home')

def show_home_page(request):

    cat = Category.objects.all()
    image = Image.objects.all()
    data = {'images':image,'cats':cat}
    return render(request,"home.html",data)



def show_category_page(request, cid):

    cat = Category.objects.all()
    get_cat = Category.objects.get(pk=cid)

    image = Image.objects.filter(cat = get_cat)
    data = {'images':image,'cats':cat}
    return render(request,"home.html",data)
