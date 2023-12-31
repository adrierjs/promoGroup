from django.contrib import admin
from django.urls import path
from app_promo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.Login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.index, name='index'),
    path('notebook/', views.notebook, name='notebook'),
    path('redefinir_email/', views.redefinir_email, name='redefinir_email'),
    path('contato/', views.contato, name='contato'),
    path('geladeira/', views.geladeira, name='geladeira'),
    path('tv/', views.tv, name='tv'),
    path('livro/', views.livro, name='livro'),
    path('ar_condicionado/', views.ar_condicionado, name='ar_condicionado')
]