class Rect:
    def __init__(self, left, top, width, height):
        if left<0 or top<0 or width<0 or height<0:
            left = top = width = height = 0
        self.left = left
        self.top = top
        self.width = width
        self.height = height
    def collidepoint(self, x, y):
        if x>=self.left and x<self.left+self.width and y>=self.top and y<self.top+self.height:
            return True
        else:
            return False
    def colliderect(self, rect):
        lefttopx = rect.left
        lefttopy = rect.top
        leftbotx = rect.left
        leftboty = rect.top+rect.height-1
        righttopx = rect.left+rect.width-1
        righttopy = rect.top
        rightbotx = rect.left+rect.width-1
        rightboty = rect.top+rect.height-1
        if self.collidepoint(lefttopx, lefttopy) or\
           self.collidepoint(leftbotx, leftboty) or\
           self.collidepoint(righttopx, righttopy) or\
           self.collidepoint(rightbotx, rightboty):
            return True
        else:
            return False