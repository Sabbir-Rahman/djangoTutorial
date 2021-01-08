from django.shortcuts import render
from .models import Product
from .form import ProductForm
# Create your views here.




#for raw form
def product_create_view(request):
    context = {}
    return render(request,"product_create.html", context);

# #for django form
# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()# re render
#
#     context = {
#         'form' : form
#     }
#     return render(request,"product_create.html",context)
#



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


