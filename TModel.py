from Frame import *

class TModel:
    def __init__(self,w,h):
        self.wid,self.hei=w,h
        self.mainFrame=Frame(w,h)
        self.overlapFrame=Frame(w,h)
        self.nextShape=Shape()
        self.score=0
        self.anchor=(0.0,0.0)
    def applyOverlap(self):
        sign=True
        for i in xrange(self.hei+4):
            for j in xrange(self.wid):
                if self.overlapFrame.frame[i-4][j]!=0:
                    if i-4<0:
                        sign=False
                    else:
                        self.mainFrame.frame[i-4][j]=self.overlapFrame.frame[i-4][j]
        self.overlapFrame.clear()
        return sign

    def eliminate(self):
        num=0
        for i in xrange(self.hei):
            for j in xrange(self.wid):
                if self.mainFrame.frame[i][j]==0:
                    break
            else:
                num+=1
                for m in xrange(i,-4,-1):
                    self.mainFrame.frame[m]=self.mainFrame.frame[m-1]
                self.mainFrame.frame[-4]=[0]*self.wid
        self.score+=int(num**1.5+0.5)*10
        return num!=0

    def releaseNewShape(self):
        self.overlapFrame.putShape(self.nextShape)
        self.anchor=(self.nextShape.anchor[0]-4,self.nextShape.anchor[1]+self.wid/2-2)
        self.nextShape=Shape()

    def fall(self):
        s=0
        for i in xrange(self.hei+4):
            for j in xrange(self.wid):
                s+=self.overlapFrame.frame[i-4][j]*self.mainFrame.frame[i-3][j]

        if s==0:
            self.anchor=(self.anchor[0]+1,self.anchor[1])
            for i in xrange(self.hei-1,-4,-1):
                    self.overlapFrame.frame[i]=self.overlapFrame.frame[i-1]
            self.overlapFrame.frame[-4]=[0]*self.wid
            return True
        else:
            return False

    def moveLeft(self):
        for i in xrange(self.hei+4):
            if self.overlapFrame.frame[i-4][0]!=0:
                return False
        for i in xrange(self.hei+4):
            for j in xrange(self.wid-1):
                if self.mainFrame.frame[i-4][j]*self.overlapFrame.frame[i-4][j+1]!=0:
                    return False

        self.anchor=(self.anchor[0],self.anchor[1]-1)
        for i in xrange(self.hei+4):
            for j in xrange(self.wid-1):
                self.overlapFrame.frame[i-4][j]=self.overlapFrame.frame[i-4][j+1]
            self.overlapFrame.frame[i-4][self.wid-1]=0
        return True


    def moveRight(self):
        for i in xrange(self.hei+4):
            if self.overlapFrame.frame[i-4][self.wid-1]!=0:
                return False
        for i in xrange(self.hei+4):
            for j in xrange(self.wid-1):
                if self.mainFrame.frame[i-4][j+1]*self.overlapFrame.frame[i-4][j]!=0:
                    return False

        self.anchor=(self.anchor[0],self.anchor[1]+1)
        for i in xrange(self.hei+4):
            for j in xrange(self.wid-1,0,-1):
                self.overlapFrame.frame[i-4][j]=self.overlapFrame.frame[i-4][j-1]
            self.overlapFrame.frame[i-4][0]=0
        return True

    def rotate(self):
        offset=0
        renew=[]
        for i in xrange(-4,self.hei):
            for j in xrange(self.wid):
                if self.overlapFrame.frame[i][j]!=0:
                    p=(self.anchor[0]-self.anchor[1]+j,
                        self.anchor[0]+self.anchor[1]-i)
                    p=(int(p[0]),int(p[1]))
                    renew.append(p+(self.overlapFrame.frame[i][j],))
                    if p[0]>=self.hei:      # too too low
                        return False
                    if p[1]<0:              # too left
                        offset=min(offset,p[1])
                    elif p[1]>=self.wid:    # too right
                        offset=max(offset,p[1]-self.wid+1)
                    elif self.mainFrame.frame[p[0]][p[1]]!=0:     #too low
                        return False

        self.overlapFrame.clear()
        for x in renew:
            self.overlapFrame.frame[x[0]][x[1]-offset]=x[2]
        return True
