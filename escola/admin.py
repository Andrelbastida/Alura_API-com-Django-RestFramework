from django.contrib import admin
from escola.models import Aluno, Curso # estamos importando de nosso app "escola",as nossas classes 'Aluno' e 'Curso'

# Register your models here.

class Alunos(admin.ModelAdmin):
    list_display = ('id' , 'nome', 'rg', 'cpf', 'data_nascimento') # Estas são as informações que serão disponibilizadas.
    list_display_links = ('id' , 'nome') # sempre que eu quiser alterar algum aluno, vou clicar no 'id'ou no 'nome'(campos que vamos poder alterar) 
    search_fields  = ('nome',) # Campo de busca 
    list_per_page = 20 # lista 20 alunos por página 

admin.site.register(Aluno, Alunos) # Vamos registrar a nossa configuração acima (Alunos), 
# colocamos o "Aluno"( pois foi o modelo que importamos de nossa aplicação "escola") 
# Colocamos o "Alunos" ( pois é a configuração que criamos no "ModelAdmin" acima)

class Cursos(admin.ModelAdmin):
    list_display = ('id' , 'codigo_curso', 'descricao') 
    list_display_links= ('id', 'codigo_curso')
    search_fields= ('codigo_curso', )
    list_per_page= 20

admin.site.register(Curso, Cursos)