from django import forms
from .models import Review, Product
from haystack.forms import SearchForm


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'image', 'inventory']



class SearchForm(forms.Form):
    query = forms.CharField(label='Search')
