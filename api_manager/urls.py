from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='api_index'),
    path('stack', views.stack, name='stack_api'),
]
