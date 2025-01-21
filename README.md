# dns-crawler

## Visão Geral


## Estrutura do Projeto

```
dns-crawler/
    ├── Dockerfile
    ├── docker-compose.yml
    ├── README.md/
    ├── GeoLite2-ASN.mmdb
    ├── GeoLite2-Country.mmdb
    ├── requirements.txt
    ├── pyproject.toml
    ├── pyproject.lock
    ├── config.docker.yml
    ├── config.yml
    ├── dns_crowler_database.db
    ├── all-domains.txt
    ├── data/
    │   ├── results.json
    │   └── results.json
    └── schema/
        └── transform_sql.sql


Descrição dos principais arquivos/pastas:

```
- **`Dockerfile`**: Arquivo de configuração da imagem Docker do projeto.
- **`docker-compose.yml`**: Arquivo de orquestração Docker Compose, para subir um ou mais containers.
- **`README.md`**: Documentação principal do projeto.
- **`GeoLite2-ASN.mmdb / GeoLite2-Country.mmdb`**: Bases de dados geolocalização (ou ASN) usadas pelo crawler para mapear endereços IP a regiões.
- **`requirements.txt`**: Lista de dependências (bibliotecas Python) do projeto.
- **`pyproject.toml e pyproject.lock`**: Arquivos de configuração do Poetry para gestão de bibliotecas, com as dependências e versões exatas.
- **`config.docker.yml / config.yml`**: Arquivos de configuração do crawler. O arquivo config.docker.yml
- **`dns_crowler_database.db`**: Banco de dados local do crawler (DuckDB), com dados tratados.
- **`all-domains.txt`**: Lista de domínios (ou hosts) que o crawler deve processar.
- **`data/`**: Pasta onde ficam os resultados (JSON) produzidos pelo crawler.
- **`schema/`**: Scripts SQL para transformação dos dados (transform_sql.sql).



## Dependências

###  Pré-requisitos

- Python 3.11^
- Bibliotecas listados no arquivo `requirements.txt`
- Docker

Este projeto utiliza as seguintes bibliotecas Python:

- **`Python 3.11`**: Linguagem de programação principal.
- **`duckdb 1.1.1`**: Banco de dados colunar em memória, ideal para grandes análises de dados.
- **`pandas 2.2.3`**: Biblioteca Python para manipulação de dados em DataFrames.


## Utilização

1. Criar o imagem Docker

    Criar imagem
    > docker compose build 
    
    Subir container com redis
    > docker compose up -d

2. Subir container com app

    subir container principal
    > docker run -it -v full_path_local:/dns-crawler/dados app_image_id /bin/bash

3. Singlethreaded crawling para 1 dominio

    Criar txt com 1 domínio    
    > echo -e "chrome.pt" > domain-list.txt
        
    crawling 1 dominio
    > dns-crawler domain-list.txt > results.json
    
4.     1. Multithreaded crawling 

    Inicializar redis
    > redis-server --daemonize yes
        
    domain-list.txt == lista com todos os dominios desejados
        
    Colocar dominios na fila
    > dns-crawler-controller domain-list.txt > result.json
        
    Definir número de workers e inicializar
    > dns-crawler-workers 20



