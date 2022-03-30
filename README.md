# Web_Scraping_forecast_ONS

## Script para baixar dados diários de previsão de precipitação do ONS 

Script para baixar dados diários de previsão de precipitação do ONS (Operador Nacional do Sistema Elétrico).                        
                                                                                                                    
Dados de previsão já com a metodologia de remoção de BIAS (viés) utilizada pelo ONS.                       
                                                                                                                    
Script que realiza o download dos dados diários do ONS em arquivos zipados no formato _.txt_.

A técnica utilizada aqui foi a WEB Scraping, pois a ONS não disponibiliza esses dados via ftp ou API.

### Os dados são dos modelos

+ **IFS** - Integrated Forecast System | ECMWF
+ **ETA** - Eta Model | CPTEC/INPE
+ **GEFS** - Global Ensemble Forecast System | NCEP               
                                                                                                                    
A técnica utilizada aqui foi a WEB Scraping, pois o ONS não disponibiliza esses dados via ftp ou API.

PS1: O objetivo deste código não é violar o servidor da ONS e sim automatizar o processo download para otimizar o as rotinas operacionais diárias.

PS2: Crie rotinas combinando Web Scraping, Shell script e crontab para verificar quando os produtos de precipitação da ONS estiverem disponíveis assim que disponibilizados no site. 

PS3: Otimize esse código o quanto quiser. Não programo em python, não gosto de python. 


