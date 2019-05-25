class Sprite(object):
    def __init__(self, *groups):
        self.__g={}
        if groups:
            self.add(*groups)

    def add(self, *groups):
        has = self.__g.__contains__
        for group in groups:
            if not has(group):
                group.add_internal(self)
                self.add_internal(group)

    def add_internal(self, group):
        self.__g[group] = 0

    def remove_internal(self, group):
        del self.__g[group]

    def remove(self, *groups):
        has = self.__g.__contains__
        for group in groups:
            if has(group):
                group.remove_internal(self)
                self.remove_internal(group)     
        
    def update(self, *args):
        pass

    def kill(self):
        for c in self.__g:
            c.remove_internal(self)
        self.__g.clear()
        
    def groups(self):
        return list(self.__g)

class Group(object):

    def __init__(self):
        self.spritedict = {}
        self.lostsprites = []   

    def sprites(self):
        return list(self.spritedict)

    def add_internal(self, sprite):
        self.spritedict[sprite] = 0

    def remove_internal(self, sprite):
        r = self.spritedict[sprite]
        if r:
            self.lostsprites.append(r)
        del self.spritedict[sprite]

    def has(self, sprite):
        return sprite in self.spritedict

    def add(self, *sprites):
        for sprite in sprites:
            if not self.has(sprite):
                self.add_internal(sprite)
                sprite.add_internal(self)

    def remove(self, *sprites):
        for sprite in sprites:
            if self.has_internal(sprite):
                self.remove_internal(sprite)
                sprite.remove_internal(self)

    def update(self, *args):
        for s in self.sprites():
            s.update(*args)

    def draw(self, surface):
        sprites = self.sprites()
        surface_blit = surface.blit
        for spr in sprites:
            self.spritedict[spr] = surface_blit(spr.image, spr.rect)
        self.lostsprites = []

    def empty(self):
        for s in self.sprites():
            self.remove_internal(s)
            s.remove_internal(self)

    def __len__(self):
        return len(self.sprites())

def collide_rect(left, right):
    return left.rect.colliderect(right)

def spritecollide(sprite, group, dokill, collided=None):
    if dokill:
        crashed = []
        for s in group.sprites():
            if sprite.rect.colliderect(s.rect):
                s.kill()
                crashed.append(s)
        return crashed
    else:
        return [s for s in group if sprite.rect.colliderect(s.rect)]

def groupcollide(groupa, groupb, dokilla, dokillb, collided=None):
    crashed = {}
    if dokilla:
        for s in groupa.sprites():
            c = spritecollide(s, groupb, dokillb, collided)
            if c:
                crashed[s] = c
                s.kill()
    else:
        for s in groupa:
            c = spritecollide(s, groupb, dokillb, collided)
            if c:
                crashed[s] = c
    return crashed