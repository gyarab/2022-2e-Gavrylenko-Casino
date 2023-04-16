import json
from tkinter import *
def showError(text):
    window = Tk()

    window.title("Error")

    lbl = Label(window, text=text, font=("Arial Bold", 50))

    lbl.grid(column=0, row=0)

    window.mainloop()

def authorize(name,password):
    #check for valid name
    try:
        with open('users.json') as json_file:
            data = json.load(json_file)
    except:
        showError("You need to sign up")
        return False
    is_in_base = False
    is_in_base_name = False
    for user in data:
        
        if(user['name'] == name and user['password'] == password):
            is_in_base = True 
        if(user['name'] == name):
            is_in_base_name = True           
    if is_in_base:
        return True
    else:

        showError("Your username or password is wrong")
        return False


def add_user(name,password,sec_password):
    if password != sec_password:
        showError("Passwords do not match")
        return False
    try:
        with open('users.json') as json_file:
            data = json.load(json_file)
    except:
        json_object = json.dumps([], indent=4)
        with open("users.json", "w") as outfile:
            outfile.write(json_object)
        data = []
    
    #name check
    for user in data:
        if(user['name'] == name):
            showError("This name is taken")
            return False
    user ={
    "id": len(data)+1,
    "name": name,
    "password": password,
    "money": 1000,
    "roulete_wins": 0,
    "coin_wins": 0,
    "slot_wins": 0,
    }
    data.append(user)
    json_object = json.dumps(data, indent=4)
    
    # Writing to sample.json
    with open("users.json", "w") as outfile:
        outfile.write(json_object)
    return True

def load_data(name):
    with open('users.json') as json_file:
        data = json.load(json_file)
    for user in data:
        if(user['name'] == name):
           return [user['name'], user['money'], user["roulete_wins"], user["coin_wins"], user["slot_wins"]]
    return []