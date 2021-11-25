"""fundsfinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('api.urls', namespace='api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]

# ENDPOINTS GERADOS COM OS DOIS URLS.PY
# /api/v1	GET	Raíz da API gerada automaticamente
# /api/v1/fundos	GET	Listagem de todos os elementos
# /api/v1/fundos	POST	Criação de novo elemento
# /api/v1/fundos/{lookup}	GET	Recuperar elemento pelo ID
# /api/v1/fundos/{lookup}	PUT	Atualização de elemento por ID
# /api/v1/fundos/{lookup}	PATCH	Atualização parcial por ID (partial update)
# /api/v1/fundos/{lookup}	DELETE	Deleção de elemento por ID
# Aqui, {lookup} é o parâmetro utilizado pelo DRF para identificar unicamente um elemento.
#
# Vamos supor que um Fundo tenha id=ef249e21-43cf-47e4-9aac-0ed26af2d0ce.
#
# Podemos excluí-lo enviando uma requisição HTTP DELETE para a URL:
# http://localhost:8000/api/v1/fundos/ef249e21-43cf-47e4-9aac-0ed26af2d0ce
