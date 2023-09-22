
from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet, MatriculasViewSet, ListaMatriculasAluno
#from escola.views import alunos # Este import se refere a PASTA 'escola'(aplicação), no arquivo 'views' e puxando a função "alunos"
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matriculas',MatriculasViewSet,basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('alunos/', alunos), # quando a URL 'alunos/' for mencionada, quero que retorne minha função "alunos"
    path('' ,include(router.urls)),
    path('aluno/<int:pk>/matriculas',ListaMatriculasAluno.as_view()),
]
