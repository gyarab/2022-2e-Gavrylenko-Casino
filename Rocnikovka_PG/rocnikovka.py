#zdroje:
#https://www.geeksforgeeks.org/how-to-create-a-text-input-box-with-pygame/
#https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/
#https://www.freecodecamp.org/news/create-a-dictionary-in-python-python-dict-methods/
#https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle
#https://www.youtube.com/watch?v=WIIf3WaO5x4
#https://stackoverflow.com
#https://www.w3schools.com

import pygame, math
import Database
import descriptions
from Classes import GameCard, Button, TextField, colors, Roulette, clock, money, CoinGame, SlotGame

global stage
global name
global roulete_wins
global slot_wins
global coin_wins
global roulette

pygame.init()
pygame.font.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True

stage = "login"
name = "Masha"
roulete_wins = 0
slot_wins = 0
coin_wins = 0

# Funkce , která aktualizuje tlačítka zobrazená na obrazovce na základě aktuální fáze.
def update_btns(btns):
    for btn in btns:
        btn.stage = stage

# Každá funkce (do def login_function()) nastavuje globální proměnnou "stage" na určitou hodnotu, která slouží k určení, která část aplikace nebo hry je právě aktivní.
def set_stage_roulette():
    global stage, roulette
    stage = "Roulette"
    update_btns(nav_bar_btns)
    roulette = Roulette(screen,log_user_name_txt.user_text)

def set_stage_home():
    global stage
    stage = "Home"
    update_btns(nav_bar_btns)

def set_stage_slot():
    global stage, slot
    stage = "Slot"
    slot = SlotGame(screen,log_user_name_txt.user_text)
    update_btns(nav_bar_btns)

def set_stage_coinflip():
    global stage, coin_flip
    stage = "Coinflip"
    coin_flip = CoinGame(screen,log_user_name_txt.user_text)
    update_btns(nav_bar_btns)

def set_stage_account():
    global stage
    stage = "Account"
    update_btns(nav_bar_btns)

def set_stage_about():
    global stage
    stage = "About"
    update_btns(nav_bar_btns)

def set_stage_deposite():
    global stage
    stage = "Deposite"

def set_signin_page():
    global stage
    stage = "signin"
      
def set_stage_login():
    global stage
    stage = "login"
    log_user_name_txt.user_text = log_user_name_txt.textholder
    log_user_password_txt.user_text = log_user_password_txt.textholder

# Funkce login_function() kontroluje, zda se přihlašovací údaje uživatele zadané v přihlašovacím formuláři shodují s hodnotami uloženými v databázi, a to voláním metody authorize() třídy s názvem Database.
def login_function():
    if Database.authorize(log_user_name_txt.user_text,log_user_password_txt.user_text):
        global stage
        load_data()
        stage ="Home"
        update_btns(nav_bar_btns)

# Funkce sign_function() přidá nového uživatele do databáze voláním metody add_user() třídy Database.
def sign_function():
    global stage
    if Database.add_user(signin_user_name_txt.user_text, signin_user_password_txt.user_text,signin_user_sec_password_txt.user_text):
        
        stage ="login"
    else:
        print("false")

# Používá k zobrazení informací o hře.
def show_info():
    global stage
    if (stage == "Roulette" or stage == "Slot" or stage == "Coinflip"):
        descriptions.show(stage)
        clock.tick(300)

# Tato funkce slouží k načtení dat uživatele z databáze uložené v souboru users.json.
# Vytváří a aktualizuje také tlačítka navigačního panelu (nav_bar_btns) na základě údajů uživatele a aktuální fáze. Funkce vytvoří šest tlačítek navigačního panelu: 
# Domů, Ruleta, Slots, Flip Coin, About, Účet a přidá je do nav_bar_btns. 
# Vytvoří také informační tlačítko, které po kliknutí zobrazí popis hry.
def load_data():
    global money, name, roulete_wins, slot_wins, coin_wins, nav_bar_btns

    data = Database.load_data(log_user_name_txt.user_text)
    name = data[0]
    money = data[1]
    roulete_wins = data[2]
    slot_wins = data[3]
    coin_wins = data[4]
    nav_bar_btns = []
    nav_bar_home_btn = Button(0, 0, 180, 60, "Home", set_stage_home, False, screen, stage)
    nav_bar_roulette_btn = Button(180, 0, 180, 60, "Roulette", set_stage_roulette, False, screen, stage)
    nav_bar_slot_btn = Button(360, 0, 180, 60, "Slots", set_stage_slot, False, screen, stage, "Slot")
    nav_bar_coin_btn = Button(540, 0, 180, 60, "Coin Flip", set_stage_coinflip, False, screen, stage, "Coinflip")
    nav_bar_about_btn = Button(720, 0, 180, 60, "About", set_stage_about, False, screen, stage)

    nav_bar_info_btn = Button(1200, 640, 80, 80, "?", show_info, False, screen, stage)

    nav_bar_btns.append(nav_bar_home_btn)
    nav_bar_btns.append(nav_bar_roulette_btn)
    nav_bar_btns.append(nav_bar_slot_btn)
    nav_bar_btns.append(nav_bar_coin_btn)
    nav_bar_btns.append(nav_bar_about_btn)
    nav_bar_btns.append(nav_bar_info_btn)

    nav_bar_account_btn = Button(1000, 0, 280, 60,f"{name}"+" "+f"{money}"+"$", set_stage_account, False, screen, stage, "Account")
    nav_bar_btns.append(nav_bar_account_btn)

