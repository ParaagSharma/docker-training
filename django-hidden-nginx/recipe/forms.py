from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'name', 
            'description', 
            'ingredients', 
            'directions', 
            'minutes_taken', 
            'category', 
            'image'
        ]
