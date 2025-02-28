from django import forms
from products.models import Product, Category


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'publication':
                field.widget.attrs['class'] = 'form-check-input'
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('views_counter', 'owner')
        context_object_name = 'products'

class ProductModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
            model = Product
            fields = ('publication', 'publication')
           # exclude = ('image', 'category', 'price', 'updated_at', 'views_counter', 'owner')

    def clean_name(self):
        stop_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        cleaned_data = super().clean()

        name = self.cleaned_data['name']

        for item in stop_list:
            if item in name.lower():
                raise forms.ValidationError(f'Слово "{item}" запрещено к использованию, выберите другоe')

        return name

    def clean_description(self):
        stop_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        cleaned_data = super().clean()

        description = self.cleaned_data['description']

        for item in stop_list:


            if item in description.lower():
                raise forms.ValidationError(f'Слово "{item}" запрещено к использованию, выберите другое')

        return description

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError('Отрицательная цена недопустима!')
        return price

class ProductsSearchForm(forms.Form):#ModelForm):
    category = forms.ChoiceField()

    class Meta:
        model = Product
        fields = ['category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].choices = [(category.id, category.name) for category in Category.objects.all()]


