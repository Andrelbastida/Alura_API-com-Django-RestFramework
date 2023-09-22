from rest_framework import viewsets, generics
from escola.models import Aluno, Curso , Matricula
from escola.serializer import AlunoSerializer, CursoSerializer , MatriculaSerializer, ListaMatriculaAlunoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculasViewSet(viewsets.ModelViewSet):
    """Listando todas as Matrículas """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matrículas de um(a) Aluno(a)"""
    def get_queryset(self): # Estamos criando uma função 
        queryset = Matricula.objects.filter(aluno_id= self.kwargs['pk']) # De todas as matriculas, queremos as que estejam cadastradas ao "ID" de tal aluno
        return queryset
    serializer_class = ListaMatriculaAlunoSerializer




#  from django.shortcuts import render ### Este import , renderiza uma página padrão.
#  from django.http import JsonResponse # quando chegar uma determinada requisiação para uma URL, ele retornará um JSON


# Create your views here.
# def alunos(request):
#    if request.method == 'GET':
#        aluno = {'id' : 1 , 'nome' : 'Andre'}
#        return JsonResponse(aluno) 