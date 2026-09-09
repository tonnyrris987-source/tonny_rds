def calcular_media(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

def calcular_mediana(lista):
    if not lista:
        return 0
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    meio = n // 2
    if n % 2 == 0:
        return (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2
    return lista_ordenada[meio]

def calcular_variancia(lista, amostral=True):
    if len(lista) <= 1:
        return 0
    media = calcular_media(lista)
    soma_quadrados = sum((x - media) ** 2 for x in lista)
    divisor = (len(lista) - 1) if amostral else len(lista)
    return soma_quadrados / divisor

def calcular_desvio_padrao(lista, amostral=True):
    return calcular_variancia(lista, amostral) ** 0.5

def regressao_linear_simples(x, y):
    n = len(x)
    media_x = calcular_media(x)
    media_y = calcular_media(y)
    
    numerador = sum((x[i] - media_x) * (y[i] - media_y) for i in range(n))
    denominador = sum((x[i] - media_x) ** 2 for i in range(n))
    
    if denominador == 0:
        return 0, media_y
        
    inclinacao = numerador / denominador
    intercepto = media_y - inclinacao * media_x
    return inclinacao, intercepto
