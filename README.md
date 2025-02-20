# --Calculadora-Python
# Calculadora Simples

Este é um projeto simples de uma calculadora utilizando a biblioteca Tkinter do Python para a criação da interface gráfica. A calculadora realiza operações básicas de adição, subtração, multiplicação e divisão.

## Funcionalidades

- Adição de dois números
- Subtração de dois números
- Multiplicação de dois números
- Divisão de dois números (tratamento de divisão por zero)

## Pré-requisitos

- Python 3.x instalado

## Como executar

1. Clone este repositório:
    ```sh
    git clone https://github.com/seu_usuario/calculadora-simples.git
    ```

2. Navegue até o diretório do projeto:
    ```sh
    cd calculadora-simples
    ```

3. Execute o script `calculadora.py`:
    ```sh
    python calculadora.py
    ```

## Estrutura do Código

- **Importações:** Importa a biblioteca Tkinter.
- **Função `calcular(operacao)`:** Realiza a operação matemática baseada no operador passado como argumento. Atualiza o label de resultado ou exibe uma mensagem de erro em caso de entrada inválida ou divisão por zero.
- **Configuração da Janela Principal:** Cria a janela principal da interface gráfica com Tkinter, define o título e o tamanho.
- **Campos de Entrada:** Cria campos de entrada para os números a serem operados.
- **Botões de Operação:** Cria botões para cada operação matemática (adição, subtração, multiplicação e divisão).
- **Label de Resultado:** Cria um label para exibir o resultado das operações.
- **Loop Principal:** Inicia o loop principal da interface gráfica.

## Uso

1. Insira os números nos campos "Primeiro número" e "Segundo número".
2. Clique no botão da operação matemática desejada (+, -, *, /).
3. O resultado será exibido abaixo dos botões de operação.


