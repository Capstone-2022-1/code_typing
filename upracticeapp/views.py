from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from upracticeapp.models import Upractice

def upractice_main(request):
    uall = Upractice.objects.all() # main에서 들어오는 Upractice의 모든 값을 uall에 저장
    context = {'uall': uall}
    return render(request, "upracticeapp/upractice_main.html", context)

def upractice_first(request):
    try:
        if request.method == "GET":
            utitle = request.GET.get('utitle')
            ucontent = request.GET.get('ucontent')
            uresult = request.GET.get('uresult')
            print(utitle, ucontent, uresult, len(ucontent))

            upractice_data = Upractice()
            upractice_data.upractice_title = utitle
            upractice_data.upractice_content = ucontent
            upractice_data.upractice_result = uresult
            upractice_data.upractice_chnum = len(ucontent)
            upractice_data.save()

            context = {'utitle': utitle, 'ucontent': ucontent, 'uresult': uresult}

            return render(request, "upracticeapp/upractice_main.html", context)

    except Exception as identifier:
        print(identifier)

    return render(request, "upracticeapp/upractice_first.html")

def upractice_second(request, upractice_id):
            g = Upractice.objects.get(pk=upractice_id)
            context = {'g': g}
            print(g)
            return render(request, "upracticeapp/upractice_second.html", context)