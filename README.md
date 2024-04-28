# Desafio Painel e-SUS

## What is this repository about?

I was challenged to showcase my skills based on the problem described on [DESAFIO.md](../main/DESAFIO.md).

It involves using the Flask framework to develop a REST API. The API returns data about patients of a medical facility, as provided by a csv.

## Setup

Clone the repository

```
git clone https://github.com/GuilhermeCAz/desafio_painel_esus.git
```

> Docker sets up the environment according to the Dockerfile, which means you can skip the following steps straight to [#Running via Docker](#running-via-docker).

From the folder, create and activate a virtual environment

```
python -m venv .venv
```

```
.venv\scripts\activate
```

Install the requirements

```
pip install -r requirements.txt
```

Run the Flask application

```
flask run
```

## Running tests

```
python -m unittest -v
```

## Running via Docker

```
docker-compose build
```

```
docker run -dp 8001:8001 desafio_painel_esus-app
```

### Sample API requests (tested)

```
http://localhost:8001/api/v1/atendimentos?condicao_saude=hipertensao
```

```
http://localhost:8001/api/v1/atendimentos?unidade=Unidade%20de%20saude%20Cec%C3%ADlia
```

```
http://localhost:8001/api/v1/atendimentos?data_atendimento=2024-01-01
```

```
http://localhost:8001/api/v1/atendimentos?data_atendimento=2024-01-01&condicao_saude=hipertensao
```
