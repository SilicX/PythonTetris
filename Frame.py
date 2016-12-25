from Shape import *

class Frame:
    def __init__(self,w,h):
        self.wid,self.hei=w,h
        self.frame=[ [0]*w for i in xrange(h+5)]    #-4 -3 -2 -1 0~hei-1
        for i in xrange(w):
            self.frame[h][i]=-1

    def putShape(self,shape):
        for i in xrange(4):
            for j in xrange(4):
                self.frame[i-4][j+self.wid/2-2]=shape.shape[i][j]

    def clear(self):
        self.frame=[ [0]*self.wid for i in xrange(self.hei+5)]
        for i in xrange(self.wid):
            self.frame[self.hei][i]=-1

    def __str__(self):
        s=""
        for i in xrange(self.hei+5):
            for j in xrange(self.wid):
                s+="%d"%self.frame[i-4][j]
            s+='\n'
        return s


if __name__=="__main__":
    from Shape import *
    f=Frame(10,24)
    f.putShape(Shape())
    print f
