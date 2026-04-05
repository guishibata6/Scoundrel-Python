import random as r

def clear():
    i = 0
    while i <= 50:
        print("\n")
        i += 1

styles = {
    "black":"\033[0;30m",
    "red":"\033[0;31m",
    "green":"\033[0;32m",
    "brown":"\033[0;33m",
    "blue":"\033[0;34m",
    "purple":"\033[0;35m",
    "cyan":"\033[0;36m",
    "light_gray":"\033[0;37m",
    "dark_gray":"\033[1;30m",
    "light_red":"\033[1;31m",
    "light_green":"\033[1;32m",
    "yellow":"\033[1;33m",
    "light_blue":"\033[1;34m",
    "light_purple":"\033[1;35m",
    "light_cyan":"\033[1;36m",
    "light_white":"\033[1;37m",
    "bold":"\033[1m",
    "faint":"\033[2m",
    "italic":"\033[3m",
    "underline":"\033[4m",
    "blink":"\033[5m",
    "negative":"\033[7m",
    "crossed":"\033[9m",
    "reset":"\033[0m"
}

def colorformat(text,style):
    return f"{styles[style]}{text}{styles['reset']}"

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

def cardunit(card):
    if len(card) == 2:
        num = card[0]
        suit = card[1]
    elif len(card) == 3:
        num = card[:2]
        suit = card[2]
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
