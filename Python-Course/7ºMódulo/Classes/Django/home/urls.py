from django.urls import path

from home import views as hv # hv = home views

urlpatterns = [
    path('', hv.home),
]
