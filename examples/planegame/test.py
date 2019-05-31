import terminalgame
import terminalgame.time
from terminalgame.Rect import Rect
import curses
from terminalgame.Surface import Surface
import terminalgame.draw as draw
from terminalgame.sprite import Sprite, Group
import terminalgame.display
import terminalgame.key
import terminalgame.event as event
from terminalgame.locals import *
from sys import exit 
import random
import terminalgame.image
offset = {K_LEFT:0, K_RIGHT:0, K_UP:0, K_DOWN:0}
class Ball(Sprite):
    def __init__(self, init_pos):
        Sprite.__init__(self)
        self.image = Surface(10,10)
        self.image = terminalgame.image.load("./resource.txt","enemy")
        self.rect = init_pos
        self.rect.height = self.image.height
        self.rect.width = self.image.width
        self.speed = 1
    def move(self):
        self.rect.top = self.rect.top+self.speed

class Bullet(Sprite):
    def __init__(self, init_pos):
        Sprite.__init__(self)
        self.image = terminalgame.image.load("./resource.txt","bullet")
        self.rect = init_pos
        self.rect.height = self.image.height
        self.rect.width = self.image.width
        self.speed = 1
    def move(self):
        self.rect.top = self.rect.top-self.speed    
        
class Plane(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = terminalgame.image.load("./resource.txt","plane")
        self.rect = Rect(30,30,10,10)
        self.rect.height = self.image.height
        self.rect.width = self.image.width
        self.midtop = Rect(int(self.rect.left+self.image.width/2)-1, \
                           self.rect.top, \
                           0, 0)
        self.is_hit = False
        self.bullets = Group()
    def update(self, dx, dy, width, height):
        if self.rect.left+dx>=0 and self.rect.left+dx<width-8:
            self.rect.left = self.rect.left+dx
        if self.rect.top+dy>=0 and self.rect.top+dy<height-4:
            self.rect.top = self.rect.top+dy
    
    def get_midtop(self):
        return Rect(int(self.rect.left+self.image.width/2)-1, \
                           self.rect.top, \
                           0, 0)
    def shoot(self):
        bullet = Bullet(self.get_midtop())
        self.bullets.add(bullet)
        
        
if __name__ == "__main__":
    terminalgame.init()
    screen = terminalgame.display.set_mode(80,80,border=True)
    height = terminalgame.display.height
    width = terminalgame.display.width
    plane = Plane()
    group2 = Group()
    group2.add(plane)
    shoot_frequency = 0
    enemy_frequency = 0
    scores = 0
    enemies = Group()
    clock = terminalgame.time.Clock()
    while True:
        clock.tick(20)
        if enemy_frequency % 10 == 0:
            enemy_pos = Rect(random.randint(0, width - 5), 0, 0 ,0)
            enemy = Ball(enemy_pos)
            enemies.add(enemy) 
        enemy_frequency += 1
        if enemy_frequency >= 100:
            enemy_frequency = 0
            
        if shoot_frequency % 3 == 0:
            plane.shoot()
        shoot_frequency += 1
        if shoot_frequency >= 15:
            shoot_frequency = 0

        screen.fill()
        testx = 0
        testy = 0
        for enemy in enemies:
            enemy.move()
            if terminalgame.sprite.collide_rect(enemy, plane):
                enemies.remove(enemy)
                plane.is_hit = True
                break
            if enemy.rect.top > width:
                enemies.remove(enemy)
                #enemy.kill()
        
        for bullet in plane.bullets:
            bullet.move()
            if bullet.rect.top < 0:
                plane.bullets.remove(bullet)
                #bullet.kill()
        
        killed = terminalgame.sprite.groupcollide(enemies, plane.bullets, 1, 1, collided=None)
        scores += len(killed.keys())
        scores_sur = Surface(1,30)
        scores_image = list("scores: "+str(scores))
        em_len = 30 - len(scores_image)
        em_image = ["" for i in range(em_len)]
        scores_image.extend(em_image)
        scores_sur.image = [scores_image]
               
        plane.bullets.draw(screen)
        enemies.draw(screen)
        screen.blit(scores_sur, Rect(0,0,0,0))
           
        for e in event.get():
            if e.type == KEYDOWN:
                if e.dict['key'] in offset and not plane.is_hit:
                    offset[e.dict['key']] = 2
            elif e.type == KEYUP:
                if e.dict['key'] in offset:
                    offset[e.dict['key']] = 0
                if e.dict['key'] == K_q:
                    terminalgame.quit()
                    exit()
        
        offset_x = offset[K_RIGHT] - offset[K_LEFT] + testx
        offset_y = offset[K_DOWN] - offset[K_UP] + testy
        offset[K_RIGHT] = offset[K_LEFT] = offset[K_DOWN] = offset[K_UP]=0
        

        group2.update(offset_x, offset_y, width, height)
        group2.draw(screen)
        if plane.is_hit:
            gameover = Surface(1,9)
            gameover.image = [list("GAME OVER")]
            screen.blit(gameover, Rect(int(width/2-gameover.width/2),\
                        int(height/2-gameover.height/2),\
                        gameover.width, gameover.height))
            terminalgame.display.flip()
            re_flag = False
            while True:
                for e in event.get():
                    if e.type == KEYUP:
                        if e.dict['key'] == K_q:
                            terminalgame.quit()
                            exit()
                        elif e.dict['key'] == K_r:
                            shoot_frequency = 0
                            enemy_frequency = 0
                            scores = 0
                            group2.empty()
                            enemies.empty()
                            plane = Plane()
                            group2.add(plane)
                            re_flag = True
                            break
                if re_flag:
                    break                
            continue                                
        terminalgame.display.flip()
    
