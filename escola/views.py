from rest_framework import viewsets
from escola.models import Aluno, Curso
from escola.serializer import AlunoSerializer, CursoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer







#  from django.shortcuts import render ### Este import , renderiza uma página padrão.
#  from django.http import JsonResponse # quando chegar uma determinada requisiação para uma URL, ele retornará um JSON


# Create your views here.
# def alunos(request):
#    if request.method == 'GET':
#        aluno = {'id' : 1 , 'nome' : 'Andre'}
#        return JsonResponse(aluno) 