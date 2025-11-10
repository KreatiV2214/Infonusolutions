from django.urls import path
from app import views
from .views import index, Store
urlpatterns=[
    path('',views.index,name='index'),
    path('store',views.Store, name='Store'),
    path('contact',views.contact, name='contact'),
    path('login',views.login, name='login'),
    path('signup',views.signup, name='signup'),
]