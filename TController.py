from TModel import *
from TView import *

class TController:
    def __init__(self,w=10,h=15):
        self.speed=400  #ms
        self.model=TModel(w,h)
        self.view=TView()

        self.view.window.bind("<Left>",self.moveLeftEvent)
        self.view.window.bind("<Right>",self.moveRightEvent)
        self.view.window.bind("<Down>",self.fastFallEvent)
        self.view.window.bind("<Up>",self.rotateEvent)
        self.view.pauseBtn.config(command=self.pauseEvent)
        self.failState=False
        self.pauseState=False
    def start(self):
        self.model.releaseNewShape()
        self.onTimer()
        self.view.window.mainloop()
    def failed(self):
        self.failState=True
        self.view.failedAnimation(self.model.score)
        self.view.window.quit()
    def onTimer(self):
        if self.failState or self.pauseState:
            return
        if not self.model.fall():
            if not self.model.applyOverlap():
                self.failed()
                return
            if self.model.eliminate():
                self.view.updateScore(self.model.score)
            self.model.releaseNewShape()

        self.view.refreshWindow(self.model)
        self.view.window.after(self.speed,self.onTimer)

    def moveLeftEvent(self,event):
        if self.pauseState:
            return
        if self.model.moveLeft():
            self.view.refreshWindow(self.model)

    def moveRightEvent(self,event):
        if self.pauseState:
            return
        if self.model.moveRight():
            self.view.refreshWindow(self.model)
    def fastFallEvent(self,event):
        if self.pauseState:
            return
        while self.model.fall():pass
        self.view.refreshWindow(self.model)

    def rotateEvent(self,event):
        if self.pauseState:
            return
        if self.model.rotate():
            self.view.refreshWindow(self.model)

    def pauseEvent(self):
        if self.pauseState:
            self.pauseState=False
            self.view.pauseBtn.config(text="Pause")
            self.view.window.after(self.speed,self.onTimer)
        else:
            self.pauseState=True
            self.view.pauseBtn.config(text="Resume")
