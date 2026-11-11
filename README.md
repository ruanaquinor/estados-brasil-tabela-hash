

# Tabela Hash: Sistema de Emplacamento (Estados do Brasil)

## Sobre o Projeto
Este repositório contém a implementação de uma **Tabela Hash com Endereçamento em Cadeia** (vetor de listas encadeadas) desenvolvida em Python. O objetivo é armazenar as siglas dos 26 estados brasileiros, o Distrito Federal e um estado fictício em 10 posições (0 a 9).

## Lógica da Função Hash
A distribuição dos estados na tabela segue uma regra matemática baseada na Tabela ASCII:
1. A função converte as duas letras da sigla do estado para seus valores ASCII, soma os dois valores e calcula o resto da divisão por 10 (`MOD 10`).
2. **Exceção :** Por definição do sistema, a sigla `DF` (Distrito Federal) ignora o cálculo ASCII e é sempre alocada na posição `7`.
3. **Tratamento de Colisão:** Como o tamanho da tabela (10) é menor que o número de estados (28), ocorrem colisões. Elas são tratadas encadeando os itens: novos estados que caem na mesma posição são inseridos no início da lista encadeada daquele índice.

## Tecnologias Utilizadas
* Python
* Estrutura de Dados: Tabela Hash + Listas Encadeadas Simples

##  Como Executar
1. O código possui os dados cadastrados estaticamente (hard code) conforme os requisitos do projeto.
2. Execute o script no terminal: `python tabela_hash_estados.py`
3. O console exibirá a evolução da estrutura em três etapas: tabela vazia, tabela com os 27 estados reais e tabela final incluindo o estado fictício.



