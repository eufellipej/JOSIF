from django.shortcuts import render
from django.views import View
from .models import *

class IndexView(View):
    def get(self, request, *args, **kwargs):
        usuarios = Usuario.objects.all()
        return render(request, 'index.html', {'usuarios': usuarios})

class UsuarioView(View):
    def get(self, request, *args, **kwargs):
        usuarios = Usuario.objects.all()
        return render(request, 'usuario.html', {'usuarios': usuarios})

class PerfilAlunoView(View):
    def get(self, request, *args, **kwargs):
        perfis = PerfilAluno.objects.all()
        return render(request, 'perfil_aluno.html', {'perfis': perfis})

class AtividadeView(View):
    def get(self, request, *args, **kwargs):
        atividades = Atividade.objects.all()
        return render(request, 'atividade.html', {'atividades': atividades})

class ParticipacaoView(View):
    def get(self, request, *args, **kwargs):
        participacoes = Participacao.objects.all()
        return render(request, 'participacao.html', {'participacoes': participacoes})

class NotificacaoView(View):
    def get(self, request, *args, **kwargs):
        notificacoes = Notificacao.objects.all()
        return render(request, 'notificacao.html', {'notificacoes': notificacoes})

class RelatorioDesempenhoView(View):
    def get(self, request, *args, **kwargs):
        relatorios = RelatorioDesempenho.objects.all()
        return render(request, 'relatorio.html', {'relatorios': relatorios})

class PersonalizacaoView(View):
    def get(self, request, *args, **kwargs):
        personalizacoes = Personalizacao.objects.all()
        return render(request, 'personalizacao.html', {'personalizacoes': personalizacoes})

class DispositivoIntegradoView(View):
    def get(self, request, *args, **kwargs):
        dispositivos = DispositivoIntegrado.objects.all()
        return render(request, 'dispositivo.html', {'dispositivos': dispositivos})

class TurmaView(View):
    def get(self, request, *args, **kwargs):
        turmas = Turma.objects.all()
        return render(request, 'turma.html', {'turmas': turmas})

class FeedbackView(View):
    def get(self, request, *args, **kwargs):
        feedbacks = Feedback.objects.all()
        return render(request, 'feedback.html', {'feedbacks': feedbacks})

class AulaView(View):
    def get(self, request, *args, **kwargs):
        aulas = Aula.objects.all()
        return render(request, 'aula.html', {'aulas': aulas})

class ProgressoAlunoView(View):
    def get(self, request, *args, **kwargs):
        progressos = ProgressoAluno.objects.all()
        return render(request, 'progresso.html', {'progressos': progressos})
