# -*- coding: utf-8 -*-
import json
import requests

URL='http://127.0.0.1:5000/ChamaMoeda'

#respostaMoeda = requests.request('GET', URL)

#Parms="?moedaOrigem=USD&moedaDestino=BRL&qtd=45600&dataConversao=03/01/2020"
#respostaMoeda = requests.request('POST', URL+Parms)

####################################
body_Moeda = {
        'moedaOrigem' :"EUR",
        'moedaDestino' :"BRL",
        'dataConversao' :"29/11/2019",
        'qtd' : "12346789"
        }

headers_Moeda ={
        'Content-Type': 'application/json'
        }

respostaMoeda = requests.request('POST', URL, json=body_Moeda, headers=headers_Moeda)

#print("RETORNO JSON:" + respostaMoeda.json())