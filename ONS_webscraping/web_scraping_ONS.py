#====================================================================================================================#
#                         Script para baixar dados diários de previsão de precipitação do ONS                        #
#                                                                                                                    #
#                            Dados de previsão já com a metodologia de remoção de BIAS (viés)                        #
#                                                                                                                    #
#                       Script que realiza o download dos dados diários do ONS zipados no formato .txt.              # 
#                                                                                                                    #
#            A técnica utilizada aqui foi a WEB Scraping, pois a ONS não disponibiliza esses dados via ftp ou API.   #
#                                                                                                                    #
#                                   Mateus Dias Nunes @WorldSE - Março de 2022                                       # 
#                                                                                                                    #
#====================================================================================================================#
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from pathlib import Path
import os

#====================================================================================================================#

print('--------------------------------------------------------------')
print('             Dados ONS Download - Script started              ')
print('--------------------------------------------------------------')

USER_path='/home/username/'         #altere para o seu caminho desejado

navegador=webdriver.FirefoxProfile()
navegador.set_preference("browser.download.folderList",2)
navegador.set_preference("browser.download.manager.showWhenStarting",False)
navegador.set_preference("browser.download.dir", USER_path)
navegador.set_preference("browser.helperApps.neverAsk.saveToDisk","application/octet-stream")
navegador=webdriver.Firefox(firefox_profile=navegador,executable_path=GeckoDriverManager().install()) #

#link acesso ONS
link = 'https://bit.ly/3uFFmtl' #utilizamos o bitly.com para encurtar o link da página de login no sintegre
navegador.get(url=link)navegador.get(url=link)
sleep(4)

print('---------------------------------------------------------------------------------------')
print('                    Preencher o primeiro campo (username)                              ')
print('                          e clicar no botão AVANÇAR                                    ')
print('---------------------------------------------------------------------------------------')

#---------------------------------------------------------------------------------------
username = 'seuemail@empresa.com.br'  #seu e-mail cadastrado no ONS entre aspas simples
password = 'seu_password'             #senha do e-mail cadastrado

campo_username = navegador.find_element_by_css_selector('#username')  #aqui o código irá preencher campo do #username
sleep(2)
campo_username.send_keys(username)
sleep(2)

botao_AVANCAR = '#form\.username > input:nth-child(3)' #clicar no botão para inserir usuário
AVANCAR = navegador.find_element_by_css_selector(botao_AVANCAR).click()
sleep(4)

print('---------------------------------------------------------------------------------------')
print('           Preencher o segundo campo (password) e clicar no botão ENTRAR               ')
print('---------------------------------------------------------------------------------------')

campo_password = navegador.find_element_by_css_selector('#password')
sleep(2)
campo_password.send_keys(password)                 #navegador.maximize_window() #se o navegador utilizado for o Chrome a página deve ser maximizada nesse ponto, para o botao de acesso ficar "clicável"
sleep(2)

botao_entrar = '#form\.password > input:nth-child(6)'
ENTRAR = navegador.find_element_by_css_selector(botao_entrar).click()
sleep(10)

print('---------------------------------------------------------------------------------------')
print('                            Site ONS Sintegre Carregado                                ')
print('---------------------------------------------------------------------------------------')
print('')
print('')
print('')
print('---------------------------------------------------------------------------------------')
print('                           Clicar no botão  CONCORDO (cookies)                         ')
print('---------------------------------------------------------------------------------------')

cookie = '/html/body/form/div[12]/div/div[5]/button'
bottom_cookie = navegador.find_element_by_xpath(cookie).click()
sleep(2)

navegador.refresh() #refresh na página para garantir que os produtos sejam carregados integralmente
sleep(10)

print('---------------------------------------------------------------------------------------')
print('                Seleciona o campo "TODOS PRODUTOS" ao carregar a página                ')
print('---------------------------------------------------------------------------------------')

# IFS = //*[@id="linkarquivo-7642"], ETA = //*[@id="linkarquivo-6419"], GEFS = //*[@id="linkarquivo-6416"]

id_model = ['//*[@id="linkarquivo-7642"]','//*[@id="linkarquivo-6419"]','//*[@id="linkarquivo-6416"]']

for id_xpath in id_model:
   print("===================================================")
   bottom_downlod = navegador.find_element_by_xpath(id_xpath)
   sleep(2)
   bottom_downlod.click()
   sleep(2)
   print("===================================================")


print('---------------------------------------------------------------------------------------')
print('                     Verificando quais os arquivos foram baixados                      ')
print('---------------------------------------------------------------------------------------')

arq_ONS=['GEFS50_precipitacao14d.zip','Eta40_precipitacao10d.zip','ECMWF_precipitacao14d.zip']

for model in arq_ONS:

   my_file = Path(USER_path+model)

   if my_file.is_file():
   
      print("=======================================================")
      print("     O ARQUIVO: " +model+" FOI BAIXADO COM SUCESSO     ")
      print("=======================================================")
      # file exists
   else: 
      print("=======================================================")
      print("OCORREU UM ERRO NO DOWLOAD DO MODELO: " +model+" DO ONS")
      print("=======================================================")