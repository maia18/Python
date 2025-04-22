from django.shortcuts import render
# from django.http import HttpResponse

def blog(request):
    print('blog')
    # return HttpResponse('blog do app')
    context = {
            'text': 'Olá blog'
    }
    
    return render(
        request, 
        'blog/index.html',
        context,
    )
    
def exemplo(request):
    print('exemplo')
    # return HttpResponse('exemplo do app')
    context = {
            'text': 'Olá exemplo',
            'title': 'PÁGINA DE EXEMPLO - ',
    }
    
    return render(
        request, 
        'blog/exemplo.html',
        context,
    )