#!/usr/bin/python

#====================================================================================================================#
#                         Script para baixar dados diários dos acumulados de precipitação do ONS                     #
#                                                                                                                    #
#                            Dados de previsão já com a metodologia de remoção de BIAS (viés)                        #
#                                                                                                                    #
#                       Script que realiza o download dos dados diários do ONS zipados no formato .txt.              # 
#                                                                                                                    #
#            A técnica utilizada aqui foi a WEB Scraping, pois a ONS não disponibiliza esses dados via ftp ou API.   #
#                                                                                                                    #
#                                   Mateus Dias Nunes @WorldSE - Março de 2022                                       # 
#                                                                                                                    #
#                                             mateus.dias@worldse.com.br                                             #
#====================================================================================================================#
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from pathlib import Path
import http.cookiejar as cookielib


#====================================================================================================================#

print('--------------------------------------------------------------')
print('             Dados ONS Download - Script started              ')
print('--------------------------------------------------------------')

USER_path='/home/mateusdiasnunes/Drive/meteorologia/worldSE/'

navegador=webdriver.FirefoxProfile()

navegador.set_preference("browser.download.folderList",2)
navegador.set_preference("browser.download.manager.showWhenStarting",False)
navegador.set_preference("browser.download.dir", USER_path)
navegador.set_preference("browser.helperApps.neverAsk.saveToDisk","application/octet-stream")
navegador=webdriver.Firefox(firefox_profile=navegador,executable_path=GeckoDriverManager().install()) #

wait = WebDriverWait(navegador, 20)

#link acesso ONS
#link = 'https://pops.ons.org.br/ons.pop.federation/?wa=wsignin1.0&wtrealm=https%3a%2f%2fsintegre.ons.org.br%2f_trust%2fdefault.aspx&wctx=https%3a%2f%2fsintegre.ons.org.br%2fsites%2f9%2f38%2f_layouts%2f15%2fAuthenticate.aspx%3fSource%3d%252Fsites%252F9%252F38%252Fpaginas%252Fservicos%252Fhistorico%252Dde%252Dprodutos%252Easpx&wreply=https%3a%2f%2fsintegre.ons.org.br%2f_trust%2fdefault.aspx'
link = 'https://bit.ly/3uFFmtl' #utilizamos o bitly para encurtar o link da página para login no sintegre
navegador.get(url=link)
sleep(4)


print('---------------------------------------------------------------------------------------')
print('                    Preencher o primeiro campo (username)                              ')
print('	                        e clicar no botão AVANÇAR                                    ')
print('---------------------------------------------------------------------------------------')

#---------------------------------------------------------------------------------------
username = 'joaomaria@empresa.com.br'  #dados do usuário
password = '123456789'

campo_username = navegador.find_element_by_css_selector('#username')  #preencher campo do #username
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
bottom_cookie = navegador.find_element(By.XPATH,cookie).click()
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
	bottom_downlod = navegador.find_element(By.XPATH,id_xpath)
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
