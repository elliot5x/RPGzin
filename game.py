import os
import time

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
        break  # Agora o `break` está controlando a saída do loop principal

def opcoes():
    print("1. Porta\n2. Janela\n3. Báu\n4. Vaso")
    acao = int(input())
        
    while True:
        if acao == 1:
            if "chave" in inventario:
                print("Abriu a porta")
                time.sleep(3)
                porta()  # A função `porta()` agora é chamada corretamente
                break
            else:
                print("A porta está trancada.")
                time.sleep(3)
                cls()
                opcoes()  # Chamamos novamente `opcoes()` sem recursão infinita
                break
        elif acao == 2:
            print("O dia está lindo, pena que não dá pra sair por aqui.")
            time.sleep(3)
            cls()
            opcoes()
            break
        elif acao == 3:
            if "chave" not in inventario:
                print("Você abre o báu e encontra uma chave, você a coloca no bolso")
                inventario.append("chave")
                time.sleep(3)
                cls()
                opcoes()
                break
            else:
                print("O báu está vazio")
                time.sleep(3)
                cls()
                opcoes()
                break
        elif acao == 4:
            print("O vaso está bonito, mas não parece ter nada de especial")
            time.sleep(3)
            cls()
            opcoes()
            break
        else:
            print("Ação inválida! Tente novamente.")
            time.sleep(2)
            cls()
            opcoes()  # Chama novamente `opcoes()` caso a ação seja inválida

def porta():
    print("Aaaa, olha só, então você abriu a porta")
    print("Seja livre meu amigo, voe gaivota, voe...")
    input()

# Inicia o jogo
game()