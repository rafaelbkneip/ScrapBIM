#Importar biblioteca
import xlsxwriter

#Definir função
def verificacao (lista, termos_lista):

    #Definir auxiliar
    filtrados = []

    #Percorrer lista final
    for i in range(len(lista)):

        for x in range(len(lista[i])):
                
                #Percorrer lista de termos essenciais
                for j in range (len(termos_lista)):

                    filtrado_aux = []
                    
                    #Comparar com termos essenciais
                    if((lista[i][x][0].upper()).find(termos_lista[j].upper())!= -1):
                        filtrado_aux.append(lista[i][x])
                        filtrados.append(filtrado_aux)

                        break;

    print("A base final filtrada possui ", len(filtrados), " elementos")

    return filtrados