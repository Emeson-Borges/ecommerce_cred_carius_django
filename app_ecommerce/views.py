from django.shortcuts import render, redirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.db import models
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import AdminForm

#Importar de onde vem os Models
from app_funcionarios.models import funcionarios
from app_produtos.models import produtos
# Create your views here.

def home(request):
  return render(request, 'home/home.html')

def login(request):
  return render(request, 'login/login.html')

def redefinir_senha(request):
  return render(request, 'redefinir_senha/redefinir_senha.html')
#-------------------------------------------------------------------
# Rotas para Cadastrar no Sistema
def cadastrar_usuario(request):
  return render(request, 'cadastrar_usuario/cadastrar_usuario.html')

def cadastrar_funcionario(request):
  return render(request, 'cadastrar_funcionario/cadastrar_funcionario.html')

def cadastrar_produto(request):
  return render(request, 'cadastrar_produto/cadastrar_produto.html')

def cadastrar_vendas(request):
  return render(request, 'cadastrar_vendas/cadastrar_vendas.html')
# -------------------------------------------------------------------

#Rotas para salvar dados no banco 
def cad_produtos(request):
  return render(request, 'cadastrar_produto/cadastrar_produto.html')

# def cad_funcionarios(request):
#   return render(request, 'cadastrar_funcionario/cadastrar_funcionario.html')
# -----------------------------------------------------------------
def vendas(request):
  return render(request, 'vendas/vendas.html')

def relatorios(request):
  return render(request, 'relatorios/relatorios.html')

#Função para listar itens na tela
def lista_produtos(request):
    Produtos = produtos.objects.all()
    return render(request, 'listar_produtos/listar_produtos.html', {'produtos': Produtos})

def listar_funcionarios(request):
    Funcionarios = funcionarios.objects.all()
    return render(request, 'listar_funcionarios/listar_funcionarios.html', {'produtos': Funcionarios})

#Classe do Modelo do Site
class ModeloView(TemplateView):
    template_name = "modelo_site/modelo_site.html"
    
class HomeView(TemplateView):
  template_name = "home/home.html"
  
  
  # Perfil do Administrador 
def admin_profile(request):
    # Lógica para recuperar os detalhes do perfil do administrador
    profile_data = {
        'username': request.user.username,
        'email': request.user.email,
        # outros dados relevantes do perfil
    }
    
    return render(request, 'admin/profile.html', {'profile_data': profile_data})

#Criar novo Usuário Administrador 
def create_admin(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            # Cria um novo usuário com as informações fornecidas no formulário
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, email=email, password=password)

            # Redireciona para a página de perfil do administrador recém-criado ou para outra página
            return redirect('admin:admin_profile')
    else:
        form = AdminForm()

    return render(request, 'admin/create_admin.html', {'form': form})
  
# ------  Class para salvar os dados vindo do Front-End  --------

# Salvar na tabela Funcionários
def cad_funcionarios(request):
  if request.method == 'POST':
    nome        = request.POST['nome']
    cpf         = request.POST['cpf']  
    rg          = request.POST['rg']                
    cidade      = request.POST['cidade']
    rua         = request.POST['rua']
    bairro      = request.POST['bairro']
    dtnasc_func = request.POST['dtnasc_func']
    numero_casa = request.POST['numero_casa']
    contato     = request.POST['contato']
    
    cad_funcionarios = funcionarios.objects.create(nome=nome,cpf=cpf,rg=rg,cidade=cidade,\
      rua=rua,bairro=bairro,dtnasc_func=dtnasc_func,numero_casa=numero_casa,contato=contato)
    
    cad_funcionarios.save()
    messages.success(request, 'Funcionário cadastrado com sucesso.')
    return redirect('cadastrar_funcionario')
  
  return render(request, 'cadastrar_funcionario.html')

# Salvar na tabela Produtos
def cad_produto(request):
  if request.method == 'POST':
    nome      = request.POST['nome']
    qtdprod   = request.POST['qtdprod']
    preco     = request.POST['preco']
    descricao = request.POST['descricao']
    
    
    cad_produto = produtos.objects.create(nome=nome,qtdprod=qtdprod,preco=preco,\
      descricao=descricao)
   
    cad_produto.save()
    messages.success(request, 'Produto cadastrado com sucesso.')
    return redirect('cadastrar_produto')
  
  return render(request, 'cadastrar_produto.html')

# Salvar na tabela Vendas
