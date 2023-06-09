# NLP_Project_D3TOP

Repositório do Projeto de NLP Fast and automated sensory analysis
IFSP Campinas
Alunas: Mariana Cabride (CP3016625) e Renata Rabelo (CP301634X)

Objetivo
Este projeto utiliza NLP para criar léxicos descritivos de produtos alimentícios e bebidas, facilitando análises sensoriais e pesquisas de consumidores e realizar a previsão do score baseado em descrições. 

Dados
O modelo foi treinado usando dados extraídos dos sites WhiskyAdvocate e WhiskyCast. A coleta dos dados foi feita por pesquisadores da Virginia Tech, com a colaboração do Prof. Jacob Lahne e sua aluna Leah M. Hamilton, que compilaram informações sobre as destilarias e o país de origem dos uísques a partir da Wikipedia e da Flaviar.

As variáveis presentes na base são:
*   ID (Número de identificação do produto)
*   Name (Nome do uísque avaliado)
*   Std.Cat (Tipo de uísque)
*   Data.Source (Origem do dado: WhiskyAdvocate ou WhiskyCast)
*   Score (Nota fornecida pelo consumidor na avaliação do uísque)
*   Origin (País de origem do uísque)
*   ABV (Alcohol by Volume, corresponde a quantidade de álcool na bebida )
*   Price (Preço do uísque)
*   Description (Avaliação do uísque)
*   Word.Count (Contagem de palavras)
*   Date (Data de avaliação)
*   Brand (Brand do uísque)

Tratamento e Modelagem
A coluna Description (avaliação do uísque) foi pré-processado (etapas de normalização, tokenização e lematização) e transformado com a utilização da técnica TF-IDF. 
Em seguida, utilizamos o modelo LightGBM com o objetivo de prever o Score (Nota fornecida pelo consumidor na avaliação do uísque) baseado em sua descrição. 

Todos os passos descritos podem ser visualizados na íntegra neste notebook

Deploy
A ferramenta Streamlit foi usada para disponibilizar o modelo online. O arquivo app.py por sua vez é o responsável por chamar as funções necessárias para o funcionamento do aplicativo hospedadp na plataforma. O aplicativo pode ser consultado no seguinte link:  https://rerabelo-nlp-project-d3top-app-awpcr4.streamlit.app/
