# Inteligência Artificial para previsão de indisponibilidade

## Sobre 
Este repositório contém o código da Inteligência Artificial. Que tem o Objetivo de Analisar as Métricas, e prever o próximo resultado do sistema, assim conseguindo chegar a conclusão se o sistema ficará indisponível ou não. 

## Tecnologias 
- [Python](https://www.python.org/)
- [Jupyter Notebook](https://jupyter.org/)

## Blibliotecas 
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Sklearn LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
- [Statsmodels](https://www.statsmodels.org/stable/index.html)


# [AutoCorrelação](https://github.com/Oraculum-Fatec/api-previsao-de-indisponibilidade-sites/blob/main/AutoCorrelacao.ipynb)
Neste código foi criado um modelo de AutoCorrelaçao, que identifica a relação dos Dados colhido pelo grupo. O objetivo deste código é auxiliar na escolha da Métrica para realizar a Analise e Previsão.

# [Time Series](https://github.com/Oraculum-Fatec/api-previsao-de-indisponibilidade-sites/blob/main/Time_Series.ipynb)
Neste código esta sendo feito uma Série Temporal, para realizar a previsão do próximo resultado do sistema teste, e assim conseguir ser feito a Analise se o sistema irá falhar ou não. 

# [Time Query](https://github.com/Oraculum-Fatec/api-previsao-de-indisponibilidade-sites/blob/main/time_query.py)
Este código está colheido as Métricas do banco de dados do prometheus, para poder passar para IA de uma forma personalizada.

# [Análise de Sobrevivência](https://github.com/Oraculum-Fatec/api-previsao-de-indisponibilidade-sites/blob/main/SurvivalAnalysis.ipynb)
Este código realiza uma análise de sobrevivência dos dados de testes de carga disponíveis no arquivo ```LoadTest.csv```. O objetivo dele é prever a taxa de sobrevivência da aplicação a partir do período de tempo em que sua falha for decretada iminente. Esta análise auxiliará a IA que tenta prever a indisponibilidadde do sistema.

# [Previsão de indisponibilidade](https://github.com/Oraculum-Fatec/api-previsao-de-indisponibilidade-sites/blob/main/death_prediction_AI.py)
Este código deverá ser executado junto com a aplicação de cadastro Spring Boot disponível em outro repositório, acesse-o clicando [AQUI](https://github.com/Oraculum-Fatec/sistema-cadastro-backend).

Com o Prometheus, esta IA, treinada pelos dados do arquivo ```LoadTest.csv```, irá receber dados da aplicação Spring Boot a cada 30 segundos e a partir dos dados treinados determinará o risco atual da aplicação. Caso a aplicação apresente um nível de risco de falha elevado, a IA alertará em um canal do Slack a probabilidade de sobrevivência dos próximos 30 segundos, baseados na análise de sobrevivência anteriormente feita. Se os dados de riscos permanecerem ativos na próxima vez em que IA receber os dados, a cada acúmulo, a porcentagem indicada aumentará de acordo com a análise de sobrevivência.

Segue abaixo, as mensagens enviadas pelo slack caso a aplicação demonstre dados de risco de falha elevado no próximos 3 minutos em que o primeiro alerta é ativado:

<p align="center">
  <img alt="slack" src="dados/Slack_message.png">
</p>
