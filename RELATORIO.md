# RELATÓRIO DE SISTEMATIZAÇÃO — LABORATÓRIO ESTATÍSTICO COMPUTACIONAL

## 1. Identificação
* **Componente(s):** Antônio Francisco Reis dos Santos
* **Projeto:** Laboratório Estatístico Interativo — Análise do Dataset de Uso da Frota (2025)

## 2. Link dos Dados Crus
* **Fonte Original:** Dataset de Uso da Frota (`uso_da_frota_2025.csv`) processado a partir de registros operacionais de transporte.

---

## 3. Decisões de Implementação do Núcleo Estatístico ("Na Unha")
Para atender aos requisitos da atividade, as principais medidas descritivas e analíticas foram programadas sem o uso de funções estatísticas prontas de bibliotecas como NumPy, SciPy ou `statistics`, utilizando apenas estruturas nativas do Python.

* **Média Aritmética:** Acumula a soma total dos valores válidos e divide pela contagem de registros ($n = 8.450$).
* **Mediana:** Dados ordenados com o método `sorted()`, calculando o ponto central exato (ou a média dos dois centrais).
* **Variância Amostral e Desvio Padrão:** Calculados somando o quadrado dos desvios em relação à média e dividindo por $n - 1$ para correção amostral.
* **Regressão Linear Simples:** Utilizou-se o Método dos Mínimos Ordinários (MQO) para calcular manualmente a inclinação da reta ($a$) e o intercepto ($b$).

---

## 4. Resultados Principais
* **Total de registros válidos:** 8.450 viagens
* **Média manual por viagem:** 6,99 passageiros
* **Mediana manual:** 2,0 passageiros
* **Variância amostral manual:** 69,48
* **Desvio padrão amostral manual:** 8,34
* **Equação da Reta de Regressão:** $\hat{Y} = -0,0054X + 7,2732$

---

## 5. As 3 Descobertas Estatísticas do Dataset (Módulo 6)
1. **Forte Assimetria Positiva na Ocupação:** A média de passageiros (6,99) é superior à mediana (2,0), comprovando que a maioria das viagens opera com baixa ocupação, enquanto poucas viagens de alta capacidade puxam a média para cima.
2. **Validação da Convergência e Normalidade:** A simulação de Monte Carlo demonstrou a Lei dos Grandes Números e o Teorema Central do Limite com sucesso.
3. **Estabilidade Temporal da Demanda:** O coeficiente de inclinação próximo de zero ($a = -0,0054$) na regressão linear indica estabilidade na demanda ao longo do período *(correlação não implica causalidade)*.
