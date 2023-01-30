from django.urls import path
from tutorialapp import views

urlpatterns = [
    path('', views.index),
    path('h',views.html),
    path('c',views.css),
    path('j',views.js),
    path('p',views.python),
    path('hd',views.htmldetail),
    path('cd',views.cssdetail),
    path('pd',views.pythondetail)

]