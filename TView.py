from Tkinter import *
from tkMessageBox import *
import Shape


class TView:
    def __init__(self):
        self.window=Tk()
        self.window.title("Tetrix")
        self.window.geometry("700x700")

        self.scene=Canvas(self.window,height=700,width=700)
        self.scene.pack()

        self.scene.create_rectangle(50,50,450,650,tags="SceneBorder",width=2)
        self.scene.create_text(575,75,text="Next Shape")
        self.scene.create_text(575,300,text="Score")
        self.scene.create_rectangle(500,100,650,250,tags="NextBorder",width=2)

        self.scoreLabel=Label(self.window,text="0")
        self.scoreLabel.place(x=575,y=320,anchor=N)

        self.pauseBtn=Button(self.window,text="Pause")
        self.pauseBtn.place(x=575,y=400,anchor=N)
        self.blocks=[]
    def refreshWindow(self,model):
        for x in self.blocks:
            self.scene.delete(x)

        w=400/model.wid
        for i in xrange(model.hei):
            for j in xrange(model.wid):
                c=model.overlapFrame.frame[i][j]+model.mainFrame.frame[i][j]
                if c!=0:
                    self.blocks.append(
                        self.scene.create_rectangle(50+j*w,50+i*w,
                                                    50+(j+1)*w,50+(i+1)*w,
                                                    fill=Shape.toColor(c)))

        w=150/4
        for i in xrange(4):
            for j in xrange(4):
                if model.nextShape.shape[i][j]!=0:
                    self.blocks.append(
                        self.scene.create_rectangle(500+j*w,100+i*w,
                                                    500+(j+1)*w,100+(i+1)*w,
                                                    fill=Shape.toColor(model.nextShape.shape[i][j])))


    def eliminateAnimation(self):    #
        pass
    def updateScore(self,score):
        self.scoreLabel.config(text="%d"%score)
    def failedAnimation(self,score):
        showwarning("Tetrix","Game Over\nYour score is %d"%score)
if __name__=="__main__":
    v=TView()
    v.window.mainloop()
