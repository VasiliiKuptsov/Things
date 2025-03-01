from django import forms
from django.core.cache import cache
from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, FormView
from products.forms import ProductForm, StyleFormMixin, ProductsSearchForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProductModeratorForm
from django.core.exceptions import PermissionDenied
from django.forms import forms
from products.services import get_product_from_category
from django.views import View
from django import forms
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator



class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('views_counter', 'owner')
        context_object_name = 'products'



class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return get_products_from_cache()



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





class  ProductUpdateView(LoginRequiredMixin, UpdateView):

    model = Product
    form_class = ProductForm
    #fields = ('name', 'description', 'image', 'category', 'price', 'updated_at')
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('products:products_list')

    def get_success_url(self):
        return reverse('products:products_detail', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        user = self.request.user
        if user ==self.object.owner:
            return ProductForm
        if user.has_perm('products.can_publication_product'):
            return ProductModeratorForm
        return ProductModeratorForm




class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products:products_list')


class ProductsSearchView(FormView):


    form_class = ProductsSearchForm
    template_name = 'products_search.html'


    def form_valid(self, form):
        category_id = int(form.cleaned_data["category"])

        return redirect('products:products_category', category_id=category_id)#super().form_valid(form)


class ProductCategoryListView(ListView):

    model = Product
    template_name = 'products/products_category.html'
    context_object_name = 'products'




    def get_queryset(self):


        category_id = self.request.GET.get('category')  # Получите category из GET-запроса
        print(f'gegqgg {category_id}')

        if category_id:
            return get_product_from_category(category_id)
        else:
            return Product.objects.none()




    def get(self, request, *args, **kwargs):
        form = ProductsSearchForm()  # Создаем форму для поиска
        products = self.get_queryset()  # Получаем список продуктов по категории
        return render(request, self.template_name, {'form': form, 'products': products})















