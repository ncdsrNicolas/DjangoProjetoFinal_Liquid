from django.contrib import admin
from .models import Pagina, Produto, Contato, Pedido

admin.site.register(Pagina)
admin.site.register(Produto)
admin.site.register(Contato)
admin.site.register(Pedido)