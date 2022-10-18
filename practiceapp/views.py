import random
import json
from urllib import parse

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.urls import resolve

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
            i = Language.objects.get(pk=1)
            practice_lang = Practice.objects.filter(code_language=i)
            practice_list = list(practice_lang)
            random_practice = random.choice(practice_list)
            practice_select = Practice.objects.filter(pk=random_practice.practice_id)
            print(practice_select)
            # practice = serializers.serialize('json', practice_select)
            # print(practice)
            # print(type(practice))
            # practice_data = Practice.objects.values()
            # practice_data = list(practice_data)
            # practice_data = practice_data[0]
            # print(practice_data)
            # print(type(practice_data))
            # jpractice_data = json.dumps(practice_data)
            # print(jpractice_data)
            # print(type(jpractice_data))

            context = {'l':l, 'practice_select':practice_select}
            return render(request, 'practiceapp/practice_second.html', context)


        elif 'css' in request.GET:
            l = Language.objects.filter(language='css')
            i = Language.objects.get(pk=2)
            practice_lang = Practice.objects.filter(code_language=i)
            practice_list = list(practice_lang)
            random_practice = random.choice(practice_list)
            practice_select = Practice.objects.filter(pk=random_practice.practice_id)
            print(practice_select)

            context = {'l': l, 'practice_select': practice_select}
            return render(request, 'practiceapp/practice_second.html', context)


        elif 'html' in request.GET:
            l = Language.objects.filter(language='html')
            i = Language.objects.get(pk=3)
            practice_lang = Practice.objects.filter(code_language=i)
            practice_list = list(practice_lang)
            random_practice = random.choice(practice_list)
            practice_select = Practice.objects.filter(pk=random_practice.practice_id)
            print(practice_select)
            context = {'l': l, 'practice_select': practice_select}
            return render(request, 'practiceapp/practice_second.html', context)


        elif 'javascript' in request.GET:
            l = Language.objects.filter(language='javascript')
            i = Language.objects.get(pk=4)
            practice_lang = Practice.objects.filter(code_language=i)
            practice_list = list(practice_lang)
            random_practice = random.choice(practice_list)
            practice_select = Practice.objects.filter(pk=random_practice.practice_id)
            print(practice_select)
            context = {'l': l, 'practice_select': practice_select}
            return render(request, 'practiceapp/practice_second.html', context)

        return render(request, 'practiceapp/practice_second.html')



def result(request):
    print("result 실행")
    user = request.user
    TIME = request.GET.get('TIME')
    score = request.GET.get('score')
    miss = request.GET.get('miss')
    print(TIME,score,miss,user)
    context = {'TIME': TIME, 'score': score, 'miss':miss, 'user':user}
    return render(request, 'practiceapp/practice_result.html', context)

    # time = request.GET.get('TIME')
    # score = request.GET.get('score')
    # miss = request.GET.get('miss')
    # print("시간",time,"스코어",score,"미스",miss)
    # sendData = request.GET.get('TIME')
    # print(sendData)
    # return JsonResponse(data={})
    # return render(request, 'practiceapp/practice_result.html')

