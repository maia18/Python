from blog import views
from django.urls import path

app_name = 'blog'

# blog/
# Django URLs: https://docs.djangoproject.com/en/5.2/topics/http/urls/
urlpatterns = [
    path('<int:post_id>/', views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo'),
    path('', views.blog, name='home'),
]