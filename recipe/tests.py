from django.test import TestCase
from django.urls import reverse
from .models import Category, Recipe
from . import config


class RecipeTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Desserts")
        self.recipe1 = Recipe.objects.create(
            title="Syrnyky",
            description="Sweet cottage cheese pancakes",
            ingredients="Cottage cheese, eggs, flour, sugar",
            instructions="Mix ingredients, fry in butter",
            category=self.category
        )
        self.recipe2 = Recipe.objects.create(
            title="Varenyky",
            description="Dumplings with cherry",
            ingredients="Flour, water, cherry, sugar",
            instructions="Knead dough, boil dumplings",
            category=self.category
        )

    def test_category_iterator(self):
        recipes_from_iterator = list(self.category)
        self.assertIn(self.recipe1, recipes_from_iterator)
        self.assertIn(self.recipe2, recipes_from_iterator)
        self.assertEqual(len(recipes_from_iterator), 2)

    def test_main_view_status_and_template(self):
        response = self.client.get(reverse('recipe:main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, config.MAIN_TEMPLATE)

    def test_main_view_context_limit(self):
        for i in range(12):
            Recipe.objects.create(
                title=f"Test Recipe {i}",
                description="Test",
                ingredients="Test",
                instructions="Test",
                category=self.category
            )
        response = self.client.get(reverse('recipe:main'))
        recipes_in_context = response.context['recipes']
        self.assertEqual(len(recipes_in_context), config.RANDOM_RECIPES_LIMIT)

    def test_category_detail_view_success(self):
        response = self.client.get(reverse('recipe:category_detail', kwargs={'pk': self.category.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, config.CATEGORY_DETAIL_TEMPLATE)
        self.assertEqual(response.context['category'], self.category)

    def test_category_detail_view_not_found(self):
        response = self.client.get(reverse('recipe:category_detail', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, 404)
