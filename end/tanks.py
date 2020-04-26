import pygame, random
from math import *
pygame.init()
pygame.mixer.init()
rad = pi/180
size = [800,600]
window = pygame.display.set_mode(size)
pygame.display.set_caption("Tanks")
fps = pygame.time.Clock()
#Rainbow
rainbow = ((255,0,0)),(255,165,0),(255,255,0),(0,255,0),(0,191,255),(0,0,255),(128,0,128))
#Words
Font = pygame.font.SysFont("Times New Roman", 32)
#Tank
class Tank:

    def __init__(self,x,y,color,number):
        self.x = x
        self.y = y
        self.color = color
        self.size = 32
        self.number = number
        self.hitbox = pygame.Rect(self.x,self.y,self.size,self.size)
        self.velocity = 50
        self.angle = 180*self.number
        self.width = 5
        self.length = 20
        self.center = [(self.x+self.size/2),(self.y+self.size/2)]
        self.rotate_velocity = 30
        self.start = 0
        self.hp = 10
        self.m = True
        self.direct = ""

    def move(self,k,sec):
        self.speed = self.velocity*sec
        self.rotate_speed = self.rotate_velocity*sec
        #MovingKeeps
        if k[pygame.K_n]:
            self.m = 1
        elif k[pygame.K_m]:
            self.m =0
            
        #Player 1
        if k[pygame.K_q] and self.number ==0:
            self.angle-=self.rotate_speed
        elif k[pygame.K_e] and self.number ==0:
            self.angle+=self.rotate_speed 
        if k[pygame.K_w] and self.number ==0:
            if not(self.m):
                self.y-=self.speed 
            self.direct = "UP"
        elif k[pygame.K_s] and self.number ==0:
            if not(self.m):
                self.y+=self.speed 
            self.direct = "DOWN"
        elif k[pygame.K_a] and self.number ==0:
            if not(self.m):
                self.x-=self.speed 
            self.direct = "LEFT"
        elif k[pygame.K_d] and self.number ==0:
            if not(self.m):
                self.x+=self.speed 
            self.direct = "RIGHT"
        if k[pygame.K_SPACE] and self.number == 0 and (pygame.time.get_ticks() - self.start)/1000 >=1:
            self.start = pygame.time.get_ticks()
            color = random.choice(rainbow)
            bullet.append(Bullet(self.center[0]+2*self.length*cos(self.angle*rad),self.center[1]+2*self.length*sin(self.angle*rad),self.angle,color))
            pygame.mixer.music.load('shotoftank.wav')
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.09)

        #Player 2
        if k[pygame.K_k] and self.number ==1:
            self.angle-=self.rotate_speed 
        elif k[pygame.K_l] and self.number ==1:
            self.angle+=self.rotate_speed 
        if k[pygame.K_UP] and self.number ==1:
            if not(self.m):
                self.y-=self.speed 
            self.direct = "UP"
        elif k[pygame.K_DOWN] and self.number ==1:
            if not(self.m):
                self.y+=self.speed 
            self.direct = "DOWN"
        elif k[pygame.K_LEFT] and self.number ==1:
            if not(self.m):
                self.x-=self.speed
            self.direct = "LEFT"
        elif k[pygame.K_RIGHT] and self.number ==1:
            if not(self.m):
                self.x+=self.speed
            self.direct = "RIGHT"
        if k[pygame.K_RETURN] and self.number ==1 and (pygame.time.get_ticks() - self.start)/1000 >=1:
            self.start = pygame.time.get_ticks()
            color = random.choice(rainbow)
            bullet.append(Bullet(self.center[0]+2*self.length*cos(self.angle*rad),self.center[1]+2*self.length*sin(self.angle*rad),self.angle,color))
            pygame.mixer.music.load('shotoftank.wav')
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.08)
        #Rules for both
        if self.x>800:
            self.x = 0
        elif self.x<0-self.size:
            self.x = 800
        elif self.y>600:
            self.y = 0
        elif self.y<0-self.size:
            self.y = 600
        if self.m:
            if self.direct == "UP":
                self.y-=self.speed
            elif self.direct == "DOWN":
                self.y+=self.speed
            elif self.direct =="LEFT":
                self.x-=self.speed
            elif self.direct == "RIGHT":
                self.x+=self.speed
        self.center = [(self.x+self.size/2),(self.y+self.size/2)]
        self.hitbox = pygame.Rect(self.x,self.y,self.size,self.size)
        self.collision()
        self.draw()

    def collision(self):
        for f in bullet:
            if self.hitbox.colliderect(f.rect):
                pygame.mixer.music.load('collision.wav')
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(0.08)
                self.hp-=1
                bullet.remove(f)

    def draw(self):
        pygame.draw.rect(window, self.color, (self.x,self.y,self.size,self.size))
        pygame.draw.line(window, (0,random.randint(0,255),0),self.center, (self.center[0]+2*self.length*cos(self.angle*rad),self.center[1]+2*self.length*sin(self.angle*rad)),self.width)
        pygame.draw.circle(window, (0,random.randint(0,255),0),(round(self.center[0]),round(self.center[1])), 8)

#Bullet:
class Bullet:
    def __init__(self,x,y,angle,color):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 15
        self.bullet = pygame.Surface((5,5))
        self.bullet.fill((color))
        self.rect = self.bullet.get_rect()

    def move(self):
        self.x +=self.speed*cos(self.angle*rad)
        self.y +=self.speed*sin(self.angle*rad)
        self.rect.center = (self.x,self.y)
        self.draw()
        if self.x>=800 or self.x<=0 or self.y>=600 or self.y<=0:
            return 1
        return 0

    def draw(self):
        old = self.rect.center
        new = pygame.transform.rotate(self.bullet, self.angle)
        self.rect = new.get_rect()
        self.rect.center = old
        window.blit(new,self.rect)

bullet = []

class Game:

    def message(self, msg, color):
        self.mesg = Font.render(msg, True, color)
        window.blit(self.mesg, [size[0]//5,size[1]//3])

    game_over = False
    game_close = False

    tank_1 = Tank(600,300,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),1)
    tank_2 = Tank(200,200,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),0)
    tank = [tank_1,tank_2]
    
    effect = pygame.mixer.Sound("background1.wav")
    effect.play()
    effect.set_volume(0.03)
    def play(self):
        while not self.game_over:                
            mils = fps.tick(30)
            sec = mils/1000
            for f in pygame.event.get():
                if f.type == pygame.QUIT:
                    self.game_over = True

            window.fill((178,178,178))
            window.blit(Font.render(f"Hp:{self.tank[0].hp}",1,(255,0,0)),(700,0))
            window.blit(Font.render(f"Hp:{self.tank[1].hp}",1,(0,255,0)),(50,0))
            k = pygame.key.get_pressed()

            for f in self.tank:
                f.move(k,sec)
            for f in bullet:
                if f.move():
                    bullet.remove(f)
            
            if self.tank[0].hp == 0 or self.tank[1].hp == 0:
                self.game_close = True
                while self.game_close :
                    window.fill((178,178,178))
                    self.message("Game Over! Press 2-Play Again or 1 , Esc-Quit",[213,50,80])
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_1 or event.key == pygame.K_ESCAPE:
                                self.game_over = True
                                self.game_close = False
                            if event.key == pygame.K_2:
                                self.game_over = False
                                self.game_close = False
                                for f in self.tank:
                                    f.hp = 10
                                for i in self.tank:
                                    i.x = random.randint(0,768)
                                    i.y = random.randint(0,568)
                                

            pygame.display.update()

game = Game()
game.play()   
