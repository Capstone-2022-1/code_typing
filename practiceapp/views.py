from django.shortcuts import render

# Create your views here.
from practiceapp.models import Practice


def practice_first(request):
    return render(request, "practiceapp/practice_first.html")


def create_code(request):
    try:
        if request.method == "GET":
            if request.GET['lang'] in ['python', 'css', 'html', 'javascript']:
                language = request.GET['lang']
                content = request.GET.get('content')
                result = request.GET.get('result')
                source = request.GET.get('source')
                print(language,content,result,source,len(content))

                practice_data = Practice()
                practice_data.code_language = language
                practice_data.code_content = content
                practice_data.code_result = result
                practice_data.code_source = source
                practice_data.practice_chnum = len(content)
                practice_data.save()

                context = {'language':language, 'content':content, 'result':result, 'source':source}

                return render(request, "practiceapp/create_code.html", context)

            return render(request, "practiceapp/create_code.html")

    except Exception as identifier:
        print(identifier)

    return render(request, "practiceapp/create_code.html")

