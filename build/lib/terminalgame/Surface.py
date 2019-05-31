import numpy as np
from terminalgame.Rect import Rect
class Surface:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.image =[['' for col in range(width)] for row in range(height)]
    def load_img(self, img):
        h, w = np.array(img).shape
        if h==self.height and w==self.width:
            self.image = img
            return True
        else:
            return False
    def paint_point(self, pointlist, ptypelist):
        pnum = len(pointlist)
        if len(ptypelist)!=pnum:
            return Rect(0,0,0,0)
        min_left = self.width+100
        min_top = self.height+100
        max_left = 0
        max_top = 0
        for i in range(pnum):
            left = pointlist[i][0]
            top = pointlist[i][1]
            if left>=0 and left<self.width and\
               top>=0 and top<self.height:
                self.image[top][left] = ptypelist[i]
                if top<min_top:
                    min_top = top
                if left<min_left:
                    min_left = left
                if top>max_top:
                    max_top = top
                if left>max_left:
                    max_left = left
        return Rect(min_left, min_top, (max_left-min_left+1), (max_top-min_top+1))
    def blit(self, source, dest, area=None):
        srcimg = source.image
        sel_h = 0
        sel_w = 0
        if area!=None:
            if area.top<source.height and area.left<source.width:
                sel_h = min(source.height-area.top, area.height)
                sel_w = min(source.width-area.left, area.width)
                sel_part = [['' for col in range(sel_w)] for row in range(sel_h)]
                for i in range(sel_h):
                    for j in range(sel_w):
                        sel_part[i][j] = srcimg[area.top+i][area.left+j]
        else:
            sel_part = srcimg
            sel_h = source.height
            sel_w = source.width
        active_top = 0
        active_left = 0
        active_height = 0
        active_width = 0
        for i in range(dest.top, dest.top+sel_h):
            for j in range(dest.left, dest.left+sel_w):
                if i<self.height and j<self.width and i>=0 and j>=0 and sel_part[i-dest.top][j-dest.left]!='':
                    self.image[i][j] = sel_part[i-dest.top][j-dest.left]
                    active_top = dest.top
                    active_left = dest.left
                    if i-dest.top+1>active_height:
                        active_height = i-dest.top+1
                    if j-dest.left+1>active_width:
                        active_width = j-dest.left+1
        return Rect(active_top, active_left, active_height, active_width)        
    def fill(self):
        for i in range(self.height):
            for j in range(self.width):
                self.image[i][j]=''        