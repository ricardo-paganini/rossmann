# =====================
# Alterar tipo de dados
# =====================

def change_data_type(dataframe, column,data_type):
    """
    Objetivo: Alterar o tipo de dado de uma variável / feature do conjunto de dados
    
    Parâmetros solicitados: Dataframe, nome da coluna e tipo de dado
    
    Retorno: Dataframe com o tipo da variável / feature alterado
    
    Exemplo:
        
        change_data_type('Coluna1','int64')
        change_data_type('Coluna2','float64')
    """
    
    dataframe[column] = dataframe[column].astype(data_type)
          
    return None
    

