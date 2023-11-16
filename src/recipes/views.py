from django.shortcuts import render


def home(request):
    return render(request, "app/recipes_home.html")
