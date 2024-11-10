import os
import time
import sys

def cls():
    if os.name == 'nt':
        os.system('cls')

# Inventário do jogador
inventario = []

def game():
    while True:
        print("Você está num quarto de quatro lados")
        time.sleep(2)
        cls()
        print("Na sua frente uma porta\natrás uma janela\nna esquerda um báu\nna direita um vaso\n")
        time.sleep(4)
        cls()
        opcoes()
        break  

def opcoes():
    print("1. Porta\n2. Janela\n3. Báu\n4. Vaso")
    acao = obter_entrada()
        
    while True:
        if acao == 1:
            if "chave" in inventario:
                print("Abriu a porta")
                time.sleep(3)
                porta()  
                break
            else:
                print("A porta está trancada.")
                time.sleep(3)
                cls()
                opcoes()  
                break
        elif acao == 2:
            print("O dia está lindo, pena que não dá pra sair por aqui.")
            time.sleep(3)
            cls()
            opcoes()
            break
        elif acao == 3:
                print("O baú está vazio.")
                time.sleep(3)
                cls()
                opcoes()
                break
        elif acao == 4:
            print("O vaso está bonito, ah não ser pela rachadura na sua lateral.")
            time.sleep(2)
            print("Verificar Rachadura??\n1. Sim\n2 .Não?\n")
            rachadura = obter_entrada()
            if rachadura == 1:
                if "chave" not in inventario:
                    print("Você encontra a chave, você a coloca no bolso")
                    inventario.append("chave")
                    time.sleep(3)
                    cls()
                    opcoes()
                else:
                    print("Você já tem a chave no bolso.")
                    time.sleep(3)
                    cls()
                    opcoes()
            elif rachadura == 2:
                cls()
                opcoes()
            else:
                print("Escolha um número válido.")
                time.sleep(2)
                cls()
                opcoes()
        else:
            print("Ação inválida! Tente novamente.")
            time.sleep(2)
            cls()
            opcoes()

def obter_entrada():
    while True:
        try:
            acao = int(input("Escolha uma ação: "))
            if acao in [1, 2, 3, 4]:
                return acao
            else:
                print("Opção inválida. Tente Novamente.")
        except ValueError:
            print("Por favor, digite um número válido.")

def porta():
    cls()
    print("Aaaa, olha só, então você abriu a porta")
    print("Seja livre meu amigo, voe gaivota, voe...")
    print("\nJogar Novamente?\n1. Sim\n2. Não")
    novamente = obter_entrada()
    
    if novamente == 1:
        inventario.clear()
        game()
    elif novamente == 2:
        sys.exit()
    else:
        porta()
    

# Inicia o jogo
game()