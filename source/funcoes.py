import requests
import os


def config_video():
    os.system("mode con cols=70")
    os.system("mode con lines=10")
    os.system("title Temperatura Atual")


def temperature(city):
    api_key = "0d6913f40fd86a581d159200178960d5"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    dados = response.json()
    return dados["main"]["temp"], dados["main"]["feels_like"]


def pausar_tela():
    os.system("PAUSE")


def limpar_tela():
    os.system("CLS")


def pular_linha():
    print()
