"""Module containing main structure of the app."""

import pandas as pd
from flask import Flask, jsonify, request, wrappers
from flask.json.provider import DefaultJSONProvider

from desafio_painel_esus.config import ATENDIMENTOS_ENDPOINT, ROOT

app = Flask(__name__)
DefaultJSONProvider.sort_keys = False


def get_dataframe() -> pd.DataFrame:
    """
    Extract data from CSV, parse date columns and standardize names.

    Returns
    -------
        DataFrame containing parsed dates.

    """
    atendimentos = pd.read_csv(
        filepath_or_buffer=ROOT / 'db' / 'atendimentos.csv',
        index_col=[0],
        parse_dates=['Nascimento', 'data_atendimento'],
        date_format='mixed',
    )
    atendimentos['Nascimento'] = atendimentos['Nascimento'].dt.strftime(
        '%Y-%m-%d'
    )
    atendimentos['data_atendimento'] = atendimentos[
        'data_atendimento'
    ].dt.strftime('%Y-%m-%d %H:%M:%S.%f')

    return atendimentos.rename(columns=lambda name: name.lower())


@app.route(ATENDIMENTOS_ENDPOINT, methods=['GET'])
def get_atendimentos() -> wrappers.Response:
    """
    Define an app route for getting data about patients.

    Allows filters on three parameters:
        condicao_saude, unidade and data_atendimento

    Returns
    -------
        JSON-formatted HTTP response.

    """
    atendimentos = get_dataframe()
    for param, value in request.args.items():
        if param in ('condicao_saude', 'unidade', 'data_atendimento'):
            atendimentos = atendimentos[
                atendimentos[param].str.contains(value)
            ]

    return jsonify(atendimentos.to_dict(orient='records'))


def main() -> None:
    """
    Run Flask app through python, instead of using 'flask run' command.

    Used solely for debugging.
    """
    app.run()


if __name__ == '__main__':
    main()
