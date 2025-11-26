from .models import Pagina

def pagina_context(request):
    pagina = Pagina.objects.first()
    return {"pagina": pagina}
