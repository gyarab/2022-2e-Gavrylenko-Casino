# Example file showing a basic pygame "game loop"
import pygame
#from MyButton import Button


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
#https://www.geeksforgeeks.org/how-to-create-a-text-input-box-with-pygame/
class TextField():
    def __init__(self, x, y, width, height, textholder="default"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.base_font = pygame.font.Font(None, 32)
        self.user_text = textholder
        self.color_active = pygame.Color('lightskyblue3')
        self.color_passive = pygame.Color('chartreuse4')
        self.fillColors = {
            'normal' : '0x1B262C',
            'hover' : '0x0F4C75',
            'pressed' : '0x00B7C2',
        }

        self.textRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.active = False
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.textRect.collidepoint(event.pos):
                    self.active = True
                else:
                    self.active = False
    
            if event.type == pygame.KEYDOWN:
    
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
    
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
    
                # Unicode standard is used for string
                # formation
                else:
                    user_text += event.unicode
    def draw(self):
        text_surface = self.base_font.render(self.user_text, True, (255, 255, 255))
        screen.blit(text_surface, (self.textRect.x+5, self.textRect.y+5))  
        self.textRect.w = max(100, text_surface.get_width()+10)      

def myFunction():
    pygame.init()
    screen2 = pygame.display.set_mode((1280, 720))
    clock2 = pygame.time.Clock()
    running2 = True
    while running2:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running2 = False

        # fill the screen with a color to wipe away anything from last frame
        screen2.fill("0xFFFFFF")
        # stage home, login, singin, roulete, slot, coinflip, account, about, deposite
        

        
        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()
        clock2.tick(60)  # limits FPS to 60

def sign_function():
    stage = "signin"

def login_function():
    None

gey = Button(30, 30, 400, 100, 'Слава', myFunction)

login_page_btns = []
singin_btn = Button(WIDTH/2 - 75, 550, 150, 60, 'Sign In', sign_function)
login_btn = Button(WIDTH/2 - 125, 450, 250, 60, 'Login', login_function)

login_page_txt = []
user_name_txt = TextField(WIDTH/2 - 75, 150, 150, 60, 'username')
user_password_txt = TextField(WIDTH/2 - 75, 250, 150, 60, 'password')
login_page_txt.append(user_name_txt)
login_page_txt.append(user_password_txt)
login_page_btns.append(singin_btn)
login_page_btns.append(login_btn)

def loginPage():
    #TODO username text field, password text field, button login, button singin
    print("loginpage")
    for btn in login_page_btns:
        btn.process()
    for txt in login_page_txt:
        txt.draw()

def homePage():
    #TODO username text field, password text field, button login, button singin
    print("loginpage")

def singinPage():
    #TODO username text field, password text field, button login, button singin
    print("loginpage")

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
            case "singin":
                singinPage()
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


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("0x0F4C75")
    page(stage)
    
    
    
    
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()