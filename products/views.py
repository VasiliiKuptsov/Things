from django import forms
from django.shortcuts import render, get_object_or_404
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

class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('views_counter', 'owner')
        context_object_name = 'products'



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
        return ProductModeratorForm#PermissionDenied




class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products:products_list')


class ProductsSearchView(FormView):


    form_class = ProductsSearchForm
    template_name = 'products_search.html'


    def form_valid(self, form):
        category_id = form.cleaned_data["category"]
        #category_id = 2
        #cleaned_data = super().form_valid(form)
       # if not form.is_valid():
        #     return redirect('products:products_detail')
        #category_id = form.choice_category()
        print(category_id)
        return super().form_valid(form)


class ProductCategoryListView(ListView):

    model = Product
    template_name = 'products/products_category.html'
    context_object_name = 'products'



    def get(self, request, *args, **kwargs):
        form = ProductsSearchForm(request.GET)
        if form.is_valid():
            category_id = int(form.cleaned_data['category'])
            print((category_id))


            return self.get_queryset(category_id)
        else:
            return render(request, self.template_name, {'form': form})


    def get_queryset(self, category_id):


        #category_id = self.kwargs.get('category')#category_id
        print(f'gegqgg {category_id}')
        if category_id:
            return get_product_from_category(category_id=category_id)
        else:
            return get_product_from_category(category_id=category_id)#Product.objects.none()

    #def get(self, request, *args, **kwargs):
     #   form = ProductsSearchForm()
      #  return render(request, self.template_name, {'form': form, 'products': self.get_queryset()})


'''  
    def post(self, request, *args, **kwargs):
        form = ProductsSearchForm(request.POST)
        print(cleaned_data)
        #if form.is_valid():
        category_id = form.cleaned_data['category']
        print((category_id))
        return self.get_queryset(category_id)
        #else:
        return  self.get_queryset(category_id)#render(request, self.template_name, {'form': form})

'''












