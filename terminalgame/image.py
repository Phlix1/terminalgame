from terminalgame.Surface import Surface
def load(filepath, index):
    with open(filepath, 'r') as f:
        line = f.readline()
        sflag = False
        pointlist = []
        ptypelist = []
        height = 0
        width = 0
        j=0
        while line:
            line = line[:-1]
            if line=='' and sflag==True:
                break
            if sflag:
                llen = len(line)
                for i in range(llen):
                    if line[i]!=' ':
                        pointlist.append((i, j))
                        ptypelist.append(line[i])
                        if i+1>width:
                            width = i + 1
                        if j+1>height:
                            height = j + 1
                j += 1
            if line==index:
                sflag = True
            line = f.readline()
        s = Surface(height, width)
        s.paint_point(pointlist, ptypelist)
        return s
        


