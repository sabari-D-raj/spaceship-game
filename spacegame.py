import pygame
import sys
import random

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("musics/fearless.mp3")
pygame.mixer.music.play(-1)
fps=pygame.time.Clock()
width,height=800,800
screen=pygame.display.set_mode((width,height))
background= pygame.image.load("images/Parallax60.png").convert()
background=pygame.transform.scale(background,(width,height))
player= pygame.image.load("images/rockect.png").convert_alpha()
player=pygame.transform.scale(player,(100,100))
asteriod_img=pygame.image.load("images/asteriod.png").convert_alpha()
asteriod_img=pygame.transform.scale(asteriod_img,(200,200))
player_x,player_y=350,690
bg_visible,bg_above,bg_speed =0,-height,3

def create_rock():
    return {
        "x":random.randint(0,width-200),
        "y": random.randint(-1200,-200),
        "speed":random.randint(4,7)
    }
def reeset_asteriod(a):
    asteriod["x"] = random.randint(0, width - 200)
    asteriod["y"] = random.randint(-1200, -200)
    asteriod["speed"] = random.randint(4, 8)
def bullet_fire():
    bulletx=player_x+100  //2-bullet_width//2
    bullety=player_y
    rect=pygame.Rect(bulletx,bullety,bullet_width,bullet_height)
    bullet.append(rect)
laser=pygame.mixer.Sound("musics/lasergun.mp3")
destroy_a=pygame.mixer.Sound("musics/explosion.mp3")
def bullet_sound():
    laser.play()
def destroying():
    destroy_a.play()
asteriods=[]
bullet=[]
bullet_width,bullet_height= 8,12
bullet_speed=12
for i in range(5):
    asteriods.append(create_rock())
running=True
while running:
    fps.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                bullet_fire()
                bullet_sound() 
    bg_visible+=bg_speed
    bg_above+=bg_speed
    if bg_visible>=height:
        bg_visible= -height
    if bg_above >=height:
        bg_above= -height
    key=pygame.key.get_pressed()
    if key[pygame.K_d]:
        player_x+=5
    if key[pygame.K_a]:
        player_x-=5
    if player_x>=800 or player_x<=0:
        print("out")
    for asteriod in asteriods:
        asteriod["y"] += asteriod["speed"]
        if asteriod["y"] > height:
            reeset_asteriod(asteriod)
    for b in bullet[:]:
        b.y-=bullet_speed

    if asteriod["y"]>=height:
            asteriod["x"]=random.randint(0,width-200)
            asteriod["y"]=random.randint(-1200,-200)
            asteriod["speed"]=random.randint(4,7)
    screen.blit(background,(0,bg_visible))
    screen.blit(background,(0,bg_above))
    screen.blit(player,(player_x,player_y))
    for asteriod in asteriods:
        screen.blit(asteriod_img,(asteriod["x"],asteriod["y"]))
    for b in bullet:
        pygame.draw.rect(screen,(255,220,0),b)
    
    pygame.display.update()
pygame.quit()
sys.exit()