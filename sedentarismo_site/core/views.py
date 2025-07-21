from django.shortcuts import render
from django.db.models import Count, Avg
from pesquisa.models import Participante, QuestionarioIPAQ, IndicadorSaude, BarreiraSedentarismo, EstrategiaPrevencao


def home(request):
    """Página inicial com resumo da pesquisa"""
    
    # Estatísticas gerais
    total_participantes = Participante.objects.count()
    total_questionarios = QuestionarioIPAQ.objects.count()
    
    # Distribuição por tipo de participante
    distribuicao_tipo = Participante.objects.values('tipo_participante').annotate(
        total=Count('id')
    ).order_by('-total')
    
    # Níveis de atividade física
    niveis_atividade = QuestionarioIPAQ.objects.values('nivel_atividade').annotate(
        total=Count('id')
    ).order_by('-total')
    
    # Principais barreiras
    principais_barreiras = BarreiraSedentarismo.objects.values('categoria').annotate(
        total=Count('id'),
        intensidade_media=Avg('intensidade')
    ).order_by('-total')[:5]
    
    # Estratégias ativas
    estrategias_ativas = EstrategiaPrevencao.objects.filter(ativa=True).order_by('-data_criacao')[:3]
    
    context = {
        'total_participantes': total_participantes,
        'total_questionarios': total_questionarios,
        'distribuicao_tipo': distribuicao_tipo,
        'niveis_atividade': niveis_atividade,
        'principais_barreiras': principais_barreiras,
        'estrategias_ativas': estrategias_ativas,
    }
    
    return render(request, 'core/home.html', context)


def sobre_pesquisa(request):
    """Página sobre a pesquisa"""
    return render(request, 'core/sobre.html')


def metodologia(request):
    """Página sobre a metodologia da pesquisa"""
    return render(request, 'core/metodologia.html')


def resultados(request):
    """Página com resultados da pesquisa"""
    
    # Dados para gráficos e análises
    total_participantes = Participante.objects.count()
    
    # Distribuição por sexo
    distribuicao_sexo = Participante.objects.values('sexo').annotate(
        total=Count('id')
    )
    
    # Distribuição por faixa etária
    participantes_com_idade = Participante.objects.all()
    faixas_etarias = {
        '18-25': 0,
        '26-35': 0,
        '36-45': 0,
        '46-55': 0,
        '56+': 0
    }
    
    for p in participantes_com_idade:
        if p.idade <= 25:
            faixas_etarias['18-25'] += 1
        elif p.idade <= 35:
            faixas_etarias['26-35'] += 1
        elif p.idade <= 45:
            faixas_etarias['36-45'] += 1
        elif p.idade <= 55:
            faixas_etarias['46-55'] += 1
        else:
            faixas_etarias['56+'] += 1
    
    # Análise de sedentarismo
    sedentarios = QuestionarioIPAQ.objects.filter(nivel_atividade='baixo').count()
    percentual_sedentarios = (sedentarios / total_participantes * 100) if total_participantes > 0 else 0
    
    # IMC médio
    imc_medio = IndicadorSaude.objects.aggregate(Avg('imc'))['imc__avg'] or 0
    
    # Doenças mais prevalentes
    prevalencia_diabetes = IndicadorSaude.objects.filter(tem_diabetes=True).count()
    prevalencia_hipertensao = IndicadorSaude.objects.filter(tem_hipertensao=True).count()
    prevalencia_obesidade = IndicadorSaude.objects.filter(tem_obesidade=True).count()
    
    context = {
        'total_participantes': total_participantes,
        'distribuicao_sexo': distribuicao_sexo,
        'faixas_etarias': faixas_etarias,
        'percentual_sedentarios': round(percentual_sedentarios, 1),
        'imc_medio': round(imc_medio, 1),
        'prevalencia_diabetes': prevalencia_diabetes,
        'prevalencia_hipertensao': prevalencia_hipertensao,
        'prevalencia_obesidade': prevalencia_obesidade,
    }
    
    return render(request, 'core/resultados.html', context)


def estrategias(request):
    """Página com estratégias de prevenção"""
    
    estrategias_individuais = EstrategiaPrevencao.objects.filter(
        tipo='individual', ativa=True
    ).order_by('-data_criacao')
    
    estrategias_institucionais = EstrategiaPrevencao.objects.filter(
        tipo='institucional', ativa=True
    ).order_by('-data_criacao')
    
    estrategias_comunitarias = EstrategiaPrevencao.objects.filter(
        tipo='comunitaria', ativa=True
    ).order_by('-data_criacao')
    
    context = {
        'estrategias_individuais': estrategias_individuais,
        'estrategias_institucionais': estrategias_institucionais,
        'estrategias_comunitarias': estrategias_comunitarias,
    }
    
    return render(request, 'core/estrategias.html', context)


def contato(request):
    """Página de contato"""
    return render(request, 'core/contato.html')

