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

        if self.buttonText == self.stage or self.hidd_text == self.stage:
            self.buttonSurface.fill(self.fillColors['pressed'])
        

        self.buttonSurface.blit(self.buttonSurf, [
        self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
        self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
    ])
        self.screen.blit(self.buttonSurface, self.buttonRect)

class TextField():
    def __init__(self, x, y, width, height, textholder="default",isPassword=False,function =None, screen = None):
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
        self.screen = screen

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
            text_surface = self.base_font.render(self.user_text, True, colors["text"])
        pygame.draw.rect(self.screen, self.color , self.textRect)
        self.screen.blit(text_surface, (self.textRect.x+self.textRect.w/2-text_surface.get_width()/2, self.textRect.y+30)) 
        self.textRect.w = max(300, text_surface.get_width()+10)    

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
