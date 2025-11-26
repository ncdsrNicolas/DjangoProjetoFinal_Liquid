from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Pagina, Produto, Contato, Pedido

def index(request):
    pagina = Pagina.objects.first()
    produtos = Produto.objects.all()[:12]

    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        mensagem = request.POST.get("mensagem")
        Contato.objects.create(nome=nome, email=email, mensagem=mensagem)
        return redirect("index")

    return render(request, "index.html", {
        "pagina": pagina,
        "produtos": produtos
    })

def produtos(request):
    produtos = Produto.objects.all()
    return render(request, "produtos.html", {"produtos": produtos})


def cadastro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)  # já loga após cadastro
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "cadastro.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect("index")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("index")

@login_required
def compra(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == "POST":
        quantidade = int(request.POST.get("quantidade"))
        total = quantidade * produto.preco

        Pedido.objects.create(
            usuario=request.user,
            produto=produto,
            quantidade=quantidade,
            total=total
        )

        produto.estoque -= quantidade
        produto.save()

        return redirect("perfil")

    return render(request, "compra.html", {"produto": produto})

@login_required
def perfil(request):
    pedidos = Pedido.objects.filter(usuario=request.user)
    return render(request, "perfil.html", {"pedidos": pedidos})
