from click import password_option
from Grupo import Grupo
import pandas as pd    

def criando_pkl_jogos(nomes):
    lista_zeros = ['---' for i in range(4)]
    
    data = {nomes[0][0]:lista_zeros, 
            nomes[0][1]:lista_zeros,
            nomes[0][2]:lista_zeros,
            nomes[0][3]:lista_zeros}

    df = pd.DataFrame(data, index=nomes[0])
    
    print(df)
    print()
    
def criando_pkl_selecoes(nomes):
    
    data_selecoes = {'GrupoA':nomes[0],
                     'GrupoB':nomes[1],
                     'GrupoC':nomes[2],
                     'GrupoD':nomes[3],
                     'GrupoE':nomes[4],
                     'GrupoF':nomes[5],
                     'GrupoG':nomes[6],
                     'GrupoH':nomes[7],}
    
    dataFrame_selecoes = pd.DataFrame(data_selecoes)
    
    dataFrame_selecoes.to_pickle('dataset/Selecoes.plk')
    
    dados_selecoes = pd.read_pickle('dataset/Selecoes.plk')
    
    print(dados_selecoes)
    print()

if __name__ == '__main__':
    
    nomes = [[] for i in range(8)]
    
    selecoes = pd.read_csv('dataset/selecoes.csv', header=None)
        
    linhas = selecoes.shape[0]
    colunas = selecoes.shape[1]
        
    for i in range(linhas):
        for j in range(colunas):
            nomes[i].append(selecoes[j][i])
    
    criando_pkl_jogos(nomes)
    criando_pkl_selecoes(nomes)
    