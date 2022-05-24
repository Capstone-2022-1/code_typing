from random import random

from django.shortcuts import render

# Create your views here.
from practiceapp.models import Language, Practice


def practice_first(request):
    return render(request, "practiceapp/practice_first.html")

def practice_create(request):
    if request.method == "GET":
        lang = Language.objects.all()
        context = {'lang':lang}
        return render(request, "practiceapp/create_code.html", context)
    elif request.method == "POST":
        language_id = request.POST.get('language_id')
        content = request.POST.get('content')
        result = request.POST.get('result')
        source = request.POST.get('source')
        print(language_id, content, result, source, len(content))

        practice_data = Practice()
        practice_data.code_language = Language.objects.get(pk=language_id)
        practice_data.code_content = content
        practice_data.code_result = result
        practice_data.code_source = source
        practice_data.practice_chnum = len(content)
        practice_data.save()


        context = {'language_id': language_id, 'content': content, 'result': result, 'source': source}

        return render(request, "practiceapp/practice_first.html", context)
    return render(request, "practiceapp/practice_first.html")


def practice_second(request):
    if request.method == "GET":
        if 'python' in request.GET:
            l = Language.objects.filter(language='python')
            print(l)
            i = Language.objects.get(pk=1)
            print(i)
            p = Practice.objects.filter(code_language=i)
            context = {'l':l, 'p':p}
            return render(request, 'practiceapp/practice_second.html', context)
        return render(request, 'practiceapp/practice_second.html')





