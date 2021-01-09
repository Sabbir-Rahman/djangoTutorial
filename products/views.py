from django.shortcuts import render
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




def product_detail_view(request):
    obj = Product.objects.get(id=2)
    # context = {
    #     'title':obj.title,
    #     'description': obj.description
    # }

    context ={
        'object' : obj
    }
    return render(request, "detail.html", context)


