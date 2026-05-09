# Painel Infância Segura
Painel interativo em **Streamlit** para visualização de dados sobre ações e políticas públicas de prevenção e enfrentamento da violência contra crianças e adolescentes no Brasil, no contexto do projeto **Infância Segura (ATRICON)**.

## Sobre o projeto
O painel organiza indicadores em múltiplas dimensões, com foco no Sistema de Garantia de Direitos da Criança e do Adolescente (SGDCA), permitindo:
- Análise por estado (UF)
- Visualização de mapas, gráficos e métricas
- Consulta de dados de governança, prevenção, repressão/acolhimento, estatísticas, conselhos tutelares e FMDCA
- Download do relatório completo em PDF

## Funcionalidades
- Navegação por páginas temáticas:
  - `Visão Geral`
  - `Governança`
  - `Prevenção`
  - `Repressão e Acolhimento`
  - `Dados e Estatística`
  - `Conselho Tutelar`
  - `FMDCA`
- Filtro por UF na barra lateral
- Gráficos interativos com Plotly (pizza, barras e mapas do Brasil)
- Carregamento de dados locais em CSV com cache (`st.cache_data`)
- Interface customizada com tema Streamlit, CSS e assets próprios

## Tecnologias
- Python
- Streamlit
- Plotly
- Pandas

## Estrutura do repositório
```text
.
├── app.py                        # Entrada principal da aplicação Streamlit
├── import_data.py                # Carga, limpeza e joins dos dados
├── graficos.py                   # Funções reutilizáveis para gráficos
├── visao_geral.py                # Página Visão Geral
├── governanca.py                 # Página Governança
├── prevencao.py                  # Página Prevenção
├── repressao.py                  # Página Repressão e Acolhimento
├── dados_estatistica.py          # Página Dados e Estatística
├── conselho_tutelar.py           # Página Conselhos Tutelares
├── fmdca.py                      # Página FMDCA
├── dados/                        # Base de dados em CSV
├── assets/                       # Logos e ícones do projeto
├── pdf/                          # Relatório para download
├── styles.css                    # Estilos adicionais da aplicação
├── .streamlit/config.toml        # Configuração de tema/servidor Streamlit
├── requirements.txt              # Dependências Python
└── packages.txt                  # Pacotes de sistema (deploy)
```

## Pré-requisitos
- Python 3.10+ (recomendado)
- `pip`

## Instalação e execução local
1. Clone o repositório:
```bash
git clone <URL_DO_REPOSITORIO>
cd painel-infancia-segura
```

2. Crie e ative um ambiente virtual:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute o painel:
```bash
streamlit run app.py
```

5. Acesse no navegador:
```text
http://localhost:8501
```

## Dados utilizados
Os dados são carregados a partir de arquivos CSV na pasta `dados/`, incluindo:
- `capitais.csv`
- `entidades.csv`
- `levantamentos.csv`
- `respostas.csv`
- `perguntas.csv`
- `opcoes.csv`
- `resposta_opcoes.csv`
- `quantidade_conselho_tutelar.csv`
- `dados_fmdca.csv`

## Observações de ambiente
- A página de conselho tutelar utiliza locale `pt_BR.UTF-8`.
- Em ambientes Linux de deploy, os pacotes de sistema necessários estão em `packages.txt` (`locales` e `locales-all`).

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## Autor
William Gomes
