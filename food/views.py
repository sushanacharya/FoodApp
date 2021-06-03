from food.addforms import ItemForm
from django import forms, template
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Item
from django.template import context, loader

# Create your views here.
def index(request):
    item_list= Item.objects.all()
    template= loader.get_template('food/index.html')
    context={
        'itemList': item_list,
    }
    return HttpResponse(template.render(context, request))                                                                                                                                                                                                                                       

def item(request):
    return HttpResponse('Hello to the item! O_O ')


def detail(request, itemId):
    item= Item.objects.get(pk=itemId)
    context={
        'item': item,
   
    }
    template= loader.get_template('food/detail.html')
    #return HttpResponse('this is the id %s' %itemId)
    return render(request, 'food/detail.html', context)

def addItem(request):
    form= ItemForm(request.POST or None)
    #validation
    if form.is_valid():
        form.save()
        return redirect('food:index')

    template= loader.get_template('food/addItem.html')
    return HttpResponse(template.render({'form':form}, request))

def updateItem(request, itemId):
    item= Item.objects.get(id=itemId);
    #iniialize form and pass the data of selected item to the form
    form= ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save();
        return redirect('food:index')

    #load templete and return on single line
    return render(request, 'food/addItem.html', {'form':form, 'item':item})

def deleteItem(request, itemId):
    item= Item.objects.get(id=itemId);
    
    #if request.method== 'POST':
    item.delete();
    return redirect ('food:index')

    #return HttpResponse('Deleted!')
    #added this ro directly delte the item
