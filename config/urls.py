from django.contrib import admin
from django.urls import path
from app.views import *
from app.auth_views import LoginView, RegisterView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('usuario/', UsuarioView.as_view(), name='usuario'),                             # RF01
    path('perfil_aluno/', PerfilAlunoView.as_view(), name='perfil_aluno'),               # RF02
    path('atividade/', AtividadeView.as_view(), name='atividade'),                       # RF03
    path('participacao/', ParticipacaoView.as_view(), name='participacao'),              # RF04
    path('notificacao/', NotificacaoView.as_view(), name='notificacao'),                 # RF05
    path('relatorio/', RelatorioDesempenhoView.as_view(), name='relatorio'),             # RF06
    path('personalizacao/', PersonalizacaoView.as_view(), name='personalizacao'),        # RF07
    path('dispositivo/', DispositivoIntegradoView.as_view(), name='dispositivo'),        # RF08
    path('turma/', TurmaView.as_view(), name='turma'),                                   # RF09
    path('feedback/', FeedbackView.as_view(), name='feedback'),                          # RF10
    path('aula/', AulaView.as_view(), name='aula'),                                      # RF11
    path('progresso/', ProgressoAlunoView.as_view(), name='progresso'),                  # RF12
]