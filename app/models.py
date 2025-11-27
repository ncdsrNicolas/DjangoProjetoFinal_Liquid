from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Pagina(BaseModel):
    nome_do_site = models.CharField(max_length=200)
    logo_do_site = models.ImageField(upload_to='logos/', blank=True, null=True)
    texto_chamada = models.CharField(max_length=200)
    subtitulo_chamada = models.CharField(max_length=200, blank=True, null=True)
    imagem_fundo = models.ImageField(upload_to='fundo/', blank=True, null=True)
    texto_sobre = models.TextField()
    imagem_sobre = models.ImageField(upload_to='sobre/', blank=True, null=True)
    endereco = models.CharField(max_length=200)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20)

    def __str__(self):
        return self.nome_do_site

class Produto(BaseModel):
    nome = models.CharField(max_length=200)
    estoque = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='produtos/', blank=True, null=True)

    def __str__(self):
        return self.nome

class Contato(BaseModel):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    mensagem = models.TextField()

    def __str__(self):
        return f"{self.nome} - {self.email}"

class Pedido(BaseModel):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id} - {self.usuario.username}"