# Tato funkce slouží ke zvýšení množství peněz v herním účtu.
def add_money():
    global money
    try:
        money += int(dep_money_txt.user_text)
        dep_money_txt.user_text = ""
        set_stage_home()
    except:
        None
    
    Database.update(log_user_name_txt.user_text,money,roulete_wins,slot_wins,coin_wins)

#Tato funkce se zřejmě stará o výběr peněz z účtu uživatele.
def wisdraw():
    global money
    if(dep_money_out_txt.user_text != dep_money_out_txt.textholder and money- int(dep_money_out_txt.user_text)>=0):
            money -= int(dep_money_out_txt.user_text)

    dep_money_out_txt.user_text = dep_money_out_txt.textholder
    set_stage_home()       
    Database.update(log_user_name_txt.user_text,money,roulete_wins,slot_wins,coin_wins)
 

#login variables
login_page_btns = []
log_signin_btn = Button(WIDTH/2 - 75, 550, 150, 60, 'Sign In', set_signin_page, False, screen, stage)
log_login_btn = Button(WIDTH/2 - 125, 450, 250, 60, 'Login', login_function, False, screen, stage)
login_page_btns.append(log_signin_btn)
login_page_btns.append(log_login_btn)

login_page_txt = []
log_user_name_txt = TextField(WIDTH/2 - 150, 150, 300, 60, 'username',False,None, screen)
log_user_password_txt = TextField(WIDTH/2 - 150, 250, 300, 60, 'password',True,login_function, screen)
login_page_txt.append(log_user_name_txt)
login_page_txt.append(log_user_password_txt)

#signin variables
signin_page_btns = []
signin_btn = Button(WIDTH/2 - 125, 500, 250, 60, 'Sign In', sign_function, False, screen, stage)
signin_page_btns.append(signin_btn)

signin_page_txt = []
signin_user_name_txt = TextField(WIDTH/2 - 150, 150, 300, 60, 'username',False,None, screen)
signin_user_password_txt = TextField(WIDTH/2 - 150, 250, 300, 60, 'password',True,None, screen)
signin_user_sec_password_txt = TextField(WIDTH/2 - 150, 350, 300, 60, 'second password',True,sign_function, screen)
signin_page_txt.append(signin_user_name_txt)
signin_page_txt.append(signin_user_password_txt)
signin_page_txt.append(signin_user_sec_password_txt)

#navigation_bar variables
nav_bar_btns = []
nav_bar_home_btn = Button(0, 0, 180, 60, "Home", set_stage_home, False, screen, stage)
nav_bar_roulette_btn = Button(180, 0, 180, 60, "Roulette", set_stage_roulette, False, screen, stage)
nav_bar_slot_btn = Button(360, 0, 180, 60, "Slots", set_stage_slot, False, screen, stage, "Slot")
nav_bar_coin_btn = Button(540, 0, 180, 60, "Coin Flip", set_stage_coinflip, False, screen, stage, "Coinflip")
nav_bar_about_btn = Button(720, 0, 180, 60, "About", set_stage_about, False, screen, stage)
nav_bar_btns.append(nav_bar_home_btn)
nav_bar_btns.append(nav_bar_roulette_btn)
nav_bar_btns.append(nav_bar_slot_btn)
nav_bar_btns.append(nav_bar_coin_btn)
nav_bar_btns.append(nav_bar_about_btn)

