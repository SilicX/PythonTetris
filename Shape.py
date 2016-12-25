import random

def toColor(n):
    cl=("red", "yellow", "blue", "green", "purple", "orange", "brown", "gray")
    return cl[n-1]

class Shape:
    def __init__(self):
        self.shape=[[0]*4]*4
        self.color=random.randint(1,8)
        # red yellow blue green purple orange brown grey
        self.randomShape()
    def randomShape(self):
        c=random.randint(1,7)
        n=self.color
        if(c==1):
            self.shape=[[0,n,0,0],
                        [0,n,0,0],
                        [0,n,0,0],
                        [0,n,0,0]]
            self.anchor=(1,1)
        elif(c==2):
            self.shape=[[0,0,0,0],
                        [0,n,0,0],
                        [0,n,0,0],
                        [0,n,n,0]]
            self.anchor=(2,1)
        elif(c==3):
            self.shape=[[0,0,0,0],
                        [0,0,n,0],
                        [0,0,n,0],
                        [0,n,n,0]]
            self.anchor=(2,2)
        elif(c==4):
            self.shape=[[0,0,0,0],
                        [0,0,n,0],
                        [0,n,n,0],
                        [0,n,0,0]]
            self.anchor=(2,1)
        elif(c==5):
            self.shape=[[0,0,0,0],
                        [0,n,0,0],
                        [0,n,n,0],
                        [0,0,n,0]]
            self.anchor=(2,1)
        elif(c==6):
            self.shape=[[0,0,0,0],
                        [0,0,0,0],
                        [0,n,n,0],
                        [0,n,n,0]]
            self.anchor=(2.5,1.5)
        elif(c==7):
            self.shape=[[0,0,0,0],
                        [0,n,0,0],
                        [0,n,n,0],
                        [0,n,0,0]]
            self.anchor=(2,1)

    def __str__(self):
        s=""
        for i in xrange(4):
            for j in xrange(4):
                s+="%d"%self.shape[i][j]
            s+='\n'
        return s

if __name__=="__main__":
    print Shape()
