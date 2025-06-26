import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


try:
    print("Obtendo dados...")
    ENDERECO_DADOS = "https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv"

    # Buscar a base de dados CSV online do site ISP (Instituto de Segurança Pública)
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
 

except Exception as e:
    print("Erro ao obter os dados:", e)
    exit()