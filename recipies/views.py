from django.shortcuts import render

def recipies_list_view(request):
    return render(request, 'recipies/recipies_list.html')


def recipies_category_list_view(request):
    return render(request, 'recipies/recipes.html')