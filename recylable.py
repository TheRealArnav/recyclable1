import pygame
from pygame.locals import*
import random
import time
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((900,700))

winorlose = "start"
reyclablelist = ["C:/Pygame2/images/item1.png","C:/Pygame2/images/pencil.png","C:/Pygame2/images/box.png"]
score = 0
clock = pygame.time.Clock()

starttime = time.time()

def bgchange(winorlose):
    if winorlose == "start":
        bg = pygame.image.load("C:/Pygame2/images/background,eco.png")
        bg = pygame.transform.scale(bg,(900,700))
        screen.blit(bg,(0,0))
    if winorlose == "win":
        screen.fill("green")
    if winorlose == "lose":
        screen.fill("red")
    
class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Pygame2/images/bin.png")
        self.image = pygame.transform.scale(self.image,(35,50))
        self.rect = self.image.get_rect()
    def Draw(self):
          
        key =  pygame.key.get_pressed()
        if key[K_UP]:
            self.rect.y = self.rect.y - 5
        if key[K_DOWN]:
            self.rect.y = self.rect.y + 5
        if key[K_RIGHT]:
            self.rect.x = self.rect.x + 5
        if key[K_LEFT]:
            self.rect.x = self.rect.x - 5

class recyclable(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image,(25,40))
        self.rect = self.image.get_rect()

class nonrecyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Pygame2/images/plasticbag.png")
        self.image = pygame.transform.scale(self.image,(25,40))
        self.rect = self.image.get_rect()


bingroup = pygame.sprite.Group()
bin = Bin()
bingroup.add(bin)
allsprites = pygame.sprite.Group()
allsprites.add(bin)
recylclablegroup = pygame.sprite.Group()
nonrecyclablegroup = pygame.sprite.Group()

for i in range(50):
    item = recyclable(random.choice(reyclablelist))
    item.rect.x = random.randint(0,900)
    item.rect.y = random.randint(0,700)
    allsprites.add(item)
    recylclablegroup.add(item)

for i in range(25):
    item = nonrecyclable()
    item.rect.x = random.randint(0,900)
    item.rect.y = random.randint(0,900)
    allsprites.add(item)
    nonrecyclablegroup.add(item)

font = pygame.font.SysFont("Calibri",25)
timerfont = pygame.font.SysFont("Ariel",25)
winorlosefont = pygame.font.SysFont("Impact",60)
scoredisplayed = font.render("Score: "+str(score),True,(0,0,0))
screen.blit(scoredisplayed,(20,20))

run = True
while run:
    clock.tick(60)
    timeelapsed = time.time() - starttime
    if timeelapsed >= 60:
        if score > 40:
            msg = winorlosefont.render("YOU WIN",True,(0,0,0))
            winorlose = "win"
            screen.blit(msg,(450,350))            
            pygame.display.update()
        if score < 40:
            msg = winorlosefont.render("YOU LOSE",True,(0,0,0))
            winorlose = "lose"
            screen.blit(msg,(450,350))
            pygame.display.update()
    else:
        msg1 = timerfont.render("Time left: "+str(60-int(timeelapsed)),True,(0,0,0))
        screen.blit(msg1,(20,50))
        pygame.display.update()
        print(msg1)    
    bgchange(winorlose)
    allsprites.draw(screen)
    bin.Draw()
    scoredisplayed = font.render("Score"+str(score),True,(0,0,0))
    screen.blit(scoredisplayed,(20,20))
    
    recyclablehitlist = pygame.sprite.spritecollide(bin,recylclablegroup,True)
    nonrecyclablehitlist = pygame.sprite.spritecollide(bin,nonrecyclablegroup,True)
    for i in recyclablehitlist:
        score = score + 2
        scoredisplayed = font.render("Score"+str(score),True,(0,0,0))
    for i in nonrecyclablehitlist:
        score = score - 5
        scoredisplayed = font.render("Score"+str(score),True,(0,0,0))
    screen.blit(scoredisplayed,(20,20))

    for event in pygame.event.get():
        if event.type == QUIT:
            quit()

    if winorlose == "win" or winorlose == "lose":
        pygame.sprite.Sprite.kill(allsprites)
    pygame.display.flip()