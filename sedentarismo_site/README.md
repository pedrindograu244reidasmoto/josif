# Site sobre Sedentarismo - IFSULDEMINAS Muzambinho

Este projeto Django foi desenvolvido para apresentar uma pesquisa sobre "O Aumento do Sedentarismo e suas Consequências na Saúde do IFSULDEMINAS Campus Muzambinho".

## Sobre a Pesquisa

O sedentarismo é reconhecido como um dos principais fatores de risco para doenças crônicas não transmissíveis (DCNTs), como obesidade, diabetes e doenças cardiovasculares. No contexto do IFSULDEMINAS – Campus Muzambinho, observa-se um aumento dos comportamentos sedentários entre alunos, servidores e moradores do entorno.

### Objetivos

- Analisar o impacto do sedentarismo na saúde pública local
- Identificar fatores associados ao sedentarismo
- Propor estratégias de promoção da atividade física
- Subsidiar ações institucionais para promoção da saúde

## Funcionalidades do Site

### 1. Página Inicial
- Apresentação da pesquisa
- Estatísticas principais dos participantes
- Gráficos de distribuição por categoria
- Principais barreiras identificadas
- Estratégias de prevenção propostas

### 2. Sobre a Pesquisa
- Contexto e justificativa
- Objetivos da pesquisa
- Importância do estudo

### 3. Metodologia
- Abordagem quantitativa e qualitativa
- Questionários IPAQ (International Physical Activity Questionnaire)
- Critérios de participação
- Métodos de análise

### 4. Resultados
- Análise dos dados coletados
- Gráficos e visualizações
- Correlações entre sedentarismo e indicadores de saúde
- Prevalência de doenças crônicas

### 5. Estratégias de Prevenção
- Propostas individuais
- Ações institucionais
- Iniciativas comunitárias
- Planos de implementação

## Estrutura do Projeto

### Apps Django

#### 1. Core
- Views principais do site
- Templates base
- Páginas estáticas (sobre, contato, etc.)

#### 2. Pesquisa
- Modelos de dados da pesquisa
- Administração dos dados
- Lógica de negócio específica

### Modelos de Dados

#### Participante
- Dados pessoais dos participantes
- Tipo (aluno, servidor, morador)
- Informações acadêmicas/profissionais

#### QuestionarioIPAQ
- Dados do questionário de atividade física
- Cálculo automático de METs
- Classificação do nível de atividade

#### IndicadorSaude
- Dados antropométricos (peso, altura, IMC)
- Pressão arterial
- Histórico de doenças
- Hábitos (fumo, álcool)

#### BarreiraSedentarismo
- Barreiras identificadas pelos participantes
- Categorização por tipo
- Intensidade das barreiras

#### EstrategiaPrevencao
- Estratégias propostas para combater o sedentarismo
- Classificação por tipo (individual, institucional, comunitária)
- Recursos necessários e responsáveis

## Tecnologias Utilizadas

- **Backend**: Django 5.2.4
- **Frontend**: Bootstrap 5.3.0, Chart.js
- **Banco de Dados**: SQLite (desenvolvimento)
- **Icons**: Bootstrap Icons
- **Linguagem**: Python 3.11

## Instalação e Configuração

### Pré-requisitos
- Python 3.11+
- pip

### Passos para Instalação

1. **Clone o repositório**
```bash
git clone <url-do-repositorio>
cd sedentarismo_site
```

2. **Instale as dependências**
```bash
pip install django pillow
```

3. **Execute as migrações**
```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Crie um superusuário**
```bash
python manage.py createsuperuser
```

5. **Execute o servidor**
```bash
python manage.py runserver
```

6. **Acesse o site**
- Site: http://localhost:8000
- Admin: http://localhost:8000/admin

## Dados de Exemplo

O projeto inclui um script para criar dados de exemplo:

```bash
python manage.py shell -c "exec(open('create_sample_data.py').read())"
```

Isso criará:
- 5 participantes de exemplo
- Questionários IPAQ preenchidos
- Indicadores de saúde
- Barreiras ao sedentarismo
- Estratégias de prevenção

## Administração

O painel administrativo Django permite:
- Gerenciar participantes da pesquisa
- Visualizar e editar questionários IPAQ
- Acompanhar indicadores de saúde
- Categorizar barreiras identificadas
- Gerenciar estratégias de prevenção

### Usuário Admin Padrão
- **Usuário**: admin
- **Senha**: admin123

## Estrutura de Arquivos

```
sedentarismo_site/
├── core/                   # App principal
│   ├── views.py           # Views das páginas
│   ├── urls.py            # URLs do core
│   └── ...
├── pesquisa/              # App da pesquisa
│   ├── models.py          # Modelos de dados
│   ├── admin.py           # Configuração do admin
│   └── ...
├── templates/             # Templates HTML
│   ├── base.html          # Template base
│   └── core/              # Templates do core
├── static/                # Arquivos estáticos
├── media/                 # Uploads de arquivos
├── manage.py              # Script de gerenciamento Django
└── README.md              # Este arquivo
```

## Funcionalidades Principais

### Visualização de Dados
- Gráficos interativos com Chart.js
- Estatísticas em tempo real
- Dashboards informativos

### Análise de Sedentarismo
- Cálculo automático de METs (Metabolic Equivalent of Task)
- Classificação de níveis de atividade física
- Correlação com indicadores de saúde

### Gestão de Estratégias
- Categorização por tipo de intervenção
- Acompanhamento de implementação
- Recursos necessários

## Contribuição

Para contribuir com o projeto:

1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## Licença

Este projeto é desenvolvido para fins acadêmicos e de pesquisa no IFSULDEMINAS - Campus Muzambinho.

## Contato

- **Instituição**: IFSULDEMINAS - Campus Muzambinho
- **Email**: pesquisa@muz.ifsuldeminas.edu.br
- **Telefone**: (35) 3571-5000

## Agradecimentos

Agradecemos ao Professor Adolfo Carvalho, da área de Linguagens de Programação, e aos Professores João Carlos e Talita, da área de Educação Física, pelo apoio e valiosa orientação nesta pesquisa.

