from django.contrib import admin
from django.urls import path
from app_promo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.Login, name='login'),
    path('', views.index, name='index'),
    path('notebook/', views.notebook, name='notebook'),
    path('contato/', views.contato, name='contato')
]
