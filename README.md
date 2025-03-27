# Product Scraper

Este projeto é um web scraper que coleta informações de produtos de um site específico e as armazena em um arquivo de texto.

## 🛠️ Tecnologias Utilizadas

* Python
* Requests
* BeautifulSoup (BS4)

## 📌 Como Funciona?

O script acessa a página inicial da loja e extrai os produtos listados.
Ele percorre várias páginas da loja coletando informações sobre cada produto.
O nome e o preço dos produtos são armazenados em um dicionário.
No final, os dados coletados são salvos no arquivo products.txt.

## 📦 Instalação

Antes de rodar o script, certifique-se de ter o Python instalado e instale as dependências necessárias:
```bash
pip install requests beautifulsoup4
```

## 🚀 Como Usar

Para executar o scraper, basta rodar o seguinte comando no terminal:
```bash
python scraper.py
```

O script começará a coletar os produtos do site e armazenará os resultados no arquivo products.txt.

## 🔍 Exemplo de Saída (products.txt)

Produto 1 - R$ 99,90
Produto 2 - R$ 149,90
Produto 3 - R$ 79,50
...
