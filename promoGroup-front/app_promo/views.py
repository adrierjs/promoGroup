from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        email = request.POST.get('email')
        first_name = request.POST.get('nome')
        password = request.POST.get('password')

        result = User.objects.filter(username=username).first()
        if result:
            messages.error(request, "Este email já está cadastrado. Tente outro ou faça login.",extra_tags='username_in_use')
        else:
            user = User.objects.create_user(username=username,
                                            email=email,
                                            first_name=first_name,
                                            password=password)
            user.save()
            messages.error(request, "Usuário cadastrado com sucesso",extra_tags='cadastro_feito')
    return render(request, "cadastro.html")

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password') 

        user = authenticate(username=username, password=password)
        if user is not None:
            print('entrou')
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválidos",extra_tags='login_incorreto')
    return render(request,'login.html')

def redefinir_email(request):
    if request.method == 'POST':
        email = request.POST.get('email').strip()
        print(email)
        try:
            usuario = User.objects.get(email=email)
            if usuario is not None:
                usuario.token_confirmation = User.generate_token_confirmation(32)
                usuario.token_expiration_date = User.generate_token_expiration_date(15)
                usuario.save()

                User.send_email_redefinicao_senha(request, usuario.token_confirmation, usuario.email)
        except User.DoesNotExist:
            messages.error(request, 'Usuário inexistente.')
    return render(request, 'redefinir_email.html')

@login_required(login_url='/login/')
def index(request):
    user = User.objects.get(username=request.user)
    return render(request, 'index.html', {'user': user})

def logout_user(request):
    logout(request)
    return redirect('/')



def notebook(request):
    return render(request,'notebook.html')

def contato(request):
    return render(request,'contato.html')