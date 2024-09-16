# DS_MapReduceGrep

## MapReduce - Grep Distribuído

### Implementação de modelagem para o framework MapReduce, explorando conceito de um Grep Distribuído.

MapReduce é um modelo de programação utilizado para processar e gerar grandes conjuntos de dados de forma distribuída em um ambiente de cluster de computadores. Ele foi popularizado pelo Google para lidar com grandes volumes de dados em seus sistemas.

Este projeto implementa um sistema MapReduce para buscar e filtrar linhas em arquivos de texto com base em um padrão fornecido. Ele suporta buscas simples e avançadas usando expressões regulares (regex).

#### Estrutura do Projeto

FileGenerator.py: (Opcional) Gera e divide arquivos de texto para teste. Não necessário se você já possui arquivos de entrada. Nesse exemplo Utilizamos Arquivos de entrada com textos já fornecidos previamente.

MapReduce.py: Implementa a lógica do MapReduce para buscar padrões nos arquivos de entrada.

#### Arquivos de Entrada

Coloque os arquivos de texto que você deseja processar na mesma pasta que o script MapReduce.py. Nomeie os arquivos como input0.txt, input1.txt, etc.

### Exemplo de Uso

> [!TIP]
> Arquivos de entrada.

- files = ["input0.txt", "input1.txt", "input2.txt", "input3.txt"]

> [!TIP]
> Padrão a ser buscado. Neste exemplo, a linha deve terminar com 'cbb' usando a expressão regular '$'.

- pattern = "cbb$"

> [!TIP]
> Define se usa regex (True para usar expressões regulares, False para busca simples).

- use_regex = True

## **Desenvolvido por:**

Aluno: [`Ramon Oliveira`](https://github.com/raszz)
