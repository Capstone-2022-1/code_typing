from django.shortcuts import render

# Create your views here.
def practice_first(request):
    return render(request, "practiceapp/practice_first.html")
