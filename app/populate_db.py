from django.core.management.base import BaseCommand
from app.models import *
from django.contrib.auth.models import User
from datetime import datetime, timedelta
import random

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados de exemplo'

    def handle(self, *args, **options):
        # Criar usuários
        usuarios = []
        for i in range(1, 11):
            usuario = Usuario.objects.create(
                nome=f'Usuário {i}',
                email=f'usuario{i}@email.com',
                senha=f'password{i}',
                tipo_usuario='aluno' if i % 2 == 0 else 'professor'
            )
            usuarios.append(usuario)
        
        # Criar perfis de aluno
        for i, usuario in enumerate(usuarios):
            if usuario.tipo_usuario == 'aluno':
                PerfilAluno.objects.create(
                    usuario=usuario,
                    avatar=f'avatar{i}.png',
                    nivel_atual=random.randint(1, 10),
                    pontos_gamificacao=random.randint(100, 1000)
                )
        
        # Criar atividades
        atividades = []
        for i in range(1, 6):
            atividade = Atividade.objects.create(
                titulo=f'Atividade {i}',
                descricao=f'Descrição da atividade {i}',
                pontuacao=random.randint(10, 100),
                tempo_limite=timedelta(minutes=30),
                feedback_positivo=f'Ótimo trabalho na atividade {i}!'
            )
            atividades.append(atividade)
        
        # Criar participações
        for usuario in usuarios:
            if usuario.tipo_usuario == 'aluno':
                for atividade in atividades:
                    Participacao.objects.create(
                        usuario=usuario,
                        atividade=atividade,
                        data=datetime.now().date(),
                        pontuacao_obtida=random.randint(5, 95)
                    )
        
        self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso!'))