from django.contrib import admin
from .models import Participante, QuestionarioIPAQ, IndicadorSaude, BarreiraSedentarismo, EstrategiaPrevencao


@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'idade', 'sexo', 'tipo_participante', 'data_cadastro']
    list_filter = ['tipo_participante', 'sexo', 'data_cadastro']
    search_fields = ['nome', 'email', 'curso', 'setor']
    ordering = ['-data_cadastro']
    
    fieldsets = (
        ('Dados Pessoais', {
            'fields': ('nome', 'email', 'idade', 'sexo')
        }),
        ('Vínculo', {
            'fields': ('tipo_participante', 'curso', 'setor')
        }),
    )


@admin.register(QuestionarioIPAQ)
class QuestionarioIPAQAdmin(admin.ModelAdmin):
    list_display = ['participante', 'nivel_atividade', 'met_total', 'data_preenchimento']
    list_filter = ['nivel_atividade', 'data_preenchimento']
    search_fields = ['participante__nome']
    readonly_fields = ['nivel_atividade', 'met_total', 'data_preenchimento']
    
    fieldsets = (
        ('Participante', {
            'fields': ('participante',)
        }),
        ('Atividades Vigorosas', {
            'fields': ('dias_atividade_vigorosa', 'minutos_atividade_vigorosa')
        }),
        ('Atividades Moderadas', {
            'fields': ('dias_atividade_moderada', 'minutos_atividade_moderada')
        }),
        ('Caminhada', {
            'fields': ('dias_caminhada', 'minutos_caminhada')
        }),
        ('Tempo Sentado', {
            'fields': ('horas_sentado_semana', 'horas_sentado_fim_semana')
        }),
        ('Resultados', {
            'fields': ('nivel_atividade', 'met_total', 'data_preenchimento'),
            'classes': ('collapse',)
        }),
    )


@admin.register(IndicadorSaude)
class IndicadorSaudeAdmin(admin.ModelAdmin):
    list_display = ['participante', 'imc', 'pressao_sistolica', 'pressao_diastolica', 'tem_diabetes', 'tem_hipertensao']
    list_filter = ['tem_diabetes', 'tem_hipertensao', 'tem_obesidade', 'fuma', 'consome_alcool']
    search_fields = ['participante__nome']
    readonly_fields = ['imc', 'data_avaliacao']
    
    fieldsets = (
        ('Participante', {
            'fields': ('participante',)
        }),
        ('Dados Antropométricos', {
            'fields': ('peso', 'altura', 'imc')
        }),
        ('Pressão Arterial', {
            'fields': ('pressao_sistolica', 'pressao_diastolica')
        }),
        ('Histórico de Doenças', {
            'fields': ('tem_diabetes', 'tem_hipertensao', 'tem_obesidade', 'tem_doenca_cardiovascular')
        }),
        ('Hábitos', {
            'fields': ('fuma', 'consome_alcool')
        }),
    )


@admin.register(BarreiraSedentarismo)
class BarreiraSedentarismoAdmin(admin.ModelAdmin):
    list_display = ['participante', 'categoria', 'intensidade', 'descricao']
    list_filter = ['categoria', 'intensidade']
    search_fields = ['participante__nome', 'descricao']
    
    fieldsets = (
        ('Participante', {
            'fields': ('participante',)
        }),
        ('Barreira', {
            'fields': ('categoria', 'descricao', 'intensidade')
        }),
    )


@admin.register(EstrategiaPrevencao)
class EstrategiaPrevencaoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tipo', 'publico_alvo', 'responsavel', 'ativa', 'data_criacao']
    list_filter = ['tipo', 'ativa', 'data_criacao']
    search_fields = ['titulo', 'descricao', 'publico_alvo', 'responsavel']
    ordering = ['-data_criacao']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('titulo', 'descricao', 'tipo', 'ativa')
        }),
        ('Implementação', {
            'fields': ('publico_alvo', 'recursos_necessarios', 'prazo_implementacao', 'responsavel')
        }),
    )

