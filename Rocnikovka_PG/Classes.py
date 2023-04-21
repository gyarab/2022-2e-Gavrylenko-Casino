import pygame , math, Database, random

colors = {
    'background': '0x222222',
    'buttons': '0x434242',
    'card_bg': '0x22A39F',
    'btn_hover': '0x22A39F',
    'text': '0xF3EFE0',
    'red' : '0x9d0208',
    'green' : '0x4f772d',
    'black' : '0x000000'

}
clock = pygame.time.Clock()
money = 0

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
        if alt_color == "36":
            self.max_length = 2
        
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
        pygame.draw.rect(self.screen, colors["btn_hover"], self.textRect)
        self.screen.blit(text_surface, (self.textRect.x +self.width /2-text_surface.get_width()/2, self.textRect.y))
        
        self.btn.process()


class RouletteBall():
    def __init__(self, screen, x,y):
        self.x = x
        self.y = y
        self.screen = screen
        self.radius = 10
    
    def draw(self):
        pygame.draw.circle( self.screen, colors["text"], (self.x, self.y), self.radius, self.radius)

    
class RouletteBet():
    def __init__(self,bet,type,number = None):
        self.type = type
        self.bet = bet
        self.number = number
        self.color = colors["text"]
        

class Roulette():

    def __init__(self, screen,username):
        self.numbers = []
        self.position = 0
        self.screen = screen
        self.ball = RouletteBall(screen,825,336)
        self.base_font = pygame.font.Font(None, 32)
        self.username = username

        self.bet_txt = []
        self.text_black_bet = TextField(20,200,150,60, "Your bet..", False, None, screen,False, "9")
        self.text_red_bet = TextField(20, 300, 150,60, "Your bet..", False, None, screen, False,"9")
        self.text_green_bet = TextField(20,400,150,60,"Your bet..", False, None,screen, False, "9")
        self.text_number_bet = TextField(20,500,150,60,"Your bet..", False, None,screen, False, "9")
        self.text_black = TextField(200, 200, 120,60, "Black", False, None, screen, True, "black")
        self.text_red = TextField(200, 300, 120,60, "Red", False, None, screen, True, "red")
        self.text_green = TextField(200, 400, 120,60, "Green", False, None, screen, True, "green")
        self.text_number = TextField(200, 500, 120,60, "0-36", False, None, screen, False, "36")
        self.bet_txt.append(self.text_black_bet)
        self.bet_txt.append(self.text_red_bet)
        self.bet_txt.append(self.text_green_bet)
        self.bet_txt.append(self.text_black)
        self.bet_txt.append(self.text_red)
        self.bet_txt.append(self.text_green)
        self.bet_txt.append(self.text_number)
        self.bet_txt.append(self.text_number_bet)


        self.bets = []
        self.prev_bets = []
        self.bets_win = []
        self.roulette_btns = []
        self.win_num = -1

        self.submit_btn = Button(70, 600, 200, 60, "Submit", self.add_bet, False , screen)
        self.play_btn = Button(550, 600, 200, 60, "Play", self.play_game, False , screen)
        self.roulette_btns.append(self.submit_btn)
        self.roulette_btns.append(self.play_btn)
        
        

    def draw_circle(self,x,y):
    
        pygame.draw.ellipse(self.screen, "0x000000", pygame.Rect(x,y,400,400), 200)

        center_x = x + 200
        center_y = y + 200
        r = 220
        numbers = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
        angle = (360 * math.pi)/(37*180)
        
        for i in range(0, 37):
            if i % 2 == 0:
                pygame.draw.arc(self.screen, "0x9d0208", pygame.Rect(x, y, 400, 400), angle * i, angle * (i + 1), 150)
            else :
                pygame.draw.arc(self.screen, "0x000000", pygame.Rect(x, y, 400, 400), angle * i, angle * (i + 1), 150)
            if i == 0:
                pygame.draw.arc(self.screen, "0x4f772d", pygame.Rect(x, y, 400, 400), angle * i, angle * (i + 1), 150)

            new_x = round(r * math.cos(angle * (i - 0.5) ) + center_x - 11)
            new_y = round(r * math.sin(angle * (i - 0.5) ) + center_y - 11)

            text_surface = self.base_font.render(str(numbers[i]), True, "0xF3EFE0")
            self.screen.blit(text_surface, (new_x, new_y))
    

    def draw(self):
        for txt in self.bet_txt:
            txt.draw()
        self.submit_btn.process()
        if (len(self.bets)>0):
            self.play_btn.process()
        self.play_btn
        self.draw_circle(450,150)
        for i in range(0,len(self.bets)):
            
            if (self.bets[i].type == "number"):
                text_surface = self.base_font.render(str(self.bets[i].bet)+" $"+" on number "+str(self.bets[i].number), True, "0xF3EFE0")
            else:
                text_surface = self.base_font.render(str(self.bets[i].bet)+" $"+" on "+self.bets[i].type, True, "0xF3EFE0")
            self.screen.blit(text_surface, (1260-text_surface.get_width(), 220+i*20))
        
        if len(self.bets) == 0:
            for i in range(0,len(self.prev_bets)):
                
                if (self.prev_bets[i].type == "number"):
                    text_surface = self.base_font.render(str(self.prev_bets[i].bet)+" $"+" on number "+str(self.prev_bets[i].number), True, self.prev_bets[i].color)
                else:
                    text_surface = self.base_font.render(str(self.prev_bets[i].bet)+" $"+" on "+self.prev_bets[i].type, True, self.prev_bets[i].color)
                self.screen.blit(text_surface, (1260-text_surface.get_width(), 220+i*20))
        self.ball.draw()
        
    def add_bet(self):
        data = Database.load_data(self.username)
        money = data[1]
        roulete_wins = data[2]
        slot_wins = data[3]
        coin_wins = data[4]

        if(self.text_black_bet.user_text != self.text_black_bet.textholder and money >= int(self.text_black_bet.user_text)):
            bet = int(self.text_black_bet.user_text)
            self.bets_win.append(bet*2)
            self.bets.append(RouletteBet(bet,"black"))
            money -= bet
            self.text_black_bet.user_text = self.text_black_bet.textholder 
        if(self.text_red_bet.user_text != self.text_red_bet.textholder and money >= int(self.text_red_bet.user_text)):
            bet = int(self.text_red_bet.user_text)
            self.bets_win.append(bet*2)
            self.bets.append(RouletteBet(bet,"red"))
            money -= bet
            self.text_red_bet.user_text = self.text_red_bet.textholder
        if(self.text_green_bet.user_text != self.text_green_bet.textholder and money >= int(self.text_green_bet.user_text)):
            bet = int(self.text_green_bet.user_text)
            self.bets_win.append(bet*50)
            self.bets.append(RouletteBet(bet,"green"))
            money -= bet
            self.text_green_bet.user_text = self.text_green_bet.textholder
        if(self.text_number_bet.user_text != self.text_number_bet.textholder and self.text_number.user_text != self.text_number.textholder and money >= int(self.text_number_bet.user_text)):
            bet = int(self.text_number_bet.user_text)
            self.bets_win.append(bet*35)
            self.bets.append(RouletteBet(bet,"number",int(self.text_number.user_text)))
            money -= bet
            self.text_number_bet.user_text = self.text_number_bet.textholder
            self.text_number.user_text = self.text_number.textholder
    
        Database.update(self.username,money,roulete_wins,slot_wins,coin_wins)

    def play_game(self):
        self.ball_animation()
        print("konec")
        self.bet_process()


    def bet_process(self):
        data = Database.load_data(self.username)
        money = data[1]
        roulete_wins = data[2]
        slot_wins = data[3]
        coin_wins = data[4]
        numbers = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
        #TODO procces bets (for bet in bets)
        index = numbers.index(self.win_num)

        for i in range(0,len(self.bets)):
            if (self.bets[i].number == self.win_num):
                    money += self.bets_win[i]
                    self.bets[i].color =colors["green"]
                    roulete_wins+=1
                    continue
            if (index == 0):
                if (self.bets[i].type == "green"):
                    money += self.bets_win[i]
                    self.bets[i].color =colors["green"]
                    roulete_wins+=1
                    continue

            if (index %2 == 0) and (index != 0):
                if (self.bets[i].type == "black"):
                    money += self.bets_win[i]
                    self.bets[i].color =colors["green"]
                    roulete_wins+=1
                    continue

            if (index %2 == 1):
                if (self.bets[i].type == "red"):
                    money += self.bets_win[i]
                    self.bets[i].color =colors["green"]
                    roulete_wins+=1
                    continue
            self.bets[i].color =colors["red"]
            
            #chcek na number bet
        #write cod above ↑
        self.prev_bets =self.bets
        self.bets = []
        self.bets_win = []
        Database.update(self.username,money,roulete_wins,slot_wins,coin_wins)


    def ball_animation(self):
        center_x = 450 + 200
        center_y = 150 + 200
        r = 160
        def loop(speed):
            for i in range(0,360):
                angle = math.pi/180
                new_x = round(r * math.cos(angle * (i - 0.5) ) + center_x )
                new_y = round(r * math.sin(angle * (i - 0.5) ) + center_y )
                self.ball.x =new_x
                self.ball.y =new_y
                
                
                self.draw_circle(450,150)
                self.ball.draw()
                clock.tick(speed)
                pygame.display.flip()
        numbers = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
        self.win_num = random.choice(numbers)
        
        def slow(number, speed):
            stop_angle = (360 * math.pi)/(37*180) * numbers.index(number) 
            stop_in_degree = round((360)/(37) * numbers.index(number))
            for i in range(0,360): 
                angle = math.pi/180
                new_x = round(r * math.cos(angle * (i - 0.5) ) + center_x )
                new_y = round(r * math.sin(angle * (i - 0.5) ) + center_y )
                self.ball.x =new_x
                self.ball.y =new_y
                if(angle * (i - 0.5)>=stop_angle):
                    break
                self.draw_circle(450,150)
                self.ball.draw()
                clock.tick(speed)
                pygame.display.flip()
            for i in range(stop_in_degree,stop_in_degree+360 -3):
                angle = math.pi/180
                new_x = round(r * math.cos(angle * (i - 0.5) ) + center_x )
                new_y = round(r * math.sin(angle * (i - 0.5) ) + center_y )
                self.ball.x =new_x
                self.ball.y =new_y
                self.draw_circle(450,150)
                self.ball.draw()
                clock.tick((speed-3) * ((stop_in_degree+357-i)/(stop_in_degree+357)) + 3)
                pygame.display.flip()
                
        
        #animation
        loop(1000)
        loop(500)
        loop(400)
        slow(self.win_num,300)

class Coin():
    def __init__(self,x,y,screen) -> None:
        self.x = x
        self.y = y
        self.screen =screen
        self.b = 100
        self.color = colors["green"]
    def draw(self):
        pygame.draw.ellipse(self.screen,self.color, pygame.Rect(self.x,self.y,200,200), 180)

class CoinGame():
    def __init__(self,screen, username):
        self.screen = screen
        self.username = username
        self.coin = Coin(450,150,screen)
        self.screen = screen
        self.base_font = pygame.font.Font(None, 32)
        self.username = username
        self.bet = [-1,False]# [100,True]
        self.btns = []
        self.bets_win = 0
        self.bet_color = False
        self.coin_random = False
        
        self.submit_btn = Button(700, 600, 200, 60, "Submit", self.add_bet, False , screen)
        self.play_btn = Button(550, 400, 200, 60, "Play", self.play_game, False , screen)
        self.green_btn = Button(70, 600, 200, 60, "Green", self.select_green, False , screen)
        self.red_btn = Button(450, 600, 200, 60, "Red", self.select_red, False , screen)
        self.btns.append(self.submit_btn)
        self.btns.append(self.green_btn)
        self.btns.append(self.red_btn)

        self.text_number_bet = TextField(20,500,150,60,"Your bet..", False, None,screen, False, "9")

    def draw(self):
        for btn in self.btns:
            
            btn.process()
        self.text_number_bet.draw()
        if self.bet[0] != -1:  
            self.play_btn.process()
        self.coin.draw()

    def bet_process(self):
        data = Database.load_data(self.username)
        money = data[1]
        roulete_wins = data[2]
        slot_wins = data[3]
        coin_wins = data[4]
        #TODO procces bets (for bet in bets)

        
        if (self.bet[1] == self.coin_random):
                money += self.bets_win * 2
                coin_wins+=1
        
           
            
        self.bet = [-1,-1]
        self.bets_win = 0
        Database.update(self.username,money,roulete_wins,slot_wins,coin_wins)

    def play_game(self):
        
        self.coin_random = random.choice([True,False])
        
        self.animation()
        self.bet_process()
        self.text_number_bet.user_text = self.text_number_bet.textholder
        self.green_btn.fillColors["normal"] = colors["black"]
        self.green_btn.fillColors["hoover"] = colors["black"]
        self.red_btn.fillColors["normal"] = colors["black"]
        self.red_btn.fillColors["hoover"] = colors["black"]

    def animation(self):
        print("animation!")
        
        def loop(speed):
            b = 0
            while(self.coin.b-b>0):
                b +=1
                pygame.draw.rect(self.screen,colors["background"],pygame.Rect(self.coin.x,self.coin.y,200,200),200)
                pygame.draw.ellipse(self.screen, colors["green"], pygame.Rect(self.coin.x,self.coin.y+b,200,200-2*b), 200)
                pygame.display.flip()
                clock.tick(speed)
            
            b = 100
            while(b>0):
                b -=1
                pygame.draw.rect(self.screen,colors["background"],pygame.Rect(self.coin.x,self.coin.y,200,200),200)
                pygame.draw.ellipse(self.screen, colors["red"], pygame.Rect(self.coin.x,self.coin.y+b,200,200-2*b), 200)
                pygame.display.flip()
                clock.tick(speed)
            b = 0
            while(self.coin.b-b>0):
                b +=1
                pygame.draw.rect(self.screen,colors["background"],pygame.Rect(self.coin.x,self.coin.y,200,200),200)
                pygame.draw.ellipse(self.screen, colors["red"], pygame.Rect(self.coin.x,self.coin.y+b,200,200-2*b), 200)
                pygame.display.flip()
                clock.tick(speed)
            
            b = 100
            while(b>0):
                b -=1
                pygame.draw.rect(self.screen,colors["background"],pygame.Rect(self.coin.x,self.coin.y,200,200),200)
                pygame.draw.ellipse(self.screen, colors["green"], pygame.Rect(self.coin.x,self.coin.y+b,200,200-2*b), 200)
                pygame.display.flip()
                clock.tick(speed)
        def end():
            if self.coin_random == False:
                b = 0
                while(self.coin.b-b>0):
                    b +=1
                    pygame.draw.rect(self.screen,colors["background"],pygame.Rect(self.coin.x,self.coin.y,200,200),200)
                    pygame.draw.ellipse(self.screen, colors["green"], pygame.Rect(self.coin.x,self.coin.y+b,200,200-2*b), 200)
                    pygame.display.flip()
                    clock.tick(300)
            
                b = 100
                while(b>0):
                    b -=1
                    pygame.draw.rect(self.screen,colors["background"],pygame.Rect(self.coin.x,self.coin.y,200,200),200)
                    pygame.draw.ellipse(self.screen, colors["red"], pygame.Rect(self.coin.x,self.coin.y+b,200,200-2*b), 200)
                    pygame.display.flip()
                    clock.tick(300)
                self.coin.color = colors["red"]
            else:
                self.coin.color = colors["green"]

        num = random.randint(2,5)
        for i in range(0,num):
            loop(300)
        end()
        
            




    def add_bet(self):
        if(self.bet_color != "black" and self.text_number_bet.user_text != self.text_number_bet.textholder):
            
            data = Database.load_data(self.username)
            money = data[1]
            roulete_wins = data[2]
            slot_wins = data[3]
            coin_wins = data[4]
            if (money>int(self.text_number_bet.user_text)):
                
                self.bets_win = int(self.text_number_bet.user_text)
                money -= self.bets_win
            

                self.bet = [int(self.text_number_bet.user_text),self.bet_color] 
                
                Database.update(self.username,money,roulete_wins,slot_wins,coin_wins)
    


    def select_green(self):
        self.bet_color = True
        self.select_color(True)
    def select_red(self):
        self.bet_color = False
        self.select_color(False)
        

    def select_color(self,color):
        if(color):
            self.green_btn.fillColors["normal"] = colors["green"]
            self.green_btn.fillColors["hoover"] = colors["green"]
            self.green_btn.fillColors["pressed"] = colors["green"]

            self.red_btn.fillColors["normal"] = colors["black"]
            self.red_btn.fillColors["hoover"] = colors["black"]
        else:
            self.red_btn.fillColors["normal"] = colors["red"]
            self.red_btn.fillColors["hoover"] = colors["red"]
            self.red_btn.fillColors["pressed"] = colors["red"]


            self.green_btn.fillColors["normal"] = colors["black"]
            self.green_btn.fillColors["hoover"] = colors["black"]
    