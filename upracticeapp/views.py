from django.shortcuts import render

# Create your views here.
from upracticeapp.models import Upractice

def upractice_main(request):
    return render(request, "upracticeapp/upractice_main.html")

def upractice_first(request):
    try:
        if request.method == "GET":
            utitle = request.GET.get('utitle')
            ucontent = request.GET.get('ucontent')
            uresult = request.GET.get('uresult')
            print(utitle, ucontent, uresult, len(ucontent))

            upractice_data = Upractice()
            upractice_data.upractice_title= utitle
            upractice_data.upractice_content = ucontent
            upractice_data.upractice_result = uresult
            upractice_data.upractice_chnum = len(ucontent)
            upractice_data.save()

            context = {'utitle': utitle, 'ucontent': ucontent, 'uresult': uresult}

            return render(request, "upracticeapp/upractice_main.html", context)

    except Exception as identifier:
        print(identifier)

    return render(request, "upracticeapp/upractice_first.html")