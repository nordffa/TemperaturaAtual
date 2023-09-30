from funcoes import *

config_video()

while True:
    cidade = input("Digite o nome da cidade: ").title().strip()
    limpar_tela()
    if dados_clima := temperature(cidade):
        temperatura_atual, sensacao_termica = dados_clima
        print(cidade)
        pular_linha()
        print(f"Temperatura atual: {temperatura_atual:.0f}°C")
        print(f"Sensação térmica: {sensacao_termica:.0f}°C")
        pular_linha()
        break
    else:
        print("Cidade não encontrada. Tente novamente.")
        pular_linha()

pausar_tela()
