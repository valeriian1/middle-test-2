from django.shortcuts import render, get_object_or_404
from .models import Recipe, Category
from . import config


def main(request):
    """
    Renders the main page with a random selection of recipes.
    Fetches up to random limit recipes dynamically.
    """
    recipes = Recipe.objects.order_by('?')[:config.RANDOM_RECIPES_LIMIT]
    return render(request, config.MAIN_TEMPLATE, {'recipes': recipes})


def category_detail(request, pk):
    """
    Renders recipes belonging to a specific category.
    """
    category = get_object_or_404(Category, pk=pk)
    return render(request, config.CATEGORY_DETAIL_TEMPLATE, {'category': category})
