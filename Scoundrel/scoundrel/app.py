import flask
import random as r
import webbrowser as web

spades = {
    "2":"Slime",
    "3":"Slime",
    "4":"Aranha",
    "5":"Aranha",
    "6":"Lobo",
    "7":"Lobo",
    "8":"Goblin",
    "9":"Goblin",
    "10":"Golem",
    "11":"Ogro",
    "12":"Ciclope",
    "13":"Dragão",
    "14":"Leviatã"
}

clubs = {
    "2":"Caveira",
    "3":"Caveira",
    "4":"Fantasma",
    "5":"Fantasma",
    "6":"Zumbi",
    "7":"Zumbi",
    "8":"Esqueleto",
    "9":"Esqueleto",
    "10":"Demônio",
    "11":"Minotauro",
    "12":"Arqui-Demônio",
    "13":"Lich",
    "14":"Capeta"
}

hearts = {
    "2":"Poção Pequena",
    "3":"Poção Pequena",
    "4":"Chocolate",
    "5":"Chocolate",
    "6":"Poção Média",
    "7":"Poção Média",
    "8":"Coxa de Frango",
    "9":"Coxa de Frango",
    "10":"Poção Grande",
    "11":"Bolo",
    "12":"Picanha",
    "13":"Pizza",
    "14":"Pastel e Caldo de Cana"
}

diamonds = {
    "2":"Faca",
    "3":"Faca",
    "4":"Machado",
    "5":"Machado",
    "6":"Lança",
    "7":"Lança",
    "8":"Martelo",
    "9":"Martelo",
    "10":"Katana",
    "11":"Alabarda",
    "12":"Foice",
    "13":"Espada Sagrada",
    "14":"AK-47"
}

vida = 20
usedDeck = []
room = []
i = 0
gameRoom = []
gameRoomColor = []
gameRoomValue = []
weapon = "Mão"
weaponValue = ""
healswitch = False
save = []
run = False
runShow = True
runRoom = []
runcount = 2
deck = []
deckShow = deck + len(runRoom)

def cardunit(card):
    if len(card) == 2:
        num = card[0]
        suit = card[-1]
    elif len(card) == 3:
        num = card[:2]
        suit = card[-1]
    match suit:
        case "s":
            return f"{spades[num]}"
        case "c":
            return f"{clubs[num]}"
        case "h":
            return f"{hearts[num]}"
        case "d":
            return f"{diamonds[num]}"
        
def draw():
    num = r.randint(2,14)
    suit = r.randint(0,3)
    suits = ["s","h","c","d"]
    card = f"{num}{suits[suit]}"
    return card

def clear():
    i = 0
    while i <= 50:
        print("\n")
        i += 1

app = flask.Flask(__name__)

url = "http://127.0.0.1:5000/title"
web.open(url)

@app.route('/title', methods = ["GET","POST"])
def home():
    return flask.render_template("/index.html")

def togame():
    if flask.request.method == "POST":
        return flask.render_template("/game.html")

def toguide():
    if flask.request.method == "POST":
        return flask.render_template("/guide.html")
    
@app.route('/guide', methods = ["GET","POST"])
def guide():
    return flask.render_template("/guide.html")

@app.route('/win')
def win():
    return flask.render_template("/win.html")

@app.route('/gameover')
def gameover():
    return flask.render_template("/gameover.html")

@app.route('/game', methods = ["GET","POST"])
def game():
    global vida, usedDeck, room, i, gameRoom, gameRoomColor, gameRoomValue, weapon, weaponValue, healswitch, save, run, runRoom, runcount, runShow, deck, deckShow
    action = ""
    if flask.request.method != "POST":
        vida = 20
        usedDeck = []
        room = []
        i = 0
        gameRoom = []
        gameRoomColor = []
        gameRoomValue = []
        weapon = "Mão"
        weaponValue = ""
        healswitch = False
        run = False
        runRoom = []
        runcount = 2
        runShow = True
        save = []
        deck = 52
        deckShow = deck + len(runRoom)
    try:
        btnid = int(flask.request.form.get("btn1"))
    except:
        try:
            btnid = int(flask.request.form.get("btn2"))
        except:
            try:
                btnid = int(flask.request.form.get("btn3"))
            except:
                try:
                    btnid = int(flask.request.form.get("btn4"))
                except:
                    try:
                        btnid = int(flask.request.form.get("btn5"))
                    except:
                        try:
                            btnid = int(flask.request.form.get("btn6"))
                        except:
                             pass

    try:
        if btnid == 6:
            runRoom.extend(room)
            run = True
            action = "Você correu para outra sala."
            runcount = 0
            room.clear()
            gameRoom.clear()
            gameRoomColor.clear()
            gameRoomValue.clear()
            save.clear()
            deck -= 5
        else:
            selectedCard = room[btnid-1]
            if len(selectedCard) == 2:
                selectNum = int(selectedCard[0])
            elif len(selectedCard) == 3:
                selectNum = int(selectedCard[:2])
            if "s" in selectedCard or "c" in selectedCard:
                combatDecision = flask.request.form.get("usar")
                if combatDecision == "Mão":
                    vida -= selectNum
                    action = f"Você matou a criatura e perdeu {selectNum} de vida."
                elif combatDecision == "Arma":
                    if weapon == "Mão":
                        vida -= selectNum
                        action = f"Você matou a criatura e perdeu {selectNum} de vida."
                    elif weaponValue < selectNum:
                        vida -= selectNum
                        action = f"Você matou a criatura e perdeu {selectNum} de vida."
                    else:
                        weaponValue = selectNum
                        action = f"Você matou a criatura e sua arma teve {selectNum} de desgaste."
            elif "h" in selectedCard:
                if healswitch == False:
                    if vida == 20:
                        cura = 0
                    else:
                        tempvida = vida
                        cura = selectNum
                        vida += selectNum
                        if vida > 20:
                            vida = 20
                            cura = 20 - tempvida
                    action = f"Você curou {cura} de vida."
                elif healswitch == True:
                    action = f"Nada aconteceu."
                healswitch = True
            elif "d" in selectedCard:
                weapon = cardunit(selectedCard)
                weaponValue = selectNum
                action = f"Você equipou {weapon}."
            gameRoomColor[btnid-1] = "a"
            room[btnid-1] = "a"
            gameRoom[btnid-1] = "a"
            gameRoomValue[btnid-1] = "a"
            save.remove(selectedCard)
    except:
        pass

    if vida <= 0:
        return flask.redirect("/gameover")
    w = 0
    for x in room:
        if len(x) == 2:
            suit = x[1]
        elif len(x) == 3:
            suit = x[2]
        else:
            suit = ""
        if suit == "s" or suit == "c":
            w += 1
            break
    if w == 0:
        if deck == 0:
            w = 0
            for x in usedDeck:
                if len(x) == 2:
                    suit = x[1]
                elif len(x) == 3:
                    suit = x[2]
                if "s" in suit or "c" in suit:
                    w += 1
            win = True
            for x in runRoom:
                if len(x) == 2:
                    suit = x[1]
                elif len(x) == 3:
                    suit = x[2]
                if "s" in suit or "c" in suit:
                    win = False
                    break
            if w == 26 and win == True:
                return flask.redirect("/win")


    if run == False:
        if len(save) == 1:
            saveCard = save[0]
            room.clear()
            room.append(saveCard)
            gameRoom.clear()
            gameRoom.append(cardunit(saveCard))
            gameRoomColor.clear()
            gameRoomValue.clear()
            save.clear()
            healswitch = False
            
            if len(saveCard) == 2:
                num = saveCard[0]
                suit = saveCard[1]
            elif len(saveCard) == 3:
                num = saveCard[:2]
                suit = saveCard[2]
            match suit:
                case "s":
                    gameRoomColor.append("b")
                case "h":
                    gameRoomColor.append("r")
                case "c":
                    gameRoomColor.append("c")
                case "d":
                    gameRoomColor.append("y")
            gameRoomValue.append(num)
            i = 1
    else:
        i = 0
    if deck > 0 and len(usedDeck) != 52:
        if len(room) <= 1:
            while i <= 4:
                if deck == 0 and len(runRoom) == 0:
                    gameRoomColor.append("a")
                    room.append("a")
                    gameRoom.append("a")
                    gameRoomValue.append("a")
                    i += 1
                elif deck == 0 and len(runRoom) > 0:
                    card = runRoom[i]
                    runRoom.remove(card)
                    room.append(card)
                    gameRoom.append(cardunit(card))
                    if len(card) == 2:
                        num = card[0]
                        suit = card[1]
                    elif len(card) == 3:
                        num = card[:2]
                        suit = card[2]
                    match suit:
                        case "s":
                            gameRoomColor.append("b")
                        case "h":
                            gameRoomColor.append("r")
                        case "c":
                            gameRoomColor.append("c")
                        case "d":
                            gameRoomColor.append("y")
                    gameRoomValue.append(num)
                    i += 1
                else:
                    card = draw() 
                    if card not in usedDeck:
                        room.append(card)
                        usedDeck.append(card)
                        gameRoom.append(cardunit(card))
                        if len(card) == 2:
                            num = card[0]
                            suit = card[1]
                        elif len(card) == 3:
                            num = card[:2]
                            suit = card[2]
                        match suit:
                            case "s":
                                gameRoomColor.append("b")
                            case "h":
                                gameRoomColor.append("r")
                            case "c":
                                gameRoomColor.append("c")
                            case "d":
                                gameRoomColor.append("y")
                        gameRoomValue.append(num)
                        i += 1
                        deck -= 1
            save.extend(room)
            healswitch = False
    elif deck == 0 and len(runRoom) > 0:
        while i <= 4:
            if deck == 0 and len(runRoom) == 0:
                gameRoomColor.append("a")
                room.append("a")
                gameRoom.append("a")
                gameRoomValue.append("a")
                i += 1
            else:
                card = runRoom[i]
                runRoom.remove(card)
                room.append(card)
                gameRoom.append(cardunit(card))
                if len(card) == 2:
                    num = card[0]
                    suit = card[1]
                elif len(card) == 3:
                    num = card[:2]
                    suit = card[2]
                match suit:
                    case "s":
                        gameRoomColor.append("b")
                    case "h":
                        gameRoomColor.append("r")
                    case "c":
                        gameRoomColor.append("c")
                    case "d":
                        gameRoomColor.append("y")
                gameRoomValue.append(num)
                i += 1    
    if len(save) == 5 and deckShow > 5 and run == False:
        runShow = True
    else:
        runShow = False

    if runcount <= 2:
        runcount += 1
    if runcount == 2:
        run = False

    if deck < 0:
        deck = 0
    deckShow = deck + len(runRoom)
    print(deck)
    print(len(runRoom))
    print(len(usedDeck))
    print(runRoom)
    print(gameRoom)
    return flask.render_template("/game.html",vidaAtual = vida, baralho = deckShow, card1 = gameRoom[0], card2 = gameRoom[1], card3 = gameRoom[2], card4 = gameRoom[3], card5 = gameRoom[4], 
                                color1 = gameRoomColor[0], color2 = gameRoomColor[1], color3 = gameRoomColor[2], color4 = gameRoomColor[3], color5 = gameRoomColor[4], value1 = gameRoomValue[0],
                                value2 = gameRoomValue[1], value3 = gameRoomValue[2], value4 = gameRoomValue[3], value5 = gameRoomValue[4], acao = action, arma = weapon, desgaste = weaponValue,
                                corre = runShow)   



if __name__ == "__main__":
    app.run(debug=True)