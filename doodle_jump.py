import pygame,time,random#,threading

import pygame.event as GAME_EVENTS
pygame.init()
window = pygame.display.set_mode((300,450))
pygame.mouse.set_visible(0)
pygame.init()
clock= pygame.time.Clock()
"""
for t in range(1,10):
    window.fill((0,0,0))
    vy=a*t
    y+=vy
    print(y)
    pygame.draw.circle(window,(255,255,255),(x,y),5)
    
    pygame.display.update()
    time.sleep(0.1)
a=-10    
for t in range(10,1):
    window.fill((0,0,0))
    vy=a*t
    y+=vy
    print(y)
    pygame.draw.circle(window,(255,255,255),(x,y),5)

    pygame.display.update()
    time.sleep(0.1)
#######
def bouncing():
    x=250
    y=250
    vx=10
    while True:#for i in range(1,100):
        window.fill((0,0,0))
        
        vx+=-1 if x>=250 else 1
        x+=vx
        pygame.draw.circle(window,(255,255,255),(x,y),5)
        
        pygame.display.update()
        time.sleep(0.1)
for i in range(3):
    t=threading.Thread(target=bouncing)
    t.start()
    time.sleep(0.5)

#######
x=250
y=250
vx=10
while True:#for i in range(1,100):
    window.fill((0,0,0))
      
    vx+=20 if vx==-10 else -1

    
    x+=vx
    pygame.draw.circle(window,(255,255,255),(x,y),5)   
    pygame.display.update()
    time.sleep(0.1)

#####
x=0
y=250
vy=10
while True:
    window.fill((0,0,0))
      
    vy+=20 if vy==-10 else -1
    x+=-500 if x==500 else 5
    y-=vy
    pygame.draw.circle(window,(255,255,255),(x,y),5)   
    pygame.display.update()
    time.sleep(0.05)
"""
class brick():
    Height=6
    Width=30
    Y=-10 # 10
    Vx=0
    Vy=0
    def __init__(self,x):
        self.X=x
    def move(self):
        self.X+=self.Vx
        self.Y+=self.Vy 
    def draw(self):
        pygame.draw.rect(window,(0,255,0),(self.X-(self.Width/2),self.Y-(self.Height/2),self.Width,self.Height),0)

class player():
    X=150
    Y=450
    Vy=0
    def init(self):
        pass
    def move(self):
        self.X=pygame.mouse.get_pos()[0]
        self.Y+=self.Vy
    def draw(self):
        pygame.draw.circle(window,(255,0,0),(self.X,self.Y),2)

def onBrick():
    global newPlayY
    oldPlayY=newPlayY
    newPlayY=Player.Y
    for i in bricks:
        if i.X-(i.Width/2)<Player.X<i.X+(i.Width/2) and (oldPlayY<i.Y-i.Height<newPlayY or i.Y==(oldPlayY or newPlayY)):
            onbrick=True
            break
        else:
            onbrick=False
    return onbrick


def vCalc(Vygen):
    #General
    #print(Vygen)
    global score
    if onBrick()==True:
        Vygen=jumpIntensity
    else:
        Vygen+=1#int(jumpIntensity/-10)
        
    #Player
    if Player.Y>maxHeight or Vygen>0:
        Player.Vy=Vygen
    #Bricks
    else:
        Player.Vy=0
        Vybricks=-Vygen
        score+=-Vygen

    for i in bricks:
        try:
            i.Vy=Vybricks
        except:
            i.Vy=0
    return Vygen
def delete():
    global playing
    for i in bricks:
        if i.Y>450:
            bricks.remove(i)
    if Player.Y>500:
        playing=0
def move():
    #Player
    Player.move()
    #Bricks
    for i in bricks:
        i.move()

def draw():
    #Player
    Player.draw()
    #Bricks
    for i in bricks:
        i.draw()

playing=0
Player=player()

while True:
    print("hi")
    playing=1#playing=input("Play?")
    bricks=[]
    score=0
    #für vCalc
    jumpIntensity=-20
    maxHeight=200
    Vygen=-50
    #für onBrick
    newPlayY=0
    time.sleep(3)
    while playing==1:
        clock.tick(15)
        window.fill((0,0,0))
        pygame.display.set_caption("Score:"+str(score))
        

        #brickSpawn
        
        try:
            if random.randint(1,len(bricks))==1:
                bricks.append(brick(random.randint(30,240)))
        except:
            bricks.append(brick(random.randint(30,240)))

        Vygen=vCalc(Vygen)

        move()
        #print (Player.X)
        delete()

        draw()

        pygame.display.update()

        for event in GAME_EVENTS.get():
            pass
    pygame.display.set_caption("Your score:"+str(score))
            
