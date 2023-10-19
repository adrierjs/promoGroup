from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

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
            # Envie o e-mail de confirmação
            subject = 'Cadastro Realizado com Sucesso'
            from_email = 'suportepromogroup@gmail.com '
            recipient_list = [email]

            html_message = render_to_string('registro_feito.html', {'first_name': first_name})
            plain_message = strip_tags(html_message)  # Remove tags HTML para o corpo de texto simples

            send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)

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

def geladeira(request):
    return render(request,'geladeira.html')

def tv(request):
    return render(request,'tv.html')

def livro(request):
    return render(request,'livros.html')

def ar_condicionado(request):
    return render(request,'ar_condicionado.html')