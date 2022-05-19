from django.shortcuts import render

# Create your views here.
def first_game(request):
    return render(request, "gameapp/first_game.html")
