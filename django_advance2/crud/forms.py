from django import forms
from .models import Goods

class GoodsCreateForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ('name', 'management_code', 'price', 'release_data', 'release_flag', 'description', 'image')