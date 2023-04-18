import pygame

colors = {
    'background': '0x0F4C75',
    'buttons': '0x1B262C',
    'card_bg': '0x00B7C2',
    'btn_hover': '0x00B7C2',
    'text': '0xFDCB9E'
}

colors = {
    'background': '0x112B3C',
    'buttons': '0x205375',
    'card_bg': '0xF66B0E',
    'btn_hover': '0xF66B0E',
    'text': '0xEFEFEF'
}

colors = {
    'background': '0x222222',
    'buttons': '0x434242',
    'card_bg': '0x22A39F',
    'btn_hover': '0x22A39F',
    'text': '0xF3EFE0'
}

class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False, screen = None, stage = None, hidd_text = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        self.buttonText = buttonText
        self.screen = screen
        self.stage = stage
        self.hidd_text = hidd_text

        self.fillColors = {
            'normal' : colors["buttons"],
            'hover' : colors["btn_hover"],
            'pressed' : colors["btn_hover"],
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        font = pygame.font.SysFont('comicsans', 30,'0xF9D949', True)
        self.buttonSurf = font.render(str(self.buttonText), True,colors["text"])
        
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

        if self.buttonText == self.stage or self.hidd_text == self.stage and self.stage != None:
            self.buttonSurface.fill(self.fillColors['pressed'])
        

        self.buttonSurface.blit(self.buttonSurf, [
        self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
        self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
    ])
        self.screen.blit(self.buttonSurface, self.buttonRect)

class TextField():
    def __init__(self, x, y, width, height, textholder="default",isPassword=False,function =None, screen = None, static = False, alt_color = None):
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
        self.color_active = colors["btn_hover"]
        self.color_passive = colors["buttons"]
        self.color = colors["buttons"]
        self.alt_color = alt_color

        if alt_color == "green":
            self.color = "0x4f772d"
            self.color_passive = "0x4f772d"
        
        if alt_color == "black":
            self.color = "0x000000"
            self.color_passive = "0x000000"
        
        if alt_color == "red":
            self.color = "0x9d0208"
            self.color_passive = "0x9d0208"
        
        if alt_color == "9":
            self.max_length = 9
        
        self.screen = screen
        self.static = static
        

        self.textRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.active = False
        self.isSelected = False
        
        
    def draw(self):
        
        if self.isPassword and self.user_text!=self.textholder:
            string = ""
            for a in self.user_text:
                string+="*"
            text_surface = self.base_font.render(string, True, colors["text"])
        else:
            if self.alt_color == "9" :
                text_surface = self.base_font.render(self.user_text + " $", True, colors["text"])
            else:
                text_surface = self.base_font.render(self.user_text, True, colors["text"])
        pygame.draw.rect(self.screen, self.color , self.textRect)
        self.screen.blit(text_surface, (self.textRect.x+self.textRect.w/2-text_surface.get_width()/2, self.textRect.y + self.textRect.h/2-text_surface.get_height()/2)) 

 

#img =  pygame.image.load('racecar.png')
class GameCard():
    
    def __init__(self, x, y, width, height, title="game",btn_function =None,game_img =None, screen = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.title = title
        self.textRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.btn = Button(self.x+self.width/4, self.y+self.height+10, self.width*2/4, 45, "Play", btn_function, False, screen, None, " ")
        self.game_img = game_img
        self.base_font = pygame.font.Font(None,40)
        self.screen = screen

    def draw(self):
        
        text_surface = self.base_font.render(self.title, True, colors["text"])
        pygame.draw.rect(self.screen, colors["btn_hover"] , self.textRect)
        self.screen.blit(text_surface, (self.textRect.x +self.width /2-text_surface.get_width()/2, self.textRect.y))
        
        self.btn.process()


class Roulette():

    def __init__(self, screen):
        self.numbers = []
        self.position = 0
        self.title = "roulette"
        self.screen = screen

        self.bet_txt = []
        self.text_black_bet = TextField(20,200,150,60, "Your bet..", False, None, screen,False, "9")
        self.text_red_bet = TextField(20, 300, 150,60, "Your bet..", False, None, screen, False,"9")
        self.text_green_bet = TextField(20,400,150,60,"Your bet..", False, None,screen, False, "9")
        self.text_black = TextField(200, 200, 120,60, "Black", False, None, screen, True, "black")
        self.text_red = TextField(200, 300, 120,60, "Red", False, None, screen, True, "red")
        self.text_green = TextField(200, 400, 120,60, "Green", False, None, screen, True, "green")
        self.bets = []

        self.roulette_btns = []
        self.submit_btn = Button(70, 500, 200, 60, "Submit", False, None, screen)
        self.roulette_btns.append(self.submit_btn)
        self.bet_txt.append(self.text_black_bet)
        self.bet_txt.append(self.text_red_bet)
        self.bet_txt.append(self.text_green_bet)
        self.bet_txt.append(self.text_black)
        self.bet_txt.append(self.text_red)
        self.bet_txt.append(self.text_green)

    def draw(self):
        for txt in self.bet_txt:
            txt.draw()
        for btns in self.roulette_btns:
            btns.process()