from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Collection


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        cat_friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        collections = Collection.objects.all()
        col_friendly_names = [(c.id, c.get_friendly_name()) for c in collections]

        self.fields['category'].choices = cat_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        self.fields['collection'].choices = col_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
