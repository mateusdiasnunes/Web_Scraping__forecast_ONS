# Web_Scraping_forecast_ONS

## Script para baixar dados diários de previsão de precipitação do ONS 

Script para baixar dados diários de previsão de precipitação do ONS (Operador Nacional do Sistema Elétrico).                        
                                                                                                                    
Dados de previsão já com a metodologia de remoção de BIAS (viés) utilizada pelo ONS.                       
                                                                                                                    
Script que realiza o download dos dados diários do ONS em arquivos zipados no formato _.txt_.

A técnica utilizada aqui foi a WEB Scraping, pois a ONS não disponibiliza esses dados via ftp ou API.

O objetivo é automatizar o download para quem não tem acesso aos dados de previsão de 14 dias do IFS e assim aplicar a metodologia de remoção de viés do ONS.

### Os dados são dos modelos

+ **IFS** - Integrated Forecast System | ECMWF
+ **ETA** - Eta Model | CPTEC/INPE
+ **GEFS** - Global Ensemble Forecast System | NCEP               
                                                                                                                    
A técnica utilizada aqui foi a WEB Scraping, pois o ONS não disponibiliza esses dados via ftp ou API.

Não esqueça de instalar as bibliotecas necessárias.

Não esqueça de trocar o PATH.

PS1: O objetivo deste código não é violar o servidor da ONS e sim automatizar o processo download para otimizar o as rotinas operacionais diárias.

PS2: Crie rotinas combinando Web Scraping, Shell script e crontab para verificar quando os produtos de precipitação da ONS estiverem disponíveis assim que disponibilizados no site, depois ainda criando algum código que faça uma "varredura" verificando a existência dos arquivos (após o download), renomeando-os pela data atual e assim plotando seus produtos.

PS3: Otimize esse código o quanto quiser. Não programo em python, não gosto de python. 


