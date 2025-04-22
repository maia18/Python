from django.shortcuts import render
# from django.http import HttpResponse

def home(request):
    print('home')
    # return HttpResponse('home do app')
    context = {
            'text': 'Olá home'
    }
    
    return render(
        request, 
        'home/index.html',
        context,    
    )
