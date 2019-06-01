import terminalgame
import random
from terminalgame.Rect import Rect
from terminalgame.locals import *
from terminalgame.Surface import Surface
import time
COLORS = ('o', '#')
# 模板的宽高
TEMPLATEWIDTH = 5
TEMPLATEHEIGHT = 5
fallFreq = 0.27
# 形状_S（S旋转有2种）
S_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '..OO.',
                     '.OO..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '...O.',
                     '.....']]

# 形状_Z（Z旋转有2种）
Z_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '.O...',
                     '.....']]

# 形状_I（I旋转有2种）
I_SHAPE_TEMPLATE = [['..O..',
                     '..O..',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     'OOOO.',
                     '.....',
                     '.....']]

# 形状_O（O旋转只有一个）
O_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '.OO..',
                     '.....']]

# 形状_J（J旋转有4种）
J_SHAPE_TEMPLATE = [['.....',
                     '.O...',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..OO.',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '...O.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '.OO..',
                     '.....']]

# 形状_L（L旋转有4种）
L_SHAPE_TEMPLATE = [['.....',
                     '...O.',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '.O...',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '..O..',
                     '..O..',
                     '.....']]

# 形状_T（T旋转有4种）
T_SHAPE_TEMPLATE = [['.....',
                     '..O..',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '..O..',
                     '.....']]

# 定义一个数据结构存储，对应的形状
PIECES = {'S': S_SHAPE_TEMPLATE,
          'Z': Z_SHAPE_TEMPLATE,
          'J': J_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE,
          'O': O_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE}


WINDOWWIDTH = 50#整个游戏屏幕的宽
WINDOWHEIGHT = 50#整个游戏屏幕的高
# 放置俄罗斯方块窗口的大小
BOARDWIDTH = 20 
BOARDHEIGHT = 20
BLANK = '.' # 代表空的形状

XMARGIN = 0
TOPMARGIN = 0
BOXSIZE = 2

# board边界
def isOnBoard(x, y):
    return x >= 0 and x < BOARDWIDTH and y < BOARDHEIGHT

# piece在当前的board里是否是一个合法可用的位置
def isValidPosition(board, piece, adjX=0, adjY=0):
    # Return True if the piece is within the board and not colliding
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            isAboveBoard = y + piece['y'] + adjY < 0
            if isAboveBoard or PIECES[piece['shape']][piece['rotation']][y][x] == BLANK:
                continue
            if not isOnBoard(x + piece['x'] + adjX, y + piece['y'] + adjY):
                return False
            if board[x + piece['x'] + adjX][y + piece['y'] + adjY] != BLANK:
                return False
    return True

def addToBoard(board, piece): #游戏板数据结构用来记录之前着陆的砖块。该函数所做的事情是接受一个砖块数据结构，并且将其上的有效砖块添加到游戏板数据结构中
    for x in range(TEMPLATEWIDTH): #该函数这在一个砖块着陆之后进行
        for y in range(TEMPLATEHEIGHT):#嵌套for遍历了5x5砖块数据结构,当找到一个有效砖块时，将其添加到游戏板中
            if PIECES[piece['shape']][piece['rotation']][y][x] != BLANK:
                board[x + piece['x']][y + piece['y']] = piece['color'] #游戏板数据结构的值有两种形式：数字(表示砖块颜色)，'.'即空白，表示该处没有有效砖块

def getNewPiece():
    # return a random new piece in a random rotation and color
    shape = random.choice(list(PIECES.keys()))
    newPiece = {'shape': shape,
                'rotation': random.randint(0, len(PIECES[shape]) - 1),
                'x': int(BOARDWIDTH / 2) - int(TEMPLATEWIDTH / 2), # x居中
                'y': -1, # y在屏幕的上方，小于0
                'color': random.randint(0, len(COLORS)-1)}
    return newPiece

