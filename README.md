# django-com-postgres-legado
Projeto para estudar como utilizar o Django com banco de dados legado

## Passo número 1: Criar um banco de dados para simular o projeto legado

Para fazer isso, instale o docker e rode o comando:

```bash
docker compose up -d
```

Isso vai instalar o Postgres versão 15.2 com usuário e senha iguas a "postgres" rodando na porta 5432. Confira o arquivo docker-compose se precisar mudar as configurações.

No postgres rode o seguinte código sql para criar um banco chamado "legado" com tabela chamada "cursos" com dois cursos salvos:

```
CREATE DATABASE legado;

CREATE TABLE cursos(
    id bigserial PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP,
    updated_at TIMESTAMP DEFAULT current_timestamp
);

INSERT INTO cursos (name, created_at) VALUES ('Django', '2023-09-20 12:00:00');
INSERT INTO cursos (name, created_at) VALUES ('SQL', '2023-09-20 12:10:00' );
```

## Passo 2 criação de projeto django

Crie e ative um ambiente virtual:

```bash
 python -m venv .venv
 source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

