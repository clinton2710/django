from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import product
from .forms import productforms, RawProductForm
# Create your views here.

# def product_list_view(request):
#     queryset = product.objects.all() #list of objects
#     context = {
#         "object_list":queryset
#     }
#     return render(request, "products/products_list.html", context)
# #dynamic url
# def dynamic_lookup_view(request, my_id):
#     # try: obj = product.objects.get(id=my_id)
#     # except product.DoesNotExist:
#     #     raise Http404
#     obj = product.objects.get(id= my_id)
#     # obj = get_object_or_404(product,id=my_id)
#     # #POST request
#     # if request.method == "POST":
#     #     #confirming delete
#     #     obj.delete()
#     #     return redirect('../../')
#     context = {
#         'object': obj
#         }
#     return render(request, "products/products_detail.html", context)

    
# def render_initial_data(request):
#     initial_data = {
#         'title': "My title is awsome"
#     }
#     obj = product.objects.get(id=15)
#     form = productforms(request.POST or None, instance=obj)
#     if form.is_valid():
#         form.save()
#     context = {
#         'form': form
#     }
#     return render(request, "products/products_create.html", context)
# def product_detial_view(request, id):
#     obj = product.objects.get(id= my_id)
#     # context = {
#     #     'title': obj.title,
#     #     'description': obj.description
        
#     # }
#     context = {
#         'object': obj
#     }
#     return render(request,"products/products_detail.html", context)
# #form validation
# def product_create_view(request):
#         my_form = RawProductForm()
#         if request.method == "POST":
#             my_form = RawProductForm(request.POST)
#             if my_form.is_valid():
#                 #now the data is good 
#                 product.objects.create(**my_form.cleaned_data)
#         context ={
#             "form": my_form
#         }
#         return render(request, "products/products_create.html", context)


# def product_create_view(request):
#     if request.method =="POST":
#         title = request.POST.get('title')
#     context ={}
#     return render(request, "products/products_create.html", context)

# def product_create_view(request):
#     form = productforms(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = productforms()
#     context = {
#         'form': form
#     }
#     return render(request,"products/products_create.html", context)