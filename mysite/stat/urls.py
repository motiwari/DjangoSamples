from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^stat/', views.index, name='index'),
]