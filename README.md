# Consumindo api - forecast

1. Crie um programa em Python que consuma os dados de previsão do tempo (weather) da [API de Previsão do Tempo](https://hgbrasil.com/status/weather). 
- O sistema deverá fornecer a previsão do tempo, somente para estados e cidades brasileiras;
- O sistema permitirá que o usuário escolha um estado ou cidade para consulta;
- O sistema apresentará para o usuário as seguintes informações fornecidas pela API Weather:
    - Temperatura atual em graus celsius (ºc)
    - Data e Hora da consulta
    - Descrição do tempo atual
    - Se está de dia ou de noite
    - Umidade
    - Velocidade do vento
    - Nascer e pôr do sol
    - Condição de tempo atual.
    - Médias das temperaturas máxima e mínima semanal, baseado nos dados de previsão climática (forecast)

O sistema deverá manter em um sistema de gerenciamento de banco de dados do SQLite,  o histórico de consultas feito pelo usuário contendo os seguintes dados: data e hora da consulta, Temperatura, Umidade, descrição da condição do tempo, velocidade do vento em Km/h.
O sistema deverá manter um banco de dados de códigos WOEID para estados e cidades brasileiras. Para tal, faça o download do [conjunto de dados da Geoplanet](https://archive.org/details/geoplanet_data_7.4.1.zip) limpe, organize os dados e armazene no banco de dados SQLite, de tal forma que seja possível que o usuário pesquise por nome ou código da cidade ou estado e o sistema recupere o WOEID para consultar a API.

## Importante: 
A consulta da API de previsão do tempo é feita através do código WOEID que é um identificador de referência de 32 bits, originalmente definido pela GeoPlanet e agora utilizado pela Yahoo!, que identifica qualquer característica da Terra. A Yahoo! não fornece mais a API  de consulta do código WOEID, porém, o conjunto de dados legado está disponível para download em <https://archive.org/details/geoplanet_data_7.4.1.zip> sob a licença Creative Commons Attribution 3.0.

