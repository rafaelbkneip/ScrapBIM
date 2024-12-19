#Importações
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.keys import Keys

#Definir função
def scraping(tubos, shared_list, complementares_lista):

    #Definir opções para o navegador
    options = Options()
    options.add_experimental_option("detach", True)
    navegador = webdriver.Chrome(options=options)
    navegador.maximize_window()

    sleep(10)
    
    #Iniciar variáveis
    pesquisa_lista = []
    descricao = []
    titulos = []
    preco = []
    site = []

    #Definir termos para pesquisa
    for i in range(len(tubos)):

        pesquisa = ""

        for j in range (len(tubos[i][0].split(" "))):
                
            if ((j)!= len(tubos[i][0].split(" "))):
                    pesquisa = pesquisa + tubos[i][0].split(" ")[j] + "%20" 
            else:
                    pesquisa = pesquisa + tubos[i][0].split(" ")[j]

        pesquisa_lista.append(pesquisa)
    
    #Definir termos complementares
    aux = ""

    for i in range(len(complementares_lista)):
         
          aux = aux + complementares_lista[i] + "%20"

     #Realizar as buscas
    for j in range(len(pesquisa_lista)):

        navegador.get("https://www.casamaisfacil.com.br/"+ aux +pesquisa_lista[j]+"?map=ft")

        sleep(5)

        #Título dos produtos
        titulos_elementos = navegador.find_elements(By.CLASS_NAME, 'sc-179vp7w-0')
        for i in range(len(titulos_elementos)):
            titulos.append(titulos_elementos[i].text)

        #Preço dos produtos
        preco_elementos = navegador.find_elements(By.CLASS_NAME, 'sc-1k6l6w6-0')
        for i in range(len(preco_elementos)):
            try:
                preco.append(preco_elementos[i].text.split("\n")[1])
            except:
                preco.append(preco_elementos[i].text)

        #Descricao
        for i in range(len(titulos_elementos)):
            descricao.append(tubos[j][0])
            site.append("Mais Fácil")
        
    lista_final = []
    lista_final_aux = []

    #Montar a base final
    for i in range(len(titulos)):

        #Auxiliar
        lista_final_aux = []

        lista_final_aux.append(titulos[i])
        lista_final_aux.append(preco[i])
        lista_final_aux.append(descricao[i])
        lista_final_aux.append(site[i])
        lista_final.append(lista_final_aux)

    #Adicionar a lista compartilhada    
    shared_list.append(lista_final)