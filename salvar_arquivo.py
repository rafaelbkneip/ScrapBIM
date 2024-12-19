
#Importar bibliotecas
import xlsxwriter

#Definir função
def salvar (lista, nome):

    #Abrir arquivo
    book = xlsxwriter.Workbook(nome)    
    #Adicionar aba 
    sheet = book.add_worksheet()  

    aux_escrita = []

    #Percorrer lista
    for i in range (len(lista)):
        for j in range(len(lista[i])):
            aux_escrita.append(lista[i][j])

    #Montar base de dados
    for j in range(len(aux_escrita)):
            sheet.write(j, 0, aux_escrita[j][0])
            sheet.write(j, 1, aux_escrita[j][1])
            sheet.write(j, 2, aux_escrita[j][2])
            sheet.write(j, 3, aux_escrita[j][3])
    
    book.close()

    print("A base final possui ", len(aux_escrita), " elementos")

    return ""