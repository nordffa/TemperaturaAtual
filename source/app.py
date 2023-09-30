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
        while True:
            continuar = str(input("Deseja pesquisar outra cidade? [S/N]: ")).upper().strip()[0]
            if continuar in ["S", "N"]:
                limpar_tela()
                break
            else:
                limpar_tela()
                print("Opção inválida. Por favor, digite 'S' para Sim ou 'N' para Não.")
                pular_linha()
        if continuar == "N":
            break
    else:
        print("Cidade não encontrada. Tente novamente.")
        pular_linha()
print("Obrigado por utilizar nosso aplicativo.")
pular_linha()
pausar_tela()
