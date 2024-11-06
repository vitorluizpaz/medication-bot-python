# Bot de Consulta de Medicamentos

Este projeto é um bot desenvolvido em Python que utiliza Selenium para automatizar a busca de preços de medicamentos específicos em várias farmácias online. O bot coleta preços para medicamentos como **Depakote**, **Lítio** e **Pinazan** em farmácias selecionadas e exibe os resultados.

## Funcionalidades

- Solicita a quantidade desejada de medicamentos específicos.
- Acessa os sites das farmácias e consulta os preços dos medicamentos informados.
- Exibe os preços de cada farmácia consultada no terminal.

## Farmácias Suportadas

- Catarinense
- Panvel
- Preço Popular
- São João
- (Droga Raia – requer login e senha para acesso)

## Pré-requisitos (Os 3 devem ser compatíveis.)

- Python
- Selenium
- Driver do navegador adicionado ao PATH(Neste projeto foi usado ChromeDriver para Google Chrome, por exemplo)

## Como usar

- Se desejar utilizar a consulta na droga raia, descomentar o trecho de código
correspondente a ela em main.py e alterar login e senha no arquivo 
./farmacias/droga_raia
- Executar main.py da pasta raiz usando python
- Insira a quantidade de medicamento(caixas) desejadas