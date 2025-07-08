from django.db import models


class Usuario(models.Model):
    TIPO_USUARIO_CHOICES = [
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
    ]
    nome = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField(unique=True, verbose_name="Email")
    senha = models.CharField(max_length=128, verbose_name="Senha")
    tipo_usuario = models.CharField(max_length=10, choices=TIPO_USUARIO_CHOICES, verbose_name="Tipo de Usuário")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"


class PerfilAluno(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, verbose_name="Usuário")
    avatar = models.CharField(max_length=100, verbose_name="Avatar")
    nivel_atual = models.IntegerField(verbose_name="Nível Atual")
    pontos_gamificacao = models.IntegerField(verbose_name="Pontos de Gamificação")

    def __str__(self):
        return f"{self.usuario.nome} - Nível {self.nivel_atual}"

    class Meta:
        verbose_name = "Perfil do Aluno"
        verbose_name_plural = "Perfis dos Alunos"


class Atividade(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    descricao = models.TextField(verbose_name="Descrição")
    pontuacao = models.IntegerField(verbose_name="Pontuação")
    tempo_limite = models.DurationField(verbose_name="Tempo Limite")
    feedback_positivo = models.CharField(max_length=200, verbose_name="Feedback Positivo")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Atividade"
        verbose_name_plural = "Atividades"


class Participacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuário")
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE, verbose_name="Atividade")
    data = models.DateField(verbose_name="Data")
    pontuacao_obtida = models.IntegerField(verbose_name="Pontuação Obtida")

    def __str__(self):
        return f"{self.usuario.nome} - {self.atividade.titulo}"

    class Meta:
        verbose_name = "Participação"
        verbose_name_plural = "Participações"


class Notificacao(models.Model):
    TIPO_CHOICES = [
        ('lembrete', 'Lembrete'),
        ('gamificacao', 'Gamificação'),
    ]
    mensagem = models.CharField(max_length=200, verbose_name="Mensagem")
    data_envio = models.DateField(verbose_name="Data de Envio")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuário")
    tipo_notificacao = models.CharField(max_length=20, choices=TIPO_CHOICES, verbose_name="Tipo de Notificação")

    def __str__(self):
        return self.mensagem

    class Meta:
        verbose_name = "Notificação"
        verbose_name_plural = "Notificações"


class RelatorioDesempenho(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuário")
    atividades_realizadas = models.IntegerField(verbose_name="Atividades Realizadas")
    media_pontos = models.FloatField(verbose_name="Média de Pontos")
    ultima_atividade = models.DateField(verbose_name="Última Atividade")

    def __str__(self):
        return f"Desempenho de {self.usuario.nome}"

    class Meta:
        verbose_name = "Relatório de Desempenho"
        verbose_name_plural = "Relatórios de Desempenho"


class Personalizacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuário")
    tema_visual = models.CharField(max_length=100, verbose_name="Tema Visual")
    som_ambiente = models.CharField(max_length=100, verbose_name="Som Ambiente")

    def __str__(self):
        return f"{self.usuario.nome} - {self.tema_visual}"

    class Meta:
        verbose_name = "Personalização"
        verbose_name_plural = "Personalizações"


class DispositivoIntegrado(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuário")
    tipo_dispositivo = models.CharField(max_length=100, verbose_name="Tipo de Dispositivo")
    status = models.CharField(max_length=50, verbose_name="Status")

    def __str__(self):
        return f"{self.tipo_dispositivo} - {self.status}"

    class Meta:
        verbose_name = "Dispositivo Integrado"
        verbose_name_plural = "Dispositivos Integrados"


class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    ano = models.IntegerField(verbose_name="Ano")
    professor_responsavel = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='turmas_responsaveis', verbose_name="Professor Responsável")
    alunos = models.ManyToManyField(Usuario, related_name='turmas', verbose_name="Alunos")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"


class Feedback(models.Model):
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE, verbose_name="Atividade")
    mensagem_positiva = models.CharField(max_length=200, verbose_name="Mensagem Positiva")
    nivel_dificuldade = models.CharField(max_length=50, verbose_name="Nível de Dificuldade")

    def __str__(self):
        return self.mensagem_positiva

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"


class Aula(models.Model):
    data = models.DateField(verbose_name="Data")
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, verbose_name="Turma")
    atividades = models.ManyToManyField(Atividade, verbose_name="Atividades")

    def __str__(self):
        return f"Aula de {self.data} - {self.turma.nome}"

    class Meta:
        verbose_name = "Aula"
        verbose_name_plural = "Aulas"


class ProgressoAluno(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuário")
    nivel = models.IntegerField(verbose_name="Nível")
    conquistas = models.CharField(max_length=200, verbose_name="Conquistas")
    tempo_total_focado = models.DurationField(verbose_name="Tempo Total Focado")

    def __str__(self):
        return f"{self.usuario.nome} - Nível {self.nivel}"

    class Meta:
        verbose_name = "Progresso do Aluno"
        verbose_name_plural = "Progressos dos Alunos"
