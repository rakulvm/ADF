from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contact/', views.contact,name='contact'),
    # path('news/',views.news,name='news'),
    path('result/',views.result, name='result'),
    path('forms/',views.add_func, name='forms'),
    path('user/',views.user,name='user')
]