#home_page variables
home_cards = []
home_roulette_card = GameCard(150,100,400,200,"Roulette",set_stage_roulette,None,screen)
home_slot_card = GameCard(750,100,400,200,"Slots",set_stage_slot,None, screen)
home_flipcoin_card = GameCard(150,425,400,200,"Coin Flip",set_stage_coinflip,None, screen)
home_cards.append(home_roulette_card)
home_cards.append(home_slot_card)
home_cards.append(home_flipcoin_card)

#account page
acc_deposite_btn = Button(520, 500, 220, 60, "Deposite", set_stage_deposite, False, screen, stage)
acc_log_out_btn = Button(540, 600, 180, 60, "Log out", set_stage_login, False, screen, stage)
acc_btns = []
acc_btns.append(acc_log_out_btn)
acc_btns.append(acc_deposite_btn)

#deposite page
dep_back_btn = Button(0, 0, 180, 60, "Back", set_stage_account, False, screen, stage)

dep_deposite_txt = TextField(280, 200, 150, 60, "Deposite",False, True, screen, True)
dep_money_txt = TextField(280, 340, 150, 60, 'Value..',False, add_money, screen,False,"9")
dep_money_btn = Button(265, 440, 180, 60, "Confirm", add_money, False, screen, stage)

dep_withdrow_txt = TextField(850, 200, 150, 60, "Withdrow",False, True, screen, True)
dep_money_out_txt = TextField(850, 340, 150, 60, 'Value..',False, wisdraw, screen,False,"9")
dep_money_out_btn = Button(835, 440, 180, 60, "Confirm", wisdraw, False, screen, stage)

dep_txts = []
dep_txts.append(dep_money_txt)
dep_txts.append(dep_money_out_txt)
dep_txts.append(dep_deposite_txt)
dep_txts.append(dep_withdrow_txt)

dep_btns = []
dep_btns.append(dep_money_btn)
dep_btns.append(dep_money_out_btn)
dep_btns.append(dep_back_btn)

# Tato funkce se stará o navigační lištu v herním rozhraní. 
# Nejprve načte data hráče pomocí funkce load_data(). Poté prochází seznam tlačítek v liště a volá metodu process() na každém z nich.
def nav_bar():
    load_data()
    for btn in nav_bar_btns:
        if btn.buttonText == "?":
            if (stage == "Roulette" or stage == "Slot" or stage == "Coinflip"):
                btn.process()
            else:
                continue
        btn.process()

# Tyto funkce (do def page()) definují jednotlivé stránky aplikace kasinové hry. 
def loginPage():
    for btn in login_page_btns:
        btn.process()
    for txt in login_page_txt:
        txt.draw()

def homePage():
    nav_bar()
    for card in home_cards:
        card.draw()
    
def signinPage():
    for btn in signin_page_btns:
        btn.process()
    for txt in signin_page_txt:
        txt.draw()

def roulettePage():                 
    global roulette
    nav_bar()
    load_data()
    roulette.draw()

def slotPage():
    nav_bar()
    load_data()
    slot.draw()

def coinflipPage():
    nav_bar()
    coin_flip.draw()

def accountPage():
    nav_bar()
    for btn in acc_btns:
        btn.process()
    base_font = pygame.font.Font(None, 32)
    text_surface = base_font.render(str(money)+" $", True, "0xF3EFE0")
    screen.blit(text_surface, (30,200))

    text_surface = base_font.render(str(roulete_wins)+" Roulette wins", True, "0xF3EFE0")
    screen.blit(text_surface, (30,250))

    text_surface = base_font.render(str(slot_wins)+" Slot wins", True, "0xF3EFE0")
    screen.blit(text_surface, (30,300))
    
    text_surface = base_font.render(str(coin_wins)+" Coin flip wins", True, "0xF3EFE0")
    screen.blit(text_surface, (30,350))

