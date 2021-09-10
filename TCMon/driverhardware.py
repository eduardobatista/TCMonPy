import serial
import time
import threading
import struct

from .dataman import dataman

class driverhardware:

    def __init__(self, mwindow):        
        self.mwindow = mwindow
        self.Tsample = 2.0    
        self.serial = serial.Serial(port=None,
                                    baudrate = 19200,
                                    parity=serial.PARITY_NONE,
                                    stopbits=serial.STOPBITS_ONE,
                                    bytesize=serial.EIGHTBITS,
                                    timeout=400)
        if self.serial.isOpen():
            self.serial.close()
        self.flagrunning = False
        self.starttime = 0

        # Enable map: quais termopares e entradas devem ser lidas
        self.enablemap = [False,False,False,False,False,False,False,False,False,False]
        # Variáveis de controle:
        self.tipoctrl = "Off"
        self.termoparctrl = 0
        self.ks = [1.0,0.0,0.0]
        self.manuallevel = 0.0
        self.setpoint = 0.0

        self.MAX_TIME = 360    # 360 minutos
        self.dman = dataman(360)

        self.dummymode = False
        self.dummytable = [b"\x06\x4F\x00",b"\x01\x90\x00",b"\x00\x01\x00",
                  b"\xFF\xFC\x00",b"\xFF\xF0\x00",b"\xF0\x60\x00",
                  b"\xF0\x60\x00",b"\x01\x90\x00"]  
        self.dummyjunta = b"\xE7\x00"

    

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
                # time.sleep(0.1)
                return True
            self.serial.reset_output_buffer()
            self.serial.reset_input_buffer()
            time.sleep(0.1)
        raise Exception("Handshake com dispositivo falhou.")

    def writeThermType(self,tipo):
        cmd = f's{tipo}'[0:2].encode() # Comando para setar tipo de termopar.
        self.serial.write(cmd)
        time.sleep(0.05)
        # TODO: Ler um "ok" como resposta.
    
    def writeManualCtrlLevel(self):
        convertedlevel = 255 - int(255.0*self.manuallevel/100.0) # Adaptando considerando que 100% = 0 e 0% = 255  
        cmd = [ord('m'), convertedlevel]
        self.serial.write(cmd)

    def ctrlOff(self):
        if self.tipoctrl == "Manual":
            cmd = [ord('m'), 255]
            self.serial.write(cmd)


    def iniciaLeituras(self,amostragem,enablemap,tipotermopar):
        if not self.flagrunning:
            try:
                self.dman.resetData(amostragem)
                if not self.dummymode:
                    self.openSerial()
                    time.sleep(1.6)
                    self.handshake()
                    time.sleep(0.1)
                    self.writeThermType(tipotermopar)
                    # TODO: grava configurações controle (ks e tipo)
                self.flagrunning = True
                self.Tsample = float(amostragem)
                self.enablemap = enablemap
                self.starttime = int(round(time.time() * 1000) / 1000)
                self.realizaLeituras()
            except Exception as e:
                self.flagrunning = False
                if self.serial.isOpen():
                    self.serial.close()
                self.mwindow.errorStarting(str(e))
    
    def paraLeituras(self):
        if self.flagrunning:
            self.flagrunning = False


    def changeSetPoint(self,value):
        self.setpoint = value
        # print(value)

    def changeManualCtrlLevel(self,value):
        self.manuallevel = float(value)
        # print(value)

    def setCtrlConfig(self,tipo,termopar,kp,ki,kd):
        # print(tipo)
        self.tipoctrl = tipo
        self.termoparctrl = termopar+1
        self.ks = [kp,ki,kd]
                 
    def leTermopar(self,idx):
        if self.dummymode:
            # return 10.0+idx,21.0,f"{10.0+idx} °C"
            time.sleep(0.15)
            resp = self.dummytable[idx] + self.dummyjunta
        else:
            cmd = f'r{idx+1}'.encode() # Comando para leitura: uma string com r seguido do número (como string)
            self.serial.write(cmd)
            time.sleep(0.15)
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
            val = 0.0
            juntafria = 0.0
        else:           
            aux = int.from_bytes(resp[0:3],byteorder='big',signed=True)
            val = float(aux) / (2**12)
            aux = int.from_bytes(resp[3:5],byteorder='big',signed=True) 
            juntafria = float(aux) / (2**8)            
            text = f"{val:.2f} °C"
        return val,juntafria,text


    def realizaLeituras(self):
        if not self.flagrunning:
            return
        threading.Timer(self.Tsample, self.realizaLeituras).start()    
        if (self.tipoctrl == 'Manual') and (not self.dummymode):
            self.writeManualCtrlLevel()
        readtime = int(time.time()) - self.starttime
        self.mwindow.setCurTime(readtime)
        junta = 0
        for k in range(8):
            if self.enablemap[k]:
                val,junta,text = self.leTermopar(k)
                self.mwindow.setValText(text,k)
                self.dman.appendTData(k,readtime,val)
        self.mwindow.setJunta(f"{junta:.2f}  °C")
        for k in range(8,10):
            if self.enablemap[k]:
                print(f"E{k-8}")
        self.mwindow.updatePlot()
        
        