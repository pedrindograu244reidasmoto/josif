from django.db import models
from django.urls import reverse


class Participante(models.Model):
    TIPO_CHOICES = [
        ('aluno', 'Aluno'),
        ('servidor', 'Servidor'),
        ('morador', 'Morador do Entorno'),
    ]
    
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    idade = models.PositiveIntegerField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    tipo_participante = models.CharField(max_length=20, choices=TIPO_CHOICES)
    curso = models.CharField(max_length=100, blank=True, help_text="Para alunos")
    setor = models.CharField(max_length=100, blank=True, help_text="Para servidores")
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Participante'
        verbose_name_plural = 'Participantes'
        ordering = ['-data_cadastro']
    
    def __str__(self):
        return f"{self.nome} ({self.get_tipo_participante_display()})"


class QuestionarioIPAQ(models.Model):
    """Questionário Internacional de Atividade Física"""
    
    NIVEL_ATIVIDADE_CHOICES = [
        ('baixo', 'Baixo'),
        ('moderado', 'Moderado'),
        ('alto', 'Alto'),
    ]
    
    participante = models.OneToOneField(Participante, on_delete=models.CASCADE)
    
    # Atividades vigorosas
    dias_atividade_vigorosa = models.PositiveIntegerField(
        help_text="Quantos dias por semana você faz atividades físicas vigorosas?"
    )
    minutos_atividade_vigorosa = models.PositiveIntegerField(
        help_text="Quantos minutos por dia você dedica a essas atividades?"
    )
    
    # Atividades moderadas
    dias_atividade_moderada = models.PositiveIntegerField(
        help_text="Quantos dias por semana você faz atividades físicas moderadas?"
    )
    minutos_atividade_moderada = models.PositiveIntegerField(
        help_text="Quantos minutos por dia você dedica a essas atividades?"
    )
    
    # Caminhada
    dias_caminhada = models.PositiveIntegerField(
        help_text="Quantos dias por semana você caminha?"
    )
    minutos_caminhada = models.PositiveIntegerField(
        help_text="Quantos minutos por dia você dedica à caminhada?"
    )
    
    # Tempo sentado
    horas_sentado_semana = models.DecimalField(
        max_digits=4, decimal_places=1,
        help_text="Quantas horas por dia você fica sentado em dias de semana?"
    )
    horas_sentado_fim_semana = models.DecimalField(
        max_digits=4, decimal_places=1,
        help_text="Quantas horas por dia você fica sentado em fins de semana?"
    )
    
    # Classificação calculada
    nivel_atividade = models.CharField(max_length=20, choices=NIVEL_ATIVIDADE_CHOICES, blank=True)
    met_total = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    
    data_preenchimento = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Questionário IPAQ'
        verbose_name_plural = 'Questionários IPAQ'
    
    def __str__(self):
        return f"IPAQ - {self.participante.nome}"
    
    def calcular_met(self):
        """Calcula o MET total semanal"""
        # METs para diferentes atividades
        met_vigorosa = 8.0
        met_moderada = 4.0
        met_caminhada = 3.3
        
        # Cálculo dos METs
        met_total = (
            (self.dias_atividade_vigorosa * self.minutos_atividade_vigorosa * met_vigorosa) +
            (self.dias_atividade_moderada * self.minutos_atividade_moderada * met_moderada) +
            (self.dias_caminhada * self.minutos_caminhada * met_caminhada)
        )
        
        return met_total
    
    def classificar_nivel_atividade(self):
        """Classifica o nível de atividade física"""
        met_total = self.calcular_met()
        
        if met_total < 600:
            return 'baixo'
        elif met_total < 3000:
            return 'moderado'
        else:
            return 'alto'
    
    def save(self, *args, **kwargs):
        self.met_total = self.calcular_met()
        self.nivel_atividade = self.classificar_nivel_atividade()
        super().save(*args, **kwargs)


class IndicadorSaude(models.Model):
    """Indicadores de saúde dos participantes"""
    
    participante = models.OneToOneField(Participante, on_delete=models.CASCADE)
    
    # Dados antropométricos
    peso = models.DecimalField(max_digits=5, decimal_places=2, help_text="Peso em kg")
    altura = models.DecimalField(max_digits=4, decimal_places=2, help_text="Altura em metros")
    imc = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    
    # Pressão arterial
    pressao_sistolica = models.PositiveIntegerField(help_text="Pressão sistólica (mmHg)")
    pressao_diastolica = models.PositiveIntegerField(help_text="Pressão diastólica (mmHg)")
    
    # Histórico de doenças
    tem_diabetes = models.BooleanField(default=False)
    tem_hipertensao = models.BooleanField(default=False)
    tem_obesidade = models.BooleanField(default=False)
    tem_doenca_cardiovascular = models.BooleanField(default=False)
    
    # Hábitos
    fuma = models.BooleanField(default=False)
    consome_alcool = models.BooleanField(default=False)
    
    data_avaliacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Indicador de Saúde'
        verbose_name_plural = 'Indicadores de Saúde'
    
    def __str__(self):
        return f"Indicadores - {self.participante.nome}"
    
    def calcular_imc(self):
        """Calcula o IMC"""
        if self.altura > 0:
            return self.peso / (self.altura ** 2)
        return 0
    
    def classificar_imc(self):
        """Classifica o IMC"""
        imc = self.imc or self.calcular_imc()
        
        if imc < 18.5:
            return 'Abaixo do peso'
        elif imc < 25:
            return 'Peso normal'
        elif imc < 30:
            return 'Sobrepeso'
        else:
            return 'Obesidade'
    
    def save(self, *args, **kwargs):
        self.imc = self.calcular_imc()
        super().save(*args, **kwargs)


class BarreiraSedentarismo(models.Model):
    """Barreiras identificadas para a prática de atividade física"""
    
    CATEGORIA_CHOICES = [
        ('tempo', 'Falta de Tempo'),
        ('infraestrutura', 'Infraestrutura Inadequada'),
        ('motivacao', 'Falta de Motivação'),
        ('conhecimento', 'Falta de Conhecimento'),
        ('financeiro', 'Limitações Financeiras'),
        ('saude', 'Problemas de Saúde'),
        ('social', 'Falta de Apoio Social'),
        ('tecnologia', 'Uso Excessivo de Tecnologia'),
    ]
    
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE, related_name='barreiras')
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    descricao = models.TextField()
    intensidade = models.PositiveIntegerField(
        help_text="Intensidade da barreira (1-5, sendo 5 muito intensa)"
    )
    
    class Meta:
        verbose_name = 'Barreira ao Sedentarismo'
        verbose_name_plural = 'Barreiras ao Sedentarismo'
    
    def __str__(self):
        return f"{self.get_categoria_display()} - {self.participante.nome}"


class EstrategiaPrevencao(models.Model):
    """Estratégias propostas para prevenção do sedentarismo"""
    
    TIPO_CHOICES = [
        ('individual', 'Individual'),
        ('institucional', 'Institucional'),
        ('comunitaria', 'Comunitária'),
    ]
    
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    publico_alvo = models.CharField(max_length=100)
    recursos_necessarios = models.TextField()
    prazo_implementacao = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=100)
    
    data_criacao = models.DateTimeField(auto_now_add=True)
    ativa = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Estratégia de Prevenção'
        verbose_name_plural = 'Estratégias de Prevenção'
        ordering = ['-data_criacao']
    
    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('pesquisa:estrategia_detalhe', kwargs={'pk': self.pk})

