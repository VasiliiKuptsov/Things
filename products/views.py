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

#def products_list(request):
#    products = Product.objects.all()
 #   context = {'products<object_list>': products}
#    return render(request, 'products_list.html', context)


#def products_detail(request, pk):
 #   product = get_object_or_404(Product, pk=pk)
  #  context = {'product': product}
   # return render(request, 'product_detail.html', context)



