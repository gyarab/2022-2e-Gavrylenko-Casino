from tkinter import *
import pygame 
clock = pygame.time.Clock()

# Funkce show(game) obsahuje 3 casy : "Roulette", "Slot" a "Coinflip".
# Každý case znamená hru, kde v pravé dolní části je tlačítko "?". Po kliknuti se zobrazi nove okno s pravidlami her a sazek.
def show(game):
    window = Tk()

    match game:
        case "Roulette":
            window.title(game+" info")
            text = "In this game, a player may choose to place a bet on a single number, the color red, black or green. \n To determine the winning number, a croupier (in my case the croupier is a player) \n spins a ball in the direction around a circular track running around the outer edge of the wheel. \n The ball eventually loses momentum and falls onto the wheel \n and into one of thirty-eight colored and numbered pockets on the wheel. \n In my game, I also made my own kind of bets. \n The player can bet on any color as well as on any number. \n If he wins red or black - the program pays him a bet multiplied by 2. \n If the ball hits the green color, the player gets a bet multiplied by 50. \n If a concrete number wins, then the bet is multiplied by 35. \n On the right side of the screen there are 4 fields for placing bets, \n after pressing Submit button the Play button will appear and on the left side the bets will be displayed. \n Bets can be maximum 20. \n After the ball stops, the bets that have won will light up in green, \n  and those that have not, will light up in red. \n Good luck!!!"
            lbl = Label(window, text=text, font=("Arial Bold", 20),bg = '#222222', fg="#F3EFE0")
            window.configure(bg='#222222')
            lbl.grid(column=0, row=0)
            
        case "Slot":
            window.title(game+" info")
            text = "A slot machine is a gambling game with spinning reels. \n Those reels have numbers on them, which land randomly after you place a bet and spin the reels. \n If these numbers line up, you win prizes based on which symbols fall on that “payline”. \n In this game, a player may choose to place a bet. \n After the player makes a bet, the Play button will appear. \n After pressing it the game will start. \n If 3 identical numbers fall, it is jackpot, the player gets the bet multiplied by 15. \n If the same first and second or second and third numbers, the player gets the bet multiplied by 5. \n If the numbers are in order, the player gets the bet multiplied by 3. \n he last chance to win is when the sum of digits is more than 18. \n Then the bet is multiplied by 2. \n Good luck!!!" 
            lbl = Label(window, text=text, font=("Arial Bold", 20),bg = '#222222', fg="#F3EFE0")
            window.configure(bg='#222222')
            lbl.grid(column=0, row=0)
            
        case "Coinflip":
            window.title(game+" info")
            text = "This is a game of Flip coin, where the player can put on one side or the other of the coin. \n  In this case on the red or green side. \n Only one bet can be placed. The Play button appears. \n Press it and the coin will start spinning. \n If the side on which the player bet falls out, he gets the bet multiplied by two. \n Good luck!!!"
            lbl = Label(window, text=text, font=("Arial Bold", 20),bg = '#222222', fg="#F3EFE0")
            window.configure(bg='#222222')
            lbl.grid(column=0, row=0)
    
    window.mainloop()
    
    
