from django.contrib import admin
from .models import *

# i) Perfil do Aluno como inline do Usuário (Um para Um)
class PerfilAlunoInline(admin.StackedInline):
    model = PerfilAluno
    can_delete = False
    verbose_name_plural = "Perfil do Aluno"

class UsuarioAdmin(admin.ModelAdmin):
    inlines = [PerfilAlunoInline]
    list_display = ('nome', 'email', 'tipo_usuario')
    list_filter = ['tipo_usuario']
    search_fields = ['nome', 'email']

# ii) Participações como inline do Usuário
class ParticipacaoInline(admin.TabularInline):
    model = Participacao
    extra = 1

# iii) Atividades e Feedback como inline (por atividade)
class FeedbackInline(admin.TabularInline):
    model = Feedback
    extra = 1

class AtividadeAdmin(admin.ModelAdmin):
    inlines = [FeedbackInline]
    list_display = ('titulo', 'pontuacao', 'tempo_limite')
    search_fields = ['titulo']

# iv) Aula com atividades inline
class AulaAdmin(admin.ModelAdmin):
    filter_horizontal = ['atividades']
    list_display = ('data', 'turma')

# v) Turmas com alunos listados
class TurmaAdmin(admin.ModelAdmin):
    filter_horizontal = ['alunos']
    list_display = ('nome', 'ano', 'professor_responsavel')
    search_fields = ['nome']

# vi) Personalização, Dispositivo e Progresso como readonly no admin de usuário
class PersonalizacaoInline(admin.TabularInline):
    model = Personalizacao
    extra = 0

class DispositivoIntegradoInline(admin.TabularInline):
    model = DispositivoIntegrado
    extra = 0

class ProgressoAlunoInline(admin.StackedInline):
    model = ProgressoAluno
    extra = 0

# vii) RelatórioDesempenho
class RelatorioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'atividades_realizadas', 'media_pontos', 'ultima_atividade')
    list_filter = ['media_pontos']
    search_fields = ['usuario__nome']

# Registrar todos os modelos
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Atividade, AtividadeAdmin)
admin.site.register(Participacao)
admin.site.register(Notificacao)
admin.site.register(RelatorioDesempenho, RelatorioAdmin)
admin.site.register(Personalizacao)
admin.site.register(DispositivoIntegrado)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Feedback)
admin.site.register(Aula, AulaAdmin)
admin.site.register(ProgressoAluno)
