
from PySide2.QtCore import QThread,Signal
import requests, zipfile, io

class Updater(QThread):

    updated = Signal(int)
    
    def run(self):
        zip_file_url = "https://github.com/eduardobatista/TCMonPy/archive/refs/heads/master.zip"  
        r = requests.get(zip_file_url, stream=True)
        self.updated.emit(30)
        QThread.msleep(1000)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        self.updated.emit(60)
        QThread.msleep(1000)
        print(z.namelist()) 
        self.updated.emit(100)
        pass