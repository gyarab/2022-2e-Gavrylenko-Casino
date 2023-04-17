#zdroje:
#https://www.geeksforgeeks.org/how-to-create-a-text-input-box-with-pygame/
#https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/
#https://www.freecodecamp.org/news/create-a-dictionary-in-python-python-dict-methods/
#
#

import pygame
import Database
from Classes import GameCard, Button, TextField, colors

global stage
global money
global name 
global roulete_wins
global coin_wins
global slot_wins

pygame.init()
pygame.font.init()
WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

# stage home, login, singin, roulete, slot, coinflip, account, about, deposite, test
stage = "login"
money = 0
name = "abobus"
roulete_wins = 0
coin_wins = 0
slot_wins = 0


def update_btns(btns):
    for btn in btns:
        btn.stage = stage


def set_stage_roulette():
    global stage
    stage = "Roulette"
    update_btns(nav_bar_btns)
def set_stage_home():
    global stage
    stage = "Home"
    update_btns(nav_bar_btns)
def set_stage_slot():
    global stage
    stage = "Slot"
    update_btns(nav_bar_btns)
def set_stage_coinflip():
    global stage
    stage = "Coinflip"
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
def login_function():
    if Database.authorize(log_user_name_txt.user_text,log_user_password_txt.user_text):
        global stage
        load_data()
        stage ="Home"
        update_btns(nav_bar_btns)
def sign_function():
    global stage
    if Database.add_user(signin_user_name_txt.user_text, signin_user_password_txt.user_text,signin_user_sec_password_txt.user_text):
        
        print("dobavil")
        stage ="login"
    else:
        print("false")
def load_data():
    global money, name, roulete_wins, coin_wins, slot_wins

    data = Database.load_data(log_user_name_txt.user_text)
    name = data[0]
    money = data[1]
    roulete_wins = data[2]
    coin_wins = data[3]
    slot_wins = data[4]
    
    nav_bar_account_btn = Button(1000, 0, 280, 60,f"{name}"+" "+f"{money}"+"$", set_stage_account, False, screen, stage, "Account")
    nav_bar_btns.append(nav_bar_account_btn)
    

#login variables
login_page_btns = []
log_signin_btn = Button(WIDTH/2 - 75, 550, 150, 60, 'Sign In', set_signin_page, False, screen, stage)
log_login_btn = Button(WIDTH/2 - 125, 450, 250, 60, 'Login', login_function, False, screen, stage)
login_page_btns.append(log_signin_btn)
login_page_btns.append(log_login_btn)

login_page_txt = []
log_user_name_txt = TextField(WIDTH/2-150, 150, 150, 60, 'username',False,None, screen)
log_user_password_txt = TextField(WIDTH/2 -150, 250, 150, 60, 'password',True,login_function, screen)
login_page_txt.append(log_user_name_txt)
login_page_txt.append(log_user_password_txt)

#signin variables
signin_page_btns = []
signin_btn = Button(WIDTH/2 - 125, 500, 250, 60, 'Sign In', sign_function, False, screen, stage)
signin_page_btns.append(signin_btn)

signin_page_txt = []
signin_user_name_txt = TextField(WIDTH/2 - 75, 150, 150, 60, 'username',False,None, screen)
signin_user_password_txt = TextField(WIDTH/2 - 75, 250, 150, 60, 'password',True,None, screen)
signin_user_sec_password_txt = TextField(WIDTH/2 - 75, 350, 150, 60, 'second password',True,sign_function, screen)
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

def nav_bar():
    for btn in nav_bar_btns:
        btn.process()

def loginPage():
    #TODO username text field, password text field, button login, button singin
    for btn in login_page_btns:
        btn.process()
    for txt in login_page_txt:
        txt.draw()

def homePage():
    #TODO username text field, password text field, button login, button singin
    
    nav_bar()
    for card in home_cards:
        card.draw()
    
def signinPage():
    #TODO username text field, password text field,second password text field,button singin
    for btn in signin_page_btns:
        btn.process()
    for txt in signin_page_txt:
        txt.draw()

def roulettePage():
    #TODO username text field, password text field, button login, button singin
    
    nav_bar()

def slotPage():
    #TODO username text field, password text field, button login, button singin
    nav_bar()

def coinflipPage():
    #TODO username text field, password text field, button login, button singin
    nav_bar()

def accountPage():
    #TODO username text field, password text field, button login, button singin
    nav_bar()

def aboutPage():
    #TODO username text field, password text field, button login, button singin
    nav_bar()

def depositePage():
    #TODO username text field, password text field, button login, button singin
    print("loginpage")

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

def text_field_events(event):
    global stage
    if (stage =="login"):
        page_txt = login_page_txt
    elif(stage == "signin"):
        page_txt = signin_page_txt
    else:
        page_txt = []

    for text in page_txt:
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if text.textRect.collidepoint(event.pos):
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
            # Check for backspace
            if event.key == pygame.K_BACKSPACE:
                text.user_text = text.user_text[:-1]
            elif(len(text.user_text)<text.max_length):
                text.user_text += event.unicode
        if text.active:
            text.color = text.color_active
        else:
            text.color = text.color_passive

stage = "login"

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        text_field_events(event)
    # fill the screen with a color to wipe away anything from last frame
    screen.fill(colors["background"])
    page(stage)
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()