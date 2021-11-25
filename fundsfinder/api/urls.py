from rest_framework.routers import DefaultRouter
from api.views import FundoImobiliarioViewSet

app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(r'fundos', FundoImobiliarioViewSet)

urlpatterns = router.urls

# app_name é necessário para dar contexto às URLs geradas. Esse parâmetro especifica o namespace das URLConfs
# adicionadas. DefaultRouter é o Router que escolhemos para geração automática das URLs. O parâmetro trailing_slash
# especifica que não é necessário o uso de barras / no final da URL. O método register recebe dois parâmetros: o
# primeiro é o prefixo que será usado na URL (no nosso caso: http://localhost:8000/fundos) e o segundo é a View que
# ira responder as URLs com esse prefixo. Por último, temos o velho urlpatterns do Django, que utilizamos para expor
# as URLs desse app
