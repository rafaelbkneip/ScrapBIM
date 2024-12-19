
#Importar bibliotecas
import multiprocessing 
from multiprocessing.managers import BaseManager
import csv
import time

#Importando funções
import verificacao
import salvar_arquivo
import mais_facil
import leroy_merlin
import max_obras

#Iniciar contagem de tempo
inicio = time.time()

#Criando classe para paralelização
class CustomManager(BaseManager):
    pass

#Definindo main
if __name__ == "__main__": 

    processes = []

    CustomManager.register('list', list)
    with CustomManager() as manager:
        # create a shared set instance
        shared_list = manager.list()

    #Definindo lista de termos complementares
    complementares = input("Digite os termos complementares, separados por vírgula sem espaço entre eles: ")
    complementares_lista = complementares.split(",")
    print(complementares_lista)

    #Definindo lista de termos essenciais
    essenciais = input("Digite os termos essenciais, separados por vírgula sem espaço entre eles: ")
    essenciais_lista = essenciais.split(",")
    print(essenciais_lista)

    lista = []

    #Obtendo os dados da planilha
    with open("Tabela de tubos.csv", newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            print((row))
            lista.append(row)

    #Excluir cabeçalho
    lista.pop(0)
    lista.pop(0)

    #Iniciar a paralelização
    with CustomManager() as manager:

        #Criar lista compartilhada
        shared_list = manager.list()
        processes = []

        #Leroy Merlin
        p = multiprocessing.Process(target=leroy_merlin.scraping, args=(lista, shared_list, complementares_lista)) 
        processes.append(p)

        #Mais Fácil
        p = multiprocessing.Process(target=mais_facil.scraping, args=(lista, shared_list, complementares_lista)) 
        processes.append(p)

        #Max Obras
        p = multiprocessing.Process(target=max_obras.scraping, args=(lista, shared_list, complementares_lista)) 
        processes.append(p)

        #Iniciar processos
        for p in processes:
            p.start()

        #Juntar processos
        for p in processes:  
            p.join()

        #Obter dados da lista compartilhada
        shared_list= shared_list._getvalue()
    
        #Salvar base de dados final
        salvar_arquivo.salvar(shared_list, "Base de dados final.xlsx")

        #Filtrar a lista com base nos termos essenciais
        unica_filtrada = verificacao.verificacao(shared_list, essenciais_lista)
        
        #Salvar base de arquivos filtrados
        salvar_arquivo.salvar(unica_filtrada, "Base de dados filtrada.xlsx")

#Determinar termo de duração            
fim = time.time()
print(fim - inicio)