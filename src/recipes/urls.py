from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("recipes/overview/", views.combined_charts_overview, name="recipe_overview"),
    path("recipes/combined-charts/", views.combined_charts_overview, name="combined_charts_overview"),
    path("recipes/<int:pk>/", views.recipe_detail, name="recipe_detail"),
    path("search/", views.search_results, name="search_results"),
    path("all_recipes/", views.show_all_recipes, name="show_all_recipes"),
    path("about_me/", views.about_me, name="about_me"),
]
