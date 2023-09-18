
from django.contrib import admin
from django.urls import path
from escola.views import alunos # Este import se refere a PASTA 'escola'(aplicação), no arquivo 'views' e puxando a função "alunos"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alunos/', alunos), # quando a URL 'alunos/' for mencionada, quero que retorne minha função "alunos"
]
