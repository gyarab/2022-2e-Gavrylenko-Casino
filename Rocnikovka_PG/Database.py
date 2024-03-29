import json
from tkinter import *
from hashlib import sha256

# Funkce, která při nastání chyby v novém malém okně vypíše chybu.
def showError(text):
    window = Tk()
    window.title("Error")

    lbl = Label(window, text=text, font=("Arial Bold", 30),bg = '#222222', fg="#F3EFE0")
    window.configure(bg='#222222')
    lbl.grid(column=0, row=0)

    window.mainloop()

# Funkce, díky které probíhá autorizace a ověřuje, jestli že hráč je už zaregistrovány nebo-li má špatné přihlašovací údaje.
# Taky umožňuje šifrování hesel.
def authorize(name,password):
    try:
        with open('users.json') as json_file:
            data = json.load(json_file)
    except:
        showError("You need to sign up")
        return False
    is_in_base = False

    for user in data:
        if(user['name'] == name and user['password'] == sha256(password.encode('utf-8')).hexdigest()):
            is_in_base = True 
             
    if is_in_base:
        return True
    else:
        showError("Your username or password is wrong")
        return False

# Funkce, která umožňuje registraci hráče.
# Vypíše chybu, jestli že:
# 1) 1. heslo s 2. nejsou stejná.
# 2) Heslo je menší než 5 znaků nebo větší než 12.
# 3) Jméno nového uživatele je stejné s jménem už dřív zaregistrovaného hráče.
# Jinak přidá nového uživatele do users.json.
def add_user(name,password,sec_password):
    if password != sec_password:
        showError("Passwords do not match")
        return False
    if (len(password) < 5):
        showError("Your password must be between 5 and 12 characters")
        return False
    try:
        with open('users.json') as json_file:
            data = json.load(json_file)
    except:
        json_object = json.dumps([], indent=4)
        with open("users.json", "w") as outfile:
            outfile.write(json_object)
        data = []
    for user in data:
        if(user['name'] == name):
            showError("This name is taken")
            return False
    user ={
    "id": len(data)+1,
    "name": name,
    "password": sha256(password.encode('utf-8')).hexdigest(),
    "money": 1000,
    "roulete_wins": 0,
    "slot_wins": 0,
    "coin_wins": 0
    }
    data.append(user)
    json_object = json.dumps(data, indent=4)
    with open("users.json", "w") as outfile:
        outfile.write(json_object)
    return True

# Tato funkce slouží k načtení dat uživatele z databáze uložené v souboru users.json.
def load_data(name):
    with open('users.json') as json_file:
        data = json.load(json_file)
    for user in data:
        if(user['name'] == name):
           return [user['name'], user['money'], user["roulete_wins"],  user["slot_wins"],user["coin_wins"]]
    return []

# Tato funkce slouží k aktualizaci dat o uživateli v databázi uložené v souboru users.json.
def update(name,money,roulete_wins,slot_wins,coin_wins):    
    with open('users.json') as json_file:
        data = json.load(json_file)
        for user in data:
            if(user['name'] == name):
                user["money"] = money
                user["roulete_wins"] = roulete_wins
                user["coin_wins"] = coin_wins
                user["slot_wins"] = slot_wins
                break

    with open("users.json", "w") as outfile:
        outfile.write(json.dumps(data, indent=4))

