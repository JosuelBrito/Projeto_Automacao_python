# Passo a passo do projeto
# Passo1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

#biblioteca mouse teclado tela do computador
#pip install pyautogui
import pyautogui
import time #bliblioteca de tempo

pyautogui.PAUSE = 0.7 #pausar a cada comando do pyautogui

#pyautogui.click -> clicar em algum lugar da tela
#pyautogui.write -> escrever um texto
#pyautogui.press -> pressionar 1 tecla do teclado

#abrir o navegador(chrome)

#pyautogui biblioteca de automação

pyautogui.press("win") #pressionar a teclado do windows
pyautogui.write("chrome") #digitar o navegador
pyautogui.press("enter")

pyautogui.click(x=962, y=638)#selecionando o

time.sleep(3)

pyautogui.click(x=267, y=68)

#variavel link
#entrar no site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link) #selecionando a variavel com  o link atribuido
pyautogui.press("enter") #pressionando enter


#dar uma pausa pouco maior em caso de internet lenta
time.sleep(3)

#-----------------------LOGIN----------------
# Passo 2: Fazer login
pyautogui.click(x=1028, y=412)#selecionando o campo email com a posição
pyautogui.write("")

#escrever a senha

pyautogui.press("tab")
pyautogui.write("208317@Jb")
pyautogui.press("tab")
pyautogui.press("enter")

#clicar no botão de logar


time.sleep(3)

# Passo 3: Importar a base de dados
#pip install pandas numpy openpyxl
#ferramenta para importar a base de dados é o PANDAS

import pandas
tabela = pandas.read_csv("produtos.csv")#read para leitura do arquivo

print(tabela)


# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o processo de cadastro até acabar a base de dados



