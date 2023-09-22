from rest_framework import serializers
from escola.models import Aluno, Curso , Matricula


class AlunoSerializer (serializers.ModelSerializer):
    class Meta:
        model= Aluno
        fields= ['id', 'nome', 'rg', 'cpf', 'data_nascimento']


class CursoSerializer(serializers.ModelSerializer):
    # nivel = serializers.SerializerMethodField() # Utilizando este campo, o forms no django rest, ficará sem o campo de nível disponível para selecionar 
    # class Meta: 
    #     model= Curso
    #     fields = ['id', 'codigo_curso', 'descricao', 'nivel']
    class Meta: 
        model= Curso
        fields = '__all__'

    def get_nivel(self, obj): # Esta função irá retornar o nível por escrito 
        return obj.get_nivel_display()



        
class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Matricula
        #fields = '__all__' ####!!!! O "exclude" substitui o "fields"
        exclude= [] # Esta função irá excluir o "campo" que inserimos ente as aspas simples 



class ListaMatriculaAlunoSerializer(serializers.ModelSerializer):
    curso= serializers.ReadOnlyField(source= 'curso.descricao')# aqui, ao invés de retornar o id do curso, irá retornar a "descrição"
    #ReadOnlyField :
    periodo= serializers.SerializerMethodField() # para descrevermos o PERIODO, devemos criar uma função : Na linha 35 está descrita a função para obter o periodo 
    #SerializerMethodFiel :
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']


    def get_periodo(self, obj): # Esta função irá retornar o período por escrito 
        return obj.get_periodo_display()


class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='alunos.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome']