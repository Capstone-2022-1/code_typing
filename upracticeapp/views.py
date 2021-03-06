from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from upracticeapp.models import Upractice


def upractice_main(request, pk):
    uall = Upractice.objects.filter(writer=pk) # main에서 들어오는 Upractice의 모든 값을 uall에 저장
    context = {'uall': uall}
    return render(request, "upracticeapp/upractice_main.html", context)

def upractice_first(request):
    try:
        if request.method == "POST":
            utitle = request.POST.get('utitle')
            ucontent = request.POST.get('ucontent')
            uresult = request.POST.get('uresult')
            print(utitle, ucontent, uresult, len(ucontent))

            upractice_data = Upractice()
            upractice_data.upractice_title = utitle
            upractice_data.upractice_content = ucontent
            upractice_data.upractice_result = uresult
            upractice_data.upractice_chnum = len(ucontent)
            upractice_data.writer = request.user
            upractice_data.save()
            print(upractice_data)

            uall = Upractice.objects.all()  # main에서 들어오는 Upractice의 모든 값을 uall에 저장
            context = {'uall': uall}

            return render(request, "upracticeapp/upractice_main.html", context)

    except Exception as identifier:
        print(identifier)

    return render(request, "upracticeapp/upractice_first.html")

def upractice_second(request, upractice_id):
            g = Upractice.objects.get(pk=upractice_id)
            context = {'g': g}
            print(g)
            return render(request, "upracticeapp/upractice_second.html", context)