def aboutPage():
    nav_bar()
    base_font = pygame.font.Font(None, 60)
    text_surface = base_font.render("About Casino", True, "0xF3EFE0" )
    screen.blit(text_surface, (WIDTH/2 - text_surface.get_width()/2, 100))

    base_font = pygame.font.Font(None, 40)
    text_surface = base_font.render("Welcome to my game made for the term paper at the prestigious Arabská Gymnasium.", True, "0xF3EFE0" )
    screen.blit(text_surface, (WIDTH/2 - text_surface.get_width()/2, 200))

    text_surface = base_font.render("The casino was made with all love and care, so that you were comfortable in it to play.", True, "0xF3EFE0" )
    screen.blit(text_surface, (WIDTH/2 - text_surface.get_width()/2, 250))

    text_surface = base_font.render("This is where you can enjoy three great games and win a lot of money!!!", True, "0xF3EFE0" )
    screen.blit(text_surface, (WIDTH/2 - text_surface.get_width()/2, 300))

    text_surface = base_font.render("Support", True, "0xF3EFE0" )
    screen.blit(text_surface, (WIDTH/2 - text_surface.get_width()/2, 570))

    base_font = pygame.font.Font(None, 30)
    text_surface = base_font.render("E-mail: mariia.gavrylenko@student.gyarab.cz", True, "0xF3EFE0" )
    screen.blit(text_surface, (WIDTH/2 - text_surface.get_width()/2, 620))
    
    text_surface = base_font.render("Monday - Friday 8AM - 20PM", True, "0xF3EFE0" )
    screen.blit(text_surface, (WIDTH/2 - text_surface.get_width()/2, 650))
    
    text_surface = base_font.render("Saturday - Sunday 11AM - 17PM", True, "0xF3EFE0" )
    screen.blit(text_surface, (WIDTH/2 - text_surface.get_width()/2, 680))

def depositePage():
    for btn in dep_btns:
        btn.process()
    for txt in dep_txts:
        txt.draw()

# Funkce slouží k rozhodnutí, jakou stránku zobrazit v závislosti na aktuálním stavu hry.
def page(current_state):
    match current_state:
        case "login":
            loginPage()
        case "Home":
            homePage()
        case "signin":
            signinPage()
        case "Roulette":
            roulettePage()
        case "Slot":
            slotPage()
        case "Coinflip":
            coinflipPage()
        case "Account":
            accountPage()
        case "About":
            aboutPage()
        case "Deposite":
            depositePage()

# Zpracovává události související s textovými poli.
def text_field_events(event):
    global stage, roulette, coin_flip, slot
    if (stage =="login"):
        page_txt = login_page_txt
    elif(stage == "signin"):
        page_txt = signin_page_txt
    elif(stage == "Roulette"):
        page_txt = roulette.bet_txt
        roulette.bet_txt[0].draw()
    elif(stage == "Deposite"):
        page_txt = dep_txts
    elif(stage == "Coinflip"):
        page_txt = [coin_flip.text_number_bet]
    elif(stage == "Slot"):
        page_txt = [slot.text_number_bet]
    else:
        page_txt = [] 

    for text in page_txt:
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if text.textRect.collidepoint(event.pos) and text.static == False :
                text.active = True
                text.isSelected = True
                if(text.user_text ==text.textholder):
                    text.user_text = ''
            else:
                if(text.user_text == ''):
                    text.user_text = text.textholder
                text.isSelected = False
                text.active = False

        if event.type == pygame.KEYDOWN and text.isSelected:
            
            if event.key == pygame.K_RETURN:
                
                if(stage == "login"):
                    login_function()
            
            if text.alt_color == "9" or text.alt_color == "36":

                if event.key == pygame.K_BACKSPACE:
                    text.user_text = text.user_text[:-1]

                if(len(text.user_text)<text.max_length):

                    if (event.unicode.isnumeric()):
                        if(int(text.user_text+event.unicode)!=0):
                            text.user_text += event.unicode
                    else:
                        None
                    continue
            
            # Kontrola backspace
            if event.key == pygame.K_BACKSPACE:
                text.user_text = text.user_text[:-1]
            elif(len(text.user_text)<text.max_length):
                text.user_text += event.unicode

        if text.active:
            text.color = text.color_active
        else:
            text.color = text.color_passive

# Funkce slouži k automatickému přihlášování.
def pre_login():
    global name, roulete_wins, money, slot_wins, coin_wins, stage
    data = Database.load_data("")
    name = data[0]
    money = data[1]
    roulete_wins = data[2]
    slot_wins = data[3]
    coin_wins = data[4]
    nav_bar_account_btn = Button(1000, 0, 280, 60,f"{name}"+" "+f"{money}"+"$", set_stage_account, False, screen, stage, "Account")
    nav_bar_btns.append(nav_bar_account_btn)
    stage = "Home"
    log_user_name_txt.user_text = ""
    update_btns(nav_bar_btns)
#pre_login()

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        text_field_events(event)

    screen.fill(colors["background"])
    page(stage)
    pygame.display.flip()
   
    clock.tick(15)

pygame.quit()
