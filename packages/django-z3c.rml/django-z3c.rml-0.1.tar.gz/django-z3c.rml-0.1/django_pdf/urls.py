from django.urls import path

from . import views

app_name = 'pdf'
urlpatterns = [
    path('', views.pdf),
    path('din5008', views.din5008),
]
