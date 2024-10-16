from django.urls import path
from . import views

urlpatterns = [
    path('', views.code_list, name='code_list'),
    path('code/<int:code_id>/', views.code_detail, name='code_detail'),
    path('code/<int:code_id>/draw/', views.code_draw, name='code_draw'),
    path('code/submit/', views.code_submit, name='code_submit'),
    path('code/<int:code_id>/delete/', views.code_delete, name='code_delete'),
]
