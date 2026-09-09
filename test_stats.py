import numpy as np
from minhastats import calcular_media, calcular_mediana, calcular_variancia, calcular_desvio_padrao

def test_media():
    dados = [10, 20, 30, 40, 50]
    assert calcular_media(dados) == float(np.mean(dados))

def test_mediana():
    dados = [10, 20, 50, 30, 40]
    assert calcular_mediana(dados) == float(np.median(dados))

def test_variancia():
    dados = [1, 2, 3, 4, 5]
    assert abs(calcular_variancia(dados, amostral=True) - np.var(dados, ddof=1)) < 1e-6

def test_desvio_padrao():
    dados = [5, 10, 15, 20]
    assert abs(calcular_desvio_padrao(dados, amostral=True) - np.std(dados, ddof=1)) < 1e-6
