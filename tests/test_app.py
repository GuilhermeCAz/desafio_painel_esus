import unittest
import urllib.parse
from datetime import datetime

from werkzeug.test import TestResponse

from desafio_painel_esus.app import app
from desafio_painel_esus.config import ATENDIMENTOS_ENDPOINT


class TestAPI(unittest.TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        self.app = app.test_client()

    def assert_response_ok(self, response: TestResponse) -> None:
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertIsNotNone(response.json, 'Resposta vazia.')

    def test_get_atendimentos_sem_params(self) -> None:
        response = self.app.get(ATENDIMENTOS_ENDPOINT)
        self.assert_response_ok(response)

    def test_get_atendimentos_por_condicao_saude(self) -> None:
        params = {'condicao_saude': 'hipertensao'}
        response = self.app.get(
            ATENDIMENTOS_ENDPOINT + '?' + urllib.parse.urlencode(params)
        )
        self.assert_response_ok(response)

        for atendimento in response.json or []:
            self.assertEqual('hipertensao', atendimento['condicao_saude'])

    def test_get_atendimentos_por_unidade(self) -> None:
        params = {'unidade': 'Unidade de saude Cecília'}
        response = self.app.get(
            ATENDIMENTOS_ENDPOINT + '?' + urllib.parse.urlencode(params)
        )
        self.assert_response_ok(response)

        for atendimento in response.json or []:
            self.assertEqual(
                'Unidade de saude Cecília', atendimento['unidade']
            )

    def test_get_atendimentos_por_data_atendimento(self) -> None:
        params = {'data_atendimento': '2024-01-01'}
        response = self.app.get(
            ATENDIMENTOS_ENDPOINT + '?' + urllib.parse.urlencode(params)
        )
        self.assert_response_ok(response)

        for atendimento in response.json or []:
            data_atendimento = datetime.strptime(
                atendimento['data_atendimento'], '%Y-%m-%d %H:%M:%S.%f'
            ).strftime('%Y-%m-%d')
            self.assertEqual('2024-01-01', data_atendimento)

    def test_get_atendimentos_por_condicao_saude_e_data(self) -> None:
        params = {
            'data_atendimento': '2024-01-01',
            'condicao_saude': 'hipertensao',
        }
        response = self.app.get(
            ATENDIMENTOS_ENDPOINT + '?' + urllib.parse.urlencode(params)
        )
        self.assert_response_ok(response)

        for atendimento in response.json or []:
            data_atendimento = datetime.strptime(
                atendimento['data_atendimento'], '%Y-%m-%d %H:%M:%S.%f'
            ).strftime('%Y-%m-%d')
            self.assertEqual('2024-01-01', data_atendimento)
            self.assertEqual('hipertensao', atendimento['condicao_saude'])


if __name__ == '__main__':
    unittest.main()
