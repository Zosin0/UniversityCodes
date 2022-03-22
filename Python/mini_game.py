from random import choice


jogador_vitorias = 0
maq_vitorias = 0


def Opcao_Jogador():
    esc_jogador = input("Escolha Pedra, Papel, ou Tesoura: ")
    esc_jogador.lower()
    if esc_jogador == "pedra":
        return esc_jogador
    elif esc_jogador == "papel":
        return esc_jogador
    elif esc_jogador == "tesoura":
        return esc_jogador
    else:
        print("Opcao invalida. Tente novamente!")
        Opcao_Jogador()


def Opcao_Maquina():
    esc_maquina = choice(["pedra", "papel", "tesoura"])
    return esc_maquina    


while True:    
    print("-"*30)
    esc_jogador = Opcao_Jogador()
    esc_maquina = Opcao_Maquina()
    print("-"*30)

    if(esc_jogador == "pedra") and (esc_maquina == "tesoura") \
        or (esc_jogador == "papel") and (esc_maquina == "pedra") \
            or (esc_jogador == "tesoura") and (esc_maquina == "papel"):
                #Jogador ganha
                print(f"Jogador escolheu {esc_jogador}, e a Maquina escolheu {esc_maquina}."
                "\nResultado: Você ganhou! Parabens!")
                jogador_vitorias += 1

    elif esc_jogador == esc_maquina:
        #Empate
        print(f"Jogador escolheu {esc_jogador}, e a Maquina escolheu {esc_maquina}."
         "\nResultado: Empate!")

    else:
        
        #Maquina ganha
        print(f"Jogador escolheu {esc_jogador}, e a Maquina escolheu {esc_maquina}."
        "\nResutado: Você perdeu! Tente novamente!")
        maq_vitorias += 1
    
    print("-"*30)
    print(f"Vitórias do Jogador: {jogador_vitorias}")
    print(f"Vitórias da Máquina: {maq_vitorias}")    
    print("-"*30)

    esc_jogador = input("Quer jogar novamente? ")
    if esc_jogador in ["SIM", "Sim", "sim", "s", "S"]:
        pass
    elif esc_jogador in ["NAO", "nao", "Nao","N", "n"]:
        break
    else:
        break    


