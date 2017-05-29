from .models import Product, Category
from .forms import AddProductForm
from django.shortcuts import resolve_url, redirect
from django.views.generic import ListView, CreateView


class ProductListView(ListView):

    model = Product
    template_name = 'product_list.html'
    cat = None

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context["cats"] = Category.objects.all()
        context["category"] = self.cat
        return context

    def get(self, request, *args, **kwargs):
        if self.kwargs["cat"]:
            self.cat = Category.objects.get(pk=self.kwargs["cat"])
        return super(ProductListView, self).get(request, *args, **kwargs)
    
    def get_queryset(self):
        if self.kwargs["cat"] == None:
            return Product.objects.all()
        return Product.objects.filter(category=self.cat)


class AddProductView(CreateView):
    
    form_class = AddProductForm
    template_name = 'add_product.html'

    def form_valid(self, form):
        return super(AddProductView, self).form_valid(form)
    
    def get_success_url(self):
        return resolve_url('home')
