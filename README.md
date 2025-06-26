# Otimiza-o-
Link para aplicação: https://gwuyez8ewkikqgelc35kag.streamlit.app/

Escolhi um caso real de entrega por drone, onde cada viagem ao cliente tem restrição de peso e cada pacote tem um valor (lucro ou prioridade). A Programação Dinâmica (PD) é ideal para resolver esse tipo de Knapsack 0-1, pois calcula, de forma incremental, a melhor combinação de pacotes que maximize o valor total sem ultrapassar a capacidade do drone, evitando recalcular subproblemas já resolvidos.

Na interface:

Exibe uma tabela com pacotes disponíveis.

Recebe a capacidade máxima do drone (kg) via barra lateral.

Executa o algoritmo de PD para o problema de Knapsack.

Mostra o valor máximo obtido, peso total usado e quais pacotes foram selecionados.
