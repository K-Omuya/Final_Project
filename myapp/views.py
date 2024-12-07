from .models import Item

from django.shortcuts import render, get_object_or_404, redirect
from .models import Blogpost


# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contacts(request):
    return render(request,'contacts.html')

def services(request):
    return render(request,'sevices.html')

def base(request):
    return render(request,'base.html')

def bloglist(request):
    posts=Blogpost.objects.all()
    return render(request, 'blog_list.html',{'posts':posts})

def blog_detail(request, id):
    post=get_object_or_404(Blogpost,id=id)
    return render(request,'blog_detail.html',{'post':post})
#
# # CRUD
# # CREARE
# def create_item(request):
#     if request.method=='POST':
#         name=request.POST.get('name')
#         description=request.POST.get('description')
#         Item.objects.create(name=name,description=description)
#         return redirect('item_list')
#     return render(request,'item_form.html')
#
# # READ
#
# def item_list(request):
#     items=Item.objects.all()
#     return render(request,'item_list.html',{'items':items})
#
#
#
# # UPDATE
# def update_item(request,pk):
#     item=get_object_or_404(Item,pk=pk)
#     if request.method=='POST':
#         item.name=request.POST.get('name')
#         item.description=request.get('description')
#         item.save()
#         return redirect(item_list)
#     return render(request,'item_form.html',{'item':item})
#
# # DELETE
# def delete_item(request,pk):
#     item=get_object_or_404(Item,pk=pk)
#     if request.method=='POST':
#         item.delete()
#         return redirect('item_list')
#     return render(request,'confirm_delete.html',{'item':item})
#
#
#
#
