from itertools import product
from unicodedata import category
from django.shortcuts import get_object_or_404, render
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator,InvalidPage,EmptyPage

# Create your views here.
def home(request,c_slug=None):
    c_page=None
    prod=None
    if c_slug!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        prod=product.objects.filter(category=c_page,available=True)
    else:
       
        prod=product.objects.all().filter(available=True)
    cat=categ.objects.all()    
    paginator=Paginator(prod,4)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_page)        
    return render(request,'index.html',{'pr':prod,'ct':cat,'pg':pro})

def prodetails(request,c_slug,product_slug):
    try:
        prod=product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'item.html',{'pr':prod})    

def searching(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=product.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
        
    return render(request,'search.html',{'q':query,'pr':prod})