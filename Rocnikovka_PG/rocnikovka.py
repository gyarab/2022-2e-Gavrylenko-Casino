#zdroje:
#https://www.geeksforgeeks.org/how-to-create-a-text-input-box-with-pygame/
#
#
#
#
import pygame
import Database
global stage
pygame.init()
pygame.font.init()
WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
font = pygame.font.SysFont('comicsans', 30,'0xF9D949', True)

# stage home, login, singin, roulete, slot, coinflip, account, about, deposite, test
stage = "login"

class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        

        self.fillColors = {
            'normal' : '0x1B262C',
            'hover' : '0x00B7C2',
            'pressed' : '0x00B7C2',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True,"0xFDCB9E")
        
    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
      
        self.buttonSurface.blit(self.buttonSurf, [
        self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
        self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
    ])
        screen.blit(self.buttonSurface, self.buttonRect)

class TextField():
    def __init__(self, x, y, width, height, textholder="default",isPassword=False,function =None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.base_font = pygame.font.Font(None, 32)
        self.user_text = textholder
        self.textholder = textholder
        self.isPassword = isPassword
        self.function = function
        self.max_length = 12
        self.color_active = pygame.Color('lightskyblue3')
        self.color_passive = pygame.Color('chartreuse4')
        self.fillColors = {
            'normal' : '0x1B262C',
            'hover' : '0x0F4C75',
            'pressed' : '0x00B7C2',
        }

        self.textRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.active = False
        self.isSelected = False
        
        
    def draw(self):
        if self.isPassword and self.user_text!=self.textholder:
            string = ""
            for a in self.user_text:
                string+="*"
            text_surface = self.base_font.render(string, True, (255, 255, 255))
        else:
            text_surface = self.base_font.render(self.user_text, True, (255, 255, 255))
        pygame.draw.rect(screen, "0x00B7C2" , self.textRect)
        screen.blit(text_surface, (self.textRect.x+5, self.textRect.y+5)) 
        self.textRect.w = max(100, text_surface.get_width()+10)    

def set_signin_page():
    global stage
    stage = "signin"

def login_function():
    if Database.authorize(log_user_name_txt.user_text,log_user_password_txt.user_text):
        global stage
        stage ="home"

def sign_function():
    Database.add_user(signin_user_name_txt.user_text, signin_user_password_txt.user_text)
        

#login variables
login_page_btns = []
log_signin_btn = Button(WIDTH/2 - 75, 550, 150, 60, 'Sign In', set_signin_page)
log_login_btn = Button(WIDTH/2 - 125, 450, 250, 60, 'Login', login_function)
login_page_btns.append(log_signin_btn)
login_page_btns.append(log_login_btn)

login_page_txt = []
log_user_name_txt = TextField(WIDTH/2 - 75, 150, 150, 60, 'username',False,None)
log_user_password_txt = TextField(WIDTH/2 - 75, 250, 150, 60, 'password',True,login_function)
login_page_txt.append(log_user_name_txt)
login_page_txt.append(log_user_password_txt)

#signin variables
signin_page_btns = []
signin_btn = Button(WIDTH/2 - 125, 450, 250, 60, 'Sign In', sign_function)
signin_page_btns.append(signin_btn)

signin_page_txt = []
signin_user_name_txt = TextField(WIDTH/2 - 75, 150, 150, 60, 'username',False,None)
signin_user_password_txt = TextField(WIDTH/2 - 75, 250, 150, 60, 'password',True,None)
signin_user_sec_password_txt = TextField(WIDTH/2 - 75, 350, 150, 60, 'second password',True,sign_function)
signin_page_txt.append(signin_user_name_txt)
signin_page_txt.append(signin_user_password_txt)
signin_page_txt.append(signin_user_sec_password_txt)


def loginPage():
    #TODO username text field, password text field, button login, button singin
    
    for btn in login_page_btns:
        btn.process()
    for txt in login_page_txt:
        txt.draw()

def homePage():
    #TODO username text field, password text field, button login, button singin
    screen.fill("0xFFFFFF")

def signinPage():
    #TODO username text field, password text field,second password text field,button singin
    for btn in signin_page_btns:
        btn.process()
    for txt in signin_page_txt:
        txt.draw()

def rouletePage():
    #TODO username text field, password text field, button login, button singin
    print("loginpage")

def slotPage():
    #TODO username text field, password text field, button login, button singin
    print("loginpage")

def coinflipPage():
    #TODO username text field, password text field, button login, button singin
    print("loginpage")

def accountPage():
    #TODO username text field, password text field, button login, button singin
    print("loginpage")

def aboutPage():
    #TODO username text field, password text field, button login, button singin
    print("loginpage")

def depositePage():
    #TODO username text field, password text field, button login, button singin
    print("loginpage")

def page(current_state):
    match current_state:
            case "login":
                loginPage()
            case "home":
                homePage()
            case "signin":
                signinPage()
            case "roulete":
                rouletePage()
            case "slot":
                slotPage()
            case "coinflip":
                coinflipPage()
            case "account":
                accountPage()
            case "about":
                aboutPage()
            case "deposite":
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
                
                login_function()
            # Check for backspace
            if event.key == pygame.K_BACKSPACE:
                text.user_text = text.user_text[:-1]
            elif(len(text.user_text)<text.max_length):
                text.user_text += event.unicode

while running:
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        text_field_events(event)
        
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("0x0F4C75")
    page(stage)
    
    
    
    
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()