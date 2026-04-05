import utilities as ut
hp = 20
weapon = "Nada"
weaponvalue = 0
start = True
game = True
deck = []
rundeck = []
runcolordeck = []
healswitch = False
weaponlist = []
run = False

while start == True:
    ut.clear()
    print("     S C O U N D R E L")
    print("         1. Jogar")
    print("         2. Guia")
    print("         3. Sair")
    choice = int(input())
    match choice:
        case 1:
            game = True
            hp = 20
            weapon = "Nada"
            room = []
            roomcolor = []
            deck.clear()
            rundeck.clear()
            runcolordeck.clear()
            runcount = 2
            while game == True:
                ut.clear()
                if "s" in deck or "c" in deck:
                    counter = 0
                    for x in deck:
                        if "s" in x or "c" in x:
                            counter += 1
                    if "s" in rundeck or "c" in rundeck:
                        for x in rundeck:
                            if "s" in x or "c" in x:
                                counter += 1
                    if counter == 26:
                        print(f"{ut.colorformat('==','black')} {ut.colorformat('++','blue')} Vitória {ut.colorformat('++','red')} {ut.colorformat(''=='','yellow')}")
                        print("Parabéns! Você limpou a masmorra!")
                        input("\nPressione Enter para continuar")
                        game = False
                        break
                healswitch = False
                if len(room) == 0:
                    i = 0
                else:
                    i = 1
                if len(rundeck) != 52 - len(deck):
                    while i <= 4:
                        card = ut.draw()
                        if card in deck or len(deck) == 52:
                            pass
                        else:
                            deck.append(card)
                            room.append(card)
                            if len(card) == 2:
                                suit = card[1]
                            elif len(card) == 3:
                                suit = card[2]
                            match suit:
                                case "s":
                                    roomcolor.append("black")
                                case "h":
                                    roomcolor.append("red")
                                case "c":
                                    roomcolor.append("blue")
                                case "d":
                                    roomcolor.append("yellow")
                            i += 1
                else:
                    while i <= 4:
                        if len(deck) != 52:
                            room.append(rundeck[i])
                            roomcolor.append(runcolordeck[i])
                            rundeck.pop(i)
                            runcolordeck.pop(i)
                        i += 1
                if runcount <= 2:
                    runcount += 1
                if runcount == 2:
                    run = False
                while True: 
                    i = 0
                    mistake = False
                    ut.clear()
                    print(f"Masmorra: {52-len(deck)}\nVida: {hp}/20\nArma: ({weaponvalue}) {weapon}")
                    while i <= len(room)-1:
                        card = room[i]
                        if len(card) == 2:
                            card = int(card[0])
                        elif len(card) == 3:
                            card = int(card[:2])
                        print(f"{i+1}. {ut.colorformat('[',roomcolor[i])}({card}) {ut.cardunit(room[i])}{ut.colorformat(']',roomcolor[i])}")
                        i += 1
                    if run == False and len(room) == 5:
                        print(f"\n{i+1}. Correr") 
                    gchoice = input("\nEscolha uma carta: ")
                    try:
                        gchoice = int(gchoice)
                    except:
                        print("\nEscolha uma carta da sala.")
                        input("\nPressione Enter")
                        mistake = True
                    if mistake == False:
                        if gchoice == i+1 and run == False:
                            print("\nMovendo para a próxima sala.")
                            input("\nPressione Enter")
                            rundeck.extend(room)
                            runcolordeck.extend(roomcolor)
                            room.clear()
                            roomcolor.clear()
                            run = True
                            runcount = 0
                            break
                        else: 
                            try:
                                gamechoice = room[gchoice-1]
                            except:
                                print("\nEscolha uma carta da sala.")
                                input("\nPressione Enter")
                                mistake = True
                            if mistake == False:
                                if len(gamechoice) == 2:
                                    value = int(gamechoice[0])
                                    suit = gamechoice[1]
                                elif len(gamechoice) == 3:
                                    value = int(gamechoice[:2])
                                    suit = gamechoice[2]
                                if suit == "s" or suit == "c":
                                    while True:
                                        if weapon != "Nada":
                                            print("\nNa mão ou com a arma?\n[ 1 ] Na mão\n[ 2 ] Com a arma")
                                            choice = int(input("\n"))
                                            if choice == 1:
                                                print(f"\nVocê perdeu {value} de vida.")
                                                hp -= value
                                                break
                                            elif choice == 2:
                                                if weaponvalue < value:
                                                    print("\nSua arma não vai causar efeito na criatura.")
                                                else:
                                                    print(f"\nSua arma está com {value} de durabilidade.")
                                                    weaponvalue = value
                                                    break
                                        else:
                                            print(f"\nVocê perdeu {value} de vida.")
                                            hp -= value
                                            break
                                elif suit == "h":
                                    if healswitch == False:
                                        oldhp = hp
                                        hp += value
                                        if hp > 20: 
                                            hp = 20
                                        healswitch = True
                                        print(f"\nVocê curou {20 - oldhp} de vida.")
                                elif suit == "d":
                                    weapon = ut.cardunit(gamechoice)
                                    weaponvalue = value
                                    print(f"\nVocê equipou {ut.cardunit(gamechoice)}.")
                                
                                room.pop(gchoice-1)
                                roomcolor.pop(gchoice-1)
                                input("\nPressione Enter")
                                if hp <= 0:
                                    ut.clear()
                                    print(f"{ut.colorformat('XX','black')} {ut.colorformat('XX','blue')} Game Over {ut.colorformat('XX','red')} {ut.colorformat('XX','yellow')}")
                                    input("\nPressione Enter")
                                    game = False
                                    break
                                if len(room) == 1:
                                    break
        case 2:
            ut.clear()
            print("Olá! Bem vindo ao guia de Scoundrel.\nAqui, você irá aprender tudo que precisa saber sobre este jogo.")
            input("\nPressione Enter para continuar")
            ut.clear()
            print("== Objetivo ==")
            print("O seu objetivo principal é entrar em uma masmorra e eliminar todas as criaturas dentro dela, usando armas e poções.")
            print("Masmorras consistem de salas. Cada sala consiste de cinco cartas (sim, Scoundrel é um jogo de cartas).")
            input("\nPressione Enter para continuar")
            ut.clear()
            print("== Naipes ==")
            print("Há quatro naipes, cada um com uma função no jogo e colorizadas para reconhecimento, eles são:")
            print(f"{ut.colorformat('Espadas','black')} e {ut.colorformat('Paus','blue')}: são as criaturas na masmorra. Derrote todas elas e você vencerá o jogo.")
            print(f"{ut.colorformat('Copas','red')}: são poções e te curam.")
            print(f"{ut.colorformat('Ouros','yellow')}: são as armas que você pode usar dentro da masmorra contra as criaturas.")
            input("\nPressione Enter para continuar")
            ut.clear()
            print("== Sala ==")
            print("Ao entrar em uma sala, você será apresentado cinco cartas. Escolha uma delas e uma das ações vai acontecer de acordo com o naipe.")
            print(f"{ut.colorformat('Espadas','black')} e {ut.colorformat('Paus','blue')}: você enfrentará a criatura com a sua arma equipada ou com suas mãos.")
            print(f"{ut.colorformat('Copas','red')}: você cura a sua vida (o máximo e o inicial é 20).")
            print(f"{ut.colorformat('Ouros','yellow')}: você equipa a arma e pode usá-la contra as criaturas da masmorra.")
            print("Além disso, cada carta possui um valor que determina a sua força para cada naipe.")
            print("Você escolhe quatro cartas, fazendo as ações de cada uma, até que reste apenas uma carta. Com isso, quatro novas cartas serão introduzidas e você terá movido para uma nova sala")
            input("\nPressione Enter para continuar")
            ut.clear()
            print("== Combate ==")
            print("Ao enfrentar uma criatura, você pode escolher entre usar a sua arma ou as suas mãos.")
            print("Mãos: você perde vida igual ao valor da criatura e derrota ela.")
            print("Arma: você derrota uma criatura que tenha valor igual ou menor ao valor da arma sem sofrer dano, mas o valor da arma se torna o da criatura derrotada.")
            input("\nPressione Enter para continuar")
            ut.clear()
            print("== Poções ==")
            print("Ao usar uma poção, você cura vida igual ao valor da poção. A cura não pode exceder o seu limite de vida (que é 20)."
                "\nAlém disso, você só pode se curar com uma poção uma vez por sala (você ainda pode escolher uma outra poção na sala, só não vai ser curado).")
            input("\nPressione Enter para continuar")
            ut.clear()
            print("== Correr ==")
            print("Quando você estiver em uma sala que julgue muito difícil (cinco criaturas) ou que possa desperdiçar recursos (muitas poções e armas), você sempre pode correr.")
            print("Correr é uma ação em que você re-embaralha as cartas da sala no baralho da Masmorra e cria uma nova sala, introduzindo cinco cartas novas.")
            print("Saiba que esta ação não pode ser usada duas vezes seguidas.")
            input("\nPressione Enter para continuar")
            ut.clear()
            print("É isso, você já está pronto para limpar uma masmorra. Boa sorte e bom jogo! :D")
            input("\nPressione Enter para continuar")
            ut.clear()


        case 3:
            break

    