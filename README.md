# Web Scraping usando Scrapy, Pandas, MySQL, Streamlit e Plotly

Esse projeto é uma ETL para pegar dados de alugueis da OLX da região de grande florianópolis, aplicar algumas transformações, inserir em um banco de dados e depois ler esses dados e criar um dashboard de análise.

## Indicadores analisados
 - Valor médio por Cidade
 - Valor médio por Bairro
 - Valor médio Geral
 - Quantidade de Imóveis extraídos
 - Quantidade de Cidades disponíveis
 - Quantidade de Bairros disponíveis

Porém a base da dados extraída existe muito mais informações que podemos analisar.

## Instalação

Para usar o código, siga os passos abaixo:

1. Clone o repositório:

    ```bash
    git clone https://github.com/MarcusMix/webscraping-python
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd olx
    ```

3. Instale as dependências necessárias (requer `pip`):

    ```bash
    pip install scrapy
    pip install streamlit
    pip install plotly.express
    pip install sqlalchemy
    ```
4. Entre na pasta do dashboard:

    ```bash
    cd dashboard
    ```
5. Start no projeto:

    ```bash
    streamlit run main.py
    ```

## Screenshot

### Web scraping com Scrap

![Scrapy em ação](https://i.imgur.com/IkdDFWA.png)

### Transformação e limpeza dos dados com Pandas

![ETL](https://i.imgur.com/wEAbYLt.png)

### Utilização do Banco de dados MySQL

![SGBD MYSQL](https://i.imgur.com/lTGXyH4.png)

### Dashboard usando Streamlit e Plotly

![imagem 1](https://i.imgur.com/q0HrjS3.png)
<p><i>Headline do dashboard com KPIs</i></p>

![imagem 2](https://i.imgur.com/wHvFxn0.png)
<p><i>Grafico de pizza Valor médio por Cidade</i></p>

![imagem 3](https://i.imgur.com/wKFVwqX.png)
<p><i>Valor médio por bairro</i></p>

![imagem 4](https://i.imgur.com/St0C5pm.png)
<p><i>Valor médio por bairro filtrado</i></p>

## Exemplos de Uso

Neste exemplo, o intuito foi extrair todas as informações relacionadas a alugueis da grande florianópolis, e tratar esses dados, dessa forma podemos ter uma análise precisa da situação atual dos imóveis.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](https://choosealicense.com/licenses/mit/) para mais detalhes.

### Autor

Desenvolvido por MarcusMix

---

### Referências

- [Documentação do Python](https://docs.python.org/3/)
- [Pandas Library](https://pandas.pydata.org/)
- [openpyxl Library](https://openpyxl.readthedocs.io/en/stable/)
- [Streamlit](https://openpyxl.readthedocs.io/en/stable/)
- [Plotly](https://openpyxl.readthedocs.io/en/stable/)

---

