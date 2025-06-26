import streamlit as st
import pandas as pd

# Título da aplicação
st.title('Otimização de Entrega de Drone com Programação Dinâmica')

# Dados de exemplo: pacotes disponíveis para entrega
packages = {
    'ID':     [1,    2,    3,    4,    5],
    'Nome':   ['Pacote A', 'Pacote B', 'Pacote C', 'Pacote D', 'Pacote E'],
    'Peso':   [2,    3,    4,    5,    1],  # em kg
    'Valor':  [40,   50,   65,   85,   20]  # prioridade ou lucro estimado
}
df = pd.DataFrame(packages)

# Exibe tabela de pacotes
st.subheader('Pacotes Disponíveis')
st.table(df)

# Parâmetros de entrada pelo usuário
st.sidebar.header('Parâmetros da Entrega')
capacidade = st.sidebar.number_input(
    'Capacidade do Drone (kg)',
    min_value=1,
    max_value=100,
    value=10
)

# Função de Programação Dinâmica para o Knapsack 0-1
def knapsack(pesos, valores, W):
    n = len(pesos)
    # cria tabela dp (n+1) x (W+1)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if pesos[i-1] <= w:
                dp[i][w] = max(
                    dp[i-1][w],
                    dp[i-1][w - pesos[i-1]] + valores[i-1]
                )
            else:
                dp[i][w] = dp[i-1][w]

    # valor máximo
    valor_max = dp[n][W]
    # recuperação dos itens selecionados
    w = W
    selecionados = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selecionados.append(i-1)
            w -= pesos[i-1]
    selecionados.reverse()
    return valor_max, selecionados

# Botão de execução
if st.sidebar.button('Otimizar Entrega'):
    valor_max, sel = knapsack(
        df['Peso'].tolist(),
        df['Valor'].tolist(),
        capacidade
    )

    st.subheader('Resultado da Otimização')
    st.write(f'**Valor máximo obtido:** {valor_max}')
    st.write(f'**Peso total utilizado:** {sum(df.loc[sel, "Peso"])} kg')

    st.write('**Pacotes selecionados:**')
    st.table(df.loc[sel].reset_index(drop=True))

    st.success('Otimização concluída com sucesso!')