def getBlankBoard(): #创建一个新的游戏板数据结构。
    board = [] #创建一个空白的游戏板
    for i in range(BOARDWIDTH):# range(10)=[0,9]    BOARDWIDTH=10   BLANK = '.' #表示空白空格
        board.append([BLANK] * BOARDHEIGHT)
    #board[0]-board[9]每一个变量的值都是20个.组成的列表   
    return board

def drawWindow(screen):
    lefttopx = int((WINDOWWIDTH - BOARDWIDTH * BOXSIZE)/2)
    lefttopy = int((WINDOWHEIGHT - BOARDHEIGHT * BOXSIZE)/2)
    global XMARGIN
    XMARGIN = lefttopx
    global TOPMARGIN
    TOPMARGIN = lefttopy
    rightbottomx = int(lefttopx + BOARDWIDTH * BOXSIZE)
    rightbottomy = int(lefttopy + BOARDHEIGHT * BOXSIZE)
    for i in range(lefttopy, rightbottomy):
        screen.image[i][lefttopx-1]='|'
        screen.image[i][rightbottomx]='|'
    for j in range(lefttopx, rightbottomx):
        screen.image[lefttopy-1][j]='-'
        screen.image[rightbottomy][j]='-'        

def drawBoard(screen, board):
    drawWindow(screen)
    for x in range(BOARDWIDTH):#遍历游戏板
        for y in range(BOARDHEIGHT):
            drawBox(screen, x, y, board[x][y])#这个函数会自动找出有效方块并绘制

def convertToPixelCoords(boxx, boxy):#将游戏板上方块的坐标转化成像素坐标
    return (XMARGIN + (boxx * BOXSIZE)), (TOPMARGIN + (boxy * BOXSIZE))#XMARGIN为游戏板左顶点的横坐标，TOPMARGIN为游戏板左顶点的纵坐标

def drawBox(screen, boxx, boxy, color, pixelx=None, pixely=None):#绘制一个有效方块
    if color == BLANK: #如果这不是一个有效方块，这是5x5一个空白
        return
    if pixelx == None and pixely == None:
        pixelx, pixely = convertToPixelCoords(boxx, boxy)#将游戏板上方块的坐标转化成像素坐标
    terminalgame.draw.rect(screen, Rect(pixelx, pixely, BOXSIZE, BOXSIZE), pointtype=COLORS[color])#留出1像素的空白，这样才能在砖块中看到组成砖块

def drawPiece(screen, piece, pixelx=None, pixely=None):#pixelx, pixely为5x5砖块数据结构左上角在游戏板上的的坐标
    shapeToDraw = PIECES[piece['shape']][piece['rotation']]#PIECES[piece['shape']][piece['rotation']]为一个图形的一种旋转方式
    if pixelx == None and pixely == None: 
        pixelx, pixely = convertToPixelCoords(piece['x'], piece['y'])#将砖块坐标转换为像素坐标。
    for x in range(TEMPLATEWIDTH): #遍历5x5砖块数据结构
        for y in range(TEMPLATEHEIGHT):
            if shapeToDraw[y][x] != BLANK:
                drawBox(screen, None, None, piece['color'], pixelx+(x * BOXSIZE), pixely + (y * BOXSIZE))

def isCompleteLine(board, y):#判断y行是否填满，填满返回True
    for x in range(BOARDWIDTH):#遍历该行的所有砖块
        if board[x][y] == BLANK:#如果存在空白，则没填满
            return False
    return True

def removeCompleteLines(board):#删除所有填满行，每删除一行要将游戏板上该行之上的所有方块都下移一行。返回删除的行数
    numLinesRemoved = 0
    y = BOARDHEIGHT - 1 # BOARDHEIGHT=20-1=19即从最低行开始
    while y >= 0:#注意当删除一行时y没有生变化，因为此时它的值已经更新为新的一行了
        if isCompleteLine(board, y):#如果该行填满
            for pullDownY in range(y, 0, -1):  #range(y, 0, -1)范围[y,1]
                for x in range(BOARDWIDTH):
                    board[x][pullDownY] = board[x][pullDownY-1]#将删除的行之上的每一行的值都复制到下一行
            for x in range(BOARDWIDTH):#删除第一行
                board[x][0]=BLANK
            numLinesRemoved=numLinesRemoved+1
        else:
            y =y- 1 #移到下一行
    return numLinesRemoved

