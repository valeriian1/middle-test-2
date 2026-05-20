from django.shortcuts import render
from .models import Recipe
from . import config


def main(request):
    """
    Renders the main page with a random selection of recipes.
    Fetches up to random limit recipes dynamically.
    """
    recipes = Recipe.objects.order_by('?')[:config.RANDOM_RECIPES_LIMIT]
    return render(request, config.MAIN_TEMPLATE, {'recipes': recipes})
