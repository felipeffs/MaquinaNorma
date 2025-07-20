# Máquina Norma
Simulador de Máquina Norma em Python com 3 exemplos incluídos: fatorial, multiplicação e soma.

## Como usar
1. Defina o caminho do arquivo de entrada na variável arq do arquivo principal.py
   Ex: `arq = 'exemplos/fatorial.txt'`
2. Execute `principal.py`.

## Entrada
O programa da Máquina Norma deve estar escrito em um arquivo `.txt`, seguindo a sintaxe abaixo.  
Cada linha deve conter apenas uma das instruções:

- `<numero_linha>` **ADD** `<registrador>` `<proxima_linha>`  
  Incrementa o registrador e salta para a linha indicada.

- `<numero_linha>` **SUB** `<registrador>` `<proxima_linha>`  
  Decrementa o registrador e salta para a linha indicada.

- `<numero_linha>` **ZER** `<registrador>` `<linha_se_zero>` `<linha_se_nao_zero>`  
  Testa se o registrador é zero e salta conforme o resultado.

Registradores válidos: A, B, C, D