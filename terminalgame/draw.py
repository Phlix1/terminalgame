from terminalgame.Surface import Surface
from terminalgame.Rect import Rect
def rect(surface, rect, pointtype='*', width=0,color=None):
    pointlist = []
    ptypelist = []
    if width==0:
        for top in range(rect.top, rect.top+rect.height):
            for left in range(rect.left, rect.left+rect.width):
                pointlist.append((left,top))
                ptypelist.append(pointtype)
    else:
        for top in range(rect.top, rect.top+rect.height):
            pointlist.append((rect.left, top))
            ptypelist.append(pointtype)
            pointlist.append((rect.left+rect.width-1, top))
            ptypelist.append(pointtype)                
        for left in range(rect.left, rect.left+rect.width):
            pointlist.append((left, rect.top))
            ptypelist.append(pointtype)
            pointlist.append((left, rect.top+rect.height-1))
            ptypelist.append(pointtype)   
    return surface.paint_point(pointlist, ptypelist)

def polygon():
    pass

def circle(surface, pos, radius, pointtype='*', width=0,color=None):
    pointlist = []
    ptypelist = []      
    for top in range(pos[1]-radius, pos[1]+radius+1):
        for left in range(pos[0]-radius, pos[0]+radius+1):
            if (top-pos[1])*(top-pos[1])+(left-pos[0])*(left-pos[0])<=radius*radius:
                pointlist.append((left, top))
                ptypelist.append(pointtype)
    if width!=0:
        pointlist_tmp = []
        ptypelist_tmp = []
        for p in pointlist:
            if (p[0]-1,p[1]) not in pointlist or\
               (p[0]+1,p[1]) not in pointlist or\
               (p[0],p[1]-1) not in pointlist or\
               (p[0],p[1]+1) not in pointlist:
                pointlist_tmp.append(p)
                ptypelist_tmp.append(pointtype)
        pointlist = pointlist_tmp
        ptypelist = ptypelist_tmp    
    return surface.paint_point(pointlist, ptypelist)

def ellipse():
    pass 

def line(surface, startpos, endpos, pointtype='*', color=None):
    pointlist = []
    ptypelist = []
    xstart = startpos[0]
    ystart = startpos[1]
    xend = endpos[0]
    yend = endpos[1]
    if xend==xstart:
        ymin = min(ystart, yend)
        ymax = max(ystart, yend)
        for y in range(ymin, ymax+1):
            pointlist.append((xstart, y))
            ptypelist.append(pointtype)
    elif yend==ystart:
        xmin = min(xstart, xend)
        xmax = max(xstart, xend)
        for x in range(xmin, xmax+1):
            pointlist.append((x, ystart))
            ptypelist.append(pointtype)            
    else:
        k = (yend-ystart)/(xend-xstart)
        b = ystart - k*xstart
        xmin = min(xstart, xend)
        xmax = max(xstart, xend)
        ymin = min(ystart, yend)
        ymax = max(ystart, yend)            
        for x in range(xmin, xmax+1):
            y = int(k*x+b)
            pointlist.append((x, y))
            ptypelist.append(pointtype)
        for y in range(ymin, ymax+1):
            x=int((y-b)/k)
            if (x,y) not in pointlist:
                pointlist.append((x,y))
                ptypelist.append(pointtype)
    return surface.paint_point(pointlist, ptypelist)