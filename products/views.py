from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .form import ProductForm, RawProductForm
# Create your views here.


#pure django form

# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             #now it is good data
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request, "product_create.html", context)
#


# #for raw form
# def product_create_view(request):
#     #print(request.GET)
#     #print(request.POST)
#
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         #Product.objects.create(title=my_new_title) here uncomment will save dat abut first data is null
#         print(my_new_title)
#     context = {}
#     return render(request,"product_create.html", context);


#for django form
def product_create_view(request):
    initial_data = {
        'title': "This is awesome title"
    }
    obj = Product.objects.get(id=2)
    form = ProductForm(request.POST or None, initial=initial_data)
    #form = ProductForm(request.POST or None, instance=obj)#by this id 2 obj data can be rendered and then updatede
    if form.is_valid():
        form.save()
        form = ProductForm()# re render

    context = {
        'form' : form
    }
    return render(request,"product_create.html",context)




def product_detail_view(request,id):
    obj = get_object_or_404(Product,id=id)
    # context = {
    #     'title':obj.title,
    #     'description': obj.description
    # }

    context ={
        'object' : obj
    }
    return render(request, "detail.html", context)


def dynamic_lookup_view(request,my_id):
    #obj = Product.objects.get(id=my_id)
    obj = get_object_or_404(Product, id=my_id)
    context = {
        "object": obj
    }
    return render(request, "detail.html",context)


def product_delete_view(request,my_id):

    obj = get_object_or_404(Product, id=my_id)

    #if post request then deleted
    if request.method == "POST":
        obj.delete()
        return redirect('/about')
    context = {
        "object": obj
    }
    return render(request, "delete.html",context)


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }

    return render(request, "product_list.html", context)


def product_update_view(request,my_id=id):
    obj = get_object_or_404(Product, id=my_id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request,"product_create.html",context)