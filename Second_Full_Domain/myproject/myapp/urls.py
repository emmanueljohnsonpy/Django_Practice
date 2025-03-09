from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name="hello"),
    path('hai/', views.hai, name="hai"),
    path('loop/', views.loop, name="loop"),
    path('context/', views.context, name="context"),
    path('my_view', views.status_code, name="my_view")
]
