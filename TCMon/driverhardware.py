import serial
import time
import threading
import struct
import math

from .dataman import dataman

from PyQt5.QtCore import QTimer,QObject,QThread,pyqtSignal,QMutex,QWaitCondition


class PID:

    def __init__(self,setpoint=0,kp=1,ki=0,kd=0,ts=1):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint
        self.ts = ts
        self.error = 0
        self.output = 0

    def reset(self):
        self.error = 0
        self.output = 0
        self.integral = 0

    def update(self,reading):
        self.lasterror = self.error
        self.error = self.setpoint - reading
        self.integral = self.integral + (self.error*self.ts)
        self.derivada = (self.error - self.lasterror) / self.ts
        self.output = self.kp * self.error + self.ki * self.integral + self.kd * self.derivada
        if self.output > 100.0:
            self.output = 100
        elif self.output < 0:
            self.output = 0
        return self.output


class driverhardware(QObject):

    newdata = pyqtSignal()

    def __init__(self, mwindow):   
        super(). __init__()
        self.mwindow = mwindow
        self.Tsample = 1.0
        self.serial = serial.Serial(port=None,
                                    baudrate = 19200,
                                    parity=serial.PARITY_NONE,
                                    stopbits=serial.STOPBITS_ONE,
                                    bytesize=serial.EIGHTBITS,
                                    timeout=400)
        if self.serial.isOpen():
            self.serial.close()

        self.flagstop = False
        self.flagrunning = False
        self.starttime = None

        # Enable map: quais termopares e entradas devem ser lidas
        self.enablemap = [False,False,False,False,False,False,False,False,False,False]
        # Variáveis de controle:
        self.tipoctrl = "Off"
        self.termoparctrl = 0
        self.manuallevel = 0.0

        self.MAX_TIME = 360    # 360 minutos
        self.dman = dataman(360)

        self.dummymode = False
        self.dummytable = [b"\x06\x4F\x00",b"\x01\x90\x00",b"\x00\x01\x00",
                  b"\xFF\xFC\x00",b"\xFF\xF0\x00",b"\xF0\x60\x00",
                  b"\xF0\x60\x00",b"\x01\x90\x00"]  
        self.dummyjunta = b"\xE7\x00"

        self.pid = PID()

        self.timer = QTimer()
        self.flagsampletimeout = False
        self.timer.timeout.connect(self.sampletimeout)
        self.timer.start(1000)

        self.thread = QThread()                    
        self.moveToThread(self.thread)
        self.thread.started.connect(self.realizaLeituras)            
        self.thread.start()

        self.mutex = QMutex()
        self.condwait = QWaitCondition()

        
    def openSerial(self):
        self.serial.port = self.mwindow.ui.comboPorta.currentText()
        self.serial.open()


    def handshake(self):
        self.serial.reset_output_buffer()
        self.serial.reset_input_buffer()
        # Tenta fazer o handshake 2 vezes:
        for k in range(2):
            self.serial.write(b'h')
            if self.serial.read(1) == b'k':
                return True
            self.serial.reset_output_buffer()
            self.serial.reset_input_buffer()
            # time.sleep(0.1)
            QThread.msleep(100)
        raise Exception("Handshake com dispositivo falhou.")


    def writeThermType(self,tipo):
        cmd = f's{tipo}'[0:2].encode() # Comando para setar tipo de termopar.
        self.serial.write(cmd)
        # time.sleep(0.05)
        QThread.msleep(50)
        aux = self.serial.read(2)
        if aux.decode() != f'k{tipo}':
            print("Falhou!") # TODO: Raise exception!

    
    def writeManualCtrlLevel(self,level=None):
        if self.dummymode: 
            return
        if level is None: 
            convertedlevel = int(round(self.manuallevel))
        else:
            convertedlevel = int(round(level))
        cmd = [ord('m'), convertedlevel]
        self.serial.write(cmd)
        # TODO: get response from system to confirm.


    # def writeCtrlKs(self):
    #     if self.dummymode: 
    #         return
    #     self.serial.write(ord('j'))
    #     self.serial.write(struct.pack("<fff", self.ks[0], self.ks[1], self.ks[2])) # Kp, Ki, Kd
    #     # TODO: Ler confirmação.
    #     ''' 
    #         No lado do Arduino:
    #             Serial.readBytes((char *) &kp, sizeof(float));
    #             Serial.readBytes((char *) &ki, sizeof(float));
    #             Serial.readBytes((char *) &kd, sizeof(float));
    #         one kp, ki e kd devem ser variáveis definidas como floats: float kp, ki, kd.
    #         Fonte: https://stackoverflow.com/questions/59505221/sending-floats-as-bytes-over-serial-from-python-program-to-arduino
    #     '''


    def ctrlOff(self):
        if self.dummymode: 
            return
        # cmd = [ord('m'), 255]
        cmd = [ord('m'), 0]
        self.serial.write(cmd)
        # TODO: get response from system. 


    def iniciaLeituras(self,amostragem,enablemap,tipotermopar):
        if not self.flagrunning:
            try:
                if not self.dummymode:
                    self.openSerial()
                    # time.sleep(1.6)  # TODO: Check if this time can be reduced.
                    QThread.msleep(1500)
                    self.handshake()
                    # time.sleep(0.1)
                    QThread.msleep(100)
                    self.writeThermType(tipotermopar)
                self.flagrunning = True
                self.Tsample = float(amostragem) # TODO: What to do if user changes sampling rate without resetting data?
                self.enablemap = enablemap
                self.pid.reset()
                if self.starttime is None:
                    self.dman.resetData(amostragem)
                    self.starttime = int(round(time.time() * 1000) / 1000)
                # self.realizaLeituras()                
                self.flagstop = False
                self.flagrunning = True
                self.timer.setInterval(amostragem * 1000)
                
            except Exception as e:
                self.flagrunning = False
                if self.serial.isOpen():
                    self.serial.close()
                self.mwindow.errorStarting(str(e))

    def limpaLeituras(self):
        self.starttime = None
        self.dman.resetData(self.Tsample)


    def paraLeituras(self):
        if self.flagrunning:
            self.flagstop = True            


    def changeSetPoint(self,value):
        self.pid.setpoint = value


    def changeManualCtrlLevel(self,value):
        self.manuallevel = float(value)


    def changeCtrlType(self,tipo):
        self.tipoctrl = tipo


    def setCtrlConfig(self,tipo,termopar,kp,ki,kd):
        # print(tipo)
        self.tipoctrl = tipo
        self.termoparctrl = termopar
        self.pid.kp = kp
        self.pid.kd = kd
        self.pid.ki = ki


    def leTermopar(self,idx):
        if self.dummymode:
            # time.sleep(0.15)
            QThread.msleep(150)
            resp = self.dummytable[idx] + self.dummyjunta
        else:
            cmd = f'r{idx}'.encode() # Comando para leitura: uma string com r seguido do número (como string)
            self.serial.write(cmd)
            # time.sleep(0.15)
            QThread.msleep(150)
            resp = self.serial.read(5)  # Resposta sempre em 5 bytes: os 3 primeiros correspondem à leitura, os outros 2 à junta fria.
    
        if resp[0] == 0x80:
            if resp[2] == 0x00:
                text = "Aberto"
            elif resp[2] == 0x01:
                text = "OverUnder"
            elif resp[2] == 0x02:
                text = "IntOOR"
            elif resp[2] == 0x03:
                text = "ExtOOR"
            val = float("nan")
            juntafria = None
        else:           
            aux = int.from_bytes(resp[0:3],byteorder='big',signed=True)
            val = float(aux) / (2**12)
            aux = int.from_bytes(resp[3:5],byteorder='big',signed=True) 
            juntafria = float(aux) / (2**8)            
            text = f"{val:.2f} °C"
        return val,juntafria,text


    def sampletimeout(self):
        # if (self.flagrunning):
        #     self.flagsampletimeout = True
        # print(time.time())
        self.condwait.wakeAll()


    def realizaLeituras(self):

        while True: 

            if not self.flagrunning:
                
                QThread.sleep(1)

            else:

                if self.flagstop:  

                    self.ctrlOff()        
                    if self.serial.isOpen():                
                        self.serial.close()
                    self.flagrunning = False
                    self.flagstop = False

                else:

                    readtime = int(time.time()) - self.starttime
                    self.mwindow.setCurTime(readtime)

                    autotermopread = -1
                    junta = 0
                    
                    if (self.tipoctrl == 'Off'):
                        self.ctrlOff()
                        self.dman.setpoint = None
                        self.mwindow.setPowerText(f"0%")
                    elif (self.tipoctrl == 'Manual'):
                        self.writeManualCtrlLevel()
                        self.dman.setpoint = None
                        self.mwindow.setPowerText(f"{self.manuallevel:.0f}%")
                    elif (self.tipoctrl == 'Auto'):
                        self.dman.setpoint = self.pid.setpoint
                        val,juntaaux,text = self.leTermopar(self.termoparctrl)
                        if not math.isnan(val):
                            self.pid.update(val)
                            self.mwindow.setPowerText(f"{self.pid.output:.0f}%")
                            self.writeManualCtrlLevel(level=self.pid.output)
                        else: 
                            self.writeManualCtrlLevel(level=0)
                        rtimeaux = int(time.time()) - self.starttime
                        if juntaaux is not None:
                            junta = juntaaux
                        # val,junta,text = self.leTermoparADS(k)
                        self.mwindow.setValText(text,self.termoparctrl)
                        self.dman.appendTData(self.termoparctrl,rtimeaux,val)
                        autotermopread = self.termoparctrl

                    # axx = time.time()
                    for k in range(8):
                        if k == autotermopread:
                            pass
                        elif self.enablemap[k]:
                            val,juntaaux,text = self.leTermopar(k)
                            rtimeaux = int(time.time()) - self.starttime
                            if juntaaux is not None:
                                junta = juntaaux
                            # val,junta,text = self.leTermoparADS(k)
                            self.mwindow.setValText(text,k)
                            self.dman.appendTData(k,rtimeaux,val) 
                        else:
                            self.dman.appendEmptyData(k,readtime)
                    self.dman.incrementCtReadings()  
                    # print(time.time() - axx)             
                    self.mwindow.setJunta(f"{junta:.2f}  °C")

                    # TODO: Readings if auxiliary inputs:
                    # for k in range(8,10):
                    #     if self.enablemap[k]:
                    #         print(f"E{k-8}")

                    # self.mwindow.updatePlot()
                    # self.mwindow.updatePlot()
                    self.newdata.emit()

                    # QThread.sleep(1)
                    # while not self.flagsampletimeout:
                    #     QThread.msleep(100)
                    # self.flagsampletimeout = False
                    self.mutex.lock()
                    self.condwait.wait(self.mutex)
                    self.mutex.unlock()
                    # print(".")

        
        