from django import forms
from .models import Category, Ovqat


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class OvqatForm(forms.ModelForm):
    class Meta:
        model = Ovqat
        fields = "__all__"





