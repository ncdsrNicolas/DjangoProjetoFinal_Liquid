from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("produtos/", views.produtos, name="produtos"),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("compra/<int:produto_id>/", views.compra, name="compra"),
    path("perfil/", views.perfil, name="perfil"),
]
