from django.shortcuts import render, get_object_or_404
from products.models import Product
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from products.forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin
class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):

    model = Product

    def get_object(self, queryset=None):
        self.object=super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object



class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('products:products_list')

    def form_valid(self, form):
        product=form.save()
        user=self.request.user
        product.owner=user
        product.save()
        return super().form_valid(form)




class  ProductUpdateView(UpdateView):

    model = Product
    form_class = ProductForm
    #fields = ('name', 'description', 'image', 'category', 'price', 'updated_at')
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('products:products_list')

    def get_success_url(self):
        return reverse('products:products_detail', args=[self.kwargs.get('pk')])

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products:products_list')






