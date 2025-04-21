from django.shortcuts import render
# from django.http import HttpResponse

def blog(request):
    print('blog')
    # return HttpResponse('blog do app')
    
    return render(
        request, 
        'blog/index.html'
    )
    
def exemplo(request):
    print('exemplo')
    # return HttpResponse('exemplo do app')
    
    return render(
        request, 
        'blog/exemplo.html'
    )