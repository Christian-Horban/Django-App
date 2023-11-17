from django.shortcuts import render
from .models import Recipe, Ingredient
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, "app/recipes_home.html")


@login_required
def recipe_overview(request):
    recipes = Recipe.objects.all()
    return render(request, "app/recipe_overview.html", {"recipes": recipes})


@login_required
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    difficulty = recipe.calculate_difficulty()
    return render(
        request, "app/recipe_detail.html", {"recipe": recipe, "difficulty": difficulty}
    )


@login_required
def search_by_ingredient(request):
    query = request.GET.get("query")
    if query:
        recipes = Recipe.objects.filter(ingredients__name__icontains=query).distinct()
    else:
        recipes = Recipe.objects.none()
    return render(request, "app/search_results.html", {"recipes": recipes})


@login_required
def search_results(request):
    query = request.GET.get("query", "")
    if query:
        ingredients = Ingredient.objects.filter(name__icontains=query)
        recipes = Recipe.objects.filter(ingredients__in=ingredients).distinct()
    else:
        recipes = Recipe.objects.none()

    return render(request, "search_results.html", {"recipes": recipes})
