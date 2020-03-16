# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Resource, Api, reqparse
from Moeda import Converter    

#pip install flask_restful

class ChamaMoeda(Resource):
    def post(self):
        try:
            argumentos = reqparse.RequestParser()
            argumentos.add_argument('moedaOrigem')
            argumentos.add_argument('moedaDestino')
            argumentos.add_argument('dataConversao')
            argumentos.add_argument('qtd')
            dados = argumentos.parse_args()
            moedaOrigem = dados['moedaOrigem']
            moedaDestino = dados['moedaDestino']
            dataConversao = dados['dataConversao']
            qtd = dados['qtd']

            print(f'CHAMADA: Origem {moedaOrigem} Destino {moedaDestino} Qtd {qtd} Data {dataConversao}')
            a = (Converter(moedaOrigem, moedaDestino, dataConversao, qtd))
            print(f'Cotação: {a}')
            return a
        except:
            print("Erro no app.py")

app= Flask(__name__)
api = Api(app)

api.add_resource(ChamaMoeda, '/ChamaMoeda')

if __name__ == '__main__':
    app.run(debug=True)
    