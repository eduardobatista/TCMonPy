from PySide2.QtCore import QThread,QTimer,QMutex,QWaitCondition

mutex = QMutex()

condwait = QWaitCondition()

wthread = QThread()  

class TimerThread(QThread):

    def __init__(self):
        super().__init__()
        self.ttimer = QTimer()
        self.ttimer.setInterval(1000)
        self.started.connect(self.ttimer.start)
    
    def connectWithTimer(self,func):
        self.ttimer.timeout.connect(func)

    def stopTimer(self):
        self.timer.stop()

    def setTimerInterval(self,interval):
        self.ttimer.setInterval(interval)

mytimer = TimerThread()

