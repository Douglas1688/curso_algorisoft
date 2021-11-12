from django.forms import ModelForm
from erp.models import *

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        