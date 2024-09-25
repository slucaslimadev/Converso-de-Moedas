import requests

def pegar_cotacao_moeda(moeda_origem, moeda_destino):
    link = f"https://economia.awesomeapi.com.br/last/{moeda_origem}-{moeda_destino}"
    requisao = requests.get(link)

    cotacao = requisao.json()[f"{moeda_origem}{moeda_destino}"]["bid"]
    return cotacao