if __name__ == "__main__":
    terminalgame.init()
    screen = terminalgame.display.set_mode(WINDOWHEIGHT,WINDOWWIDTH,border=True)
    height = terminalgame.display.height
    width = terminalgame.display.width
    lastFallTime = time.time()#最后下落砖块的时间
    movingDown = False #没有按下向下方向键
    movingLeft = False #没有按下向左方向键
    movingRight = False #没有按下向右方向键
    board = getBlankBoard()
    fallingPiece = getNewPiece()
    clock = terminalgame.time.Clock()
    scores = 0
    while True:
        clock.tick(20)
        if fallingPiece == None:
            fallingPiece = getNewPiece()
            if not isValidPosition(board, fallingPiece):
                terminalgame.quit()
                exit()
        for event in terminalgame.event.get():
            if event.type == KEYUP:
                if (event.key == K_LEFT):#判断当前弹起的按键是否为左方向键
                    movingLeft = False #是的话置为False,表示玩家不再想要让砖块朝着该方向移动。
                elif (event.key == K_RIGHT):#同上
                    movingRight = False
                elif (event.key == K_DOWN):#同上
                    movingDown = False
                elif event.key == K_q:
                    terminalgame.quit()
                    exit()                
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT) and isValidPosition(board, fallingPiece, adjX=-1):
                    fallingPiece['x'] = fallingPiece['x'] -1 #左移
                    movingLeft = True #将movingLeft变量设置为True，并且为了确保落下的砖块不会既向左又向右移动
                    movingRight = False #将 movingRight设置为False
                elif (event.key == K_RIGHT ) and isValidPosition(board, fallingPiece, adjX=1): #同上
                    fallingPiece['x'] =fallingPiece['x'] + 1
                    movingRight = True
                    movingLeft = False
                elif event.key == K_UP :
                    fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(PIECES[fallingPiece['shape']])
                    if not isValidPosition(board, fallingPiece):
                        fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(PIECES[fallingPiece['shape']])
                elif (event.key == K_DOWN ):
                    movingDown = True # movingDown设置为True
                    if isValidPosition(board, fallingPiece, adjY=1):#下一个位置有效
                        fallingPiece['y'] =  fallingPiece['y'] +1  #移动

        if time.time() - lastFallTime > fallFreq:#fallFreq向下移动的速率
            if not isValidPosition(board, fallingPiece, adjY=1):#当砖块下一个位置无效时，即表示砖块当前已经着陆了。
                addToBoard(board, fallingPiece) #在游戏板数据结构中记录这个着陆的砖块
                scores += removeCompleteLines(board)# removeCompleteLines()将负责删除掉游戏板上任何已经填充完整的行，并且将方块向下推动。
                fallingPiece = None#最后我们将fallingPiece变量设置为None,以表示下一个砖块应该变为新的下落砖块，并且应该生成一个随机的新砖块作为下一个砖块。？？？？？？
            else:
                # 如果砖块没有着陆，我们直接将其Y位置向下设置一个空格，并且将lastFallTime重置为当前时间
                fallingPiece['y'] = fallingPiece['y'] +1
                lastFallTime = time.time()
        screen.fill()
        scores_sur = Surface(1,30)
        scores_image = list("scores: "+str(scores))
        em_len = 30 - len(scores_image)
        em_image = ["" for i in range(em_len)]
        scores_image.extend(em_image)
        scores_sur.image = [scores_image]
        screen.blit(scores_sur, Rect(0,0,0,0))
        drawBoard(screen, board)
        if fallingPiece != None:#砖块没有下落到底部
            drawPiece(screen, fallingPiece)
        terminalgame.display.flip()
    terminalgame.quit()
