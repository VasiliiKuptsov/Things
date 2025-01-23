from django.shortcuts import render, get_object_or_404
from products.models import Product
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object=super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object

    #def get_context_data(self, **kwargs):
     #   context = super().get_context_data(**kwargs)
      #  post = self.get_object()
       # post.views_count += 1
        #post.save()
       # context['title'] = post.title
        #return context


class ProductCreateView(CreateView):
    model = Product
    fields =('name', 'description', 'image', 'category', 'price', 'updated_at')
    success_url = reverse_lazy('products:products_list')


class  ProductUpdateView(UpdateView):

    model = Product
    fields = ('name', 'description', 'image', 'category', 'price', 'updated_at')
    success_url = reverse_lazy('products:products_list')

    def get_success_url(self):
        return reverse('products:products_detail', args=[self.kwargs.get('pk')])

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products:products_list')





