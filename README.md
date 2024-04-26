## Running the project

```
> pip install -r requirements.txt
> flask run
```

## Running via Docker

```
> docker-compose build
> docker run -dp 8001:8001 desafio_painel_esus-app
```

## Running the tests

```
> pip install -r requirements.txt
> python -m unittest -v
```

### Sample API requests (tested)

- http://localhost:8001/api/v1/atendimentos?condicao_saude=hipertensao
- http://localhost:8001/api/v1/atendimentos?unidade=Unidade%20de%20saude%20Cec%C3%ADlia
- http://localhost:8001/api/v1/atendimentos?data_atendimento=2024-01-01
- http://localhost:8001/api/v1/atendimentos?data_atendimento=2024-01-01&condicao_saude=hipertensao
