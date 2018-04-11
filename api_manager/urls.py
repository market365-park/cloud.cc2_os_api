from django.urls import path

from api_manager import views

urlpatterns = [
    path('', views.index, name='api_index'),
    path('stack', views.stack, name='stack_api'),
]


