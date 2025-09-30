from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

class IndexView(View):
    def get(self, request, *args, **kwargs):
        usuarios = Usuario.objects.all()
        return render(request, 'index.html', {'usuarios': usuarios})

class UsuarioView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        usuarios = Usuario.objects.all()
        return render(request, 'usuario.html', {'usuarios': usuarios})

class PerfilAlunoView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        perfis = PerfilAluno.objects.all()
        return render(request, 'perfil_aluno.html', {'perfis': perfis})

class AtividadeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        atividades = Atividade.objects.all()
        return render(request, 'atividade.html', {'atividades': atividades})

class ParticipacaoView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        participacoes = Participacao.objects.all()
        return render(request, 'participacao.html', {'participacoes': participacoes})

class NotificacaoView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        notificacoes = Notificacao.objects.all()
        return render(request, 'notificacao.html', {'notificacoes': notificacoes})

class RelatorioDesempenhoView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        relatorios = RelatorioDesempenho.objects.all()
        return render(request, 'relatorio.html', {'relatorios': relatorios})

class PersonalizacaoView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        personalizacoes = Personalizacao.objects.all()
        return render(request, 'personalizacao.html', {'personalizacoes': personalizacoes})

class DispositivoIntegradoView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        dispositivos = DispositivoIntegrado.objects.all()
        return render(request, 'dispositivo.html', {'dispositivos': dispositivos})

class TurmaView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        turmas = Turma.objects.all()
        return render(request, 'turma.html', {'turmas': turmas})

class FeedbackView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        feedbacks = Feedback.objects.all()
        return render(request, 'feedback.html', {'feedbacks': feedbacks})

class AulaView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        aulas = Aula.objects.all()
        return render(request, 'aula.html', {'aulas': aulas})

class ProgressoAlunoView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        progressos = ProgressoAluno.objects.all()
        return render(request, 'progresso.html', {'progressos': progressos})
    
# Adicione ao arquivo views.py
class PerfilAlunoDetailView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        try:
            # Buscar o usuário pelo ID
            usuario = Usuario.objects.get(pk=pk, tipo_usuario='aluno')
            perfil_aluno = PerfilAluno.objects.get(usuario=usuario)
            
            # Buscar dados relacionados
            participacoes = Participacao.objects.filter(usuario=usuario)
            progresso = ProgressoAluno.objects.filter(usuario=usuario).first()
            relatorio = RelatorioDesempenho.objects.filter(usuario=usuario).first()
            
            # Verificar se o aluno pertence a alguma turma
            turmas = Turma.objects.filter(alunos=usuario)
            colegas = Usuario.objects.filter(
                turmas__in=turmas, 
                tipo_usuario='aluno'
            ).exclude(pk=usuario.pk).distinct()
            
            context = {
                'usuario': usuario,
                'perfil_aluno': perfil_aluno,
                'participacoes': participacoes,
                'progresso': progresso,
                'relatorio': relatorio,
                'turmas': turmas,
                'colegas': colegas,
            }
            
            return render(request, 'perfil_aluno.html', context)
            
        except Usuario.DoesNotExist:
            raise ("Aluno não encontrado")
        except PerfilAluno.DoesNotExist:
            raise ("Perfil do aluno não encontrado")