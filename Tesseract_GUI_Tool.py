"""
Tesseract GUI

In this script, A simple GUI to execute 
Tesseract commands to convert PDF to 
Text file

Author: Parathan Thiyagalingam
Website: medium.com/@parathantl
Last edited: May 2020
"""

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from datetime import datetime
import subprocess
import time
from PyPDF2 import PdfFileReader, PdfFileWriter
import platform

class NewDialog(QtWidgets.QWidget):
  def __init__(self):
    super().__init__()
    self.title = 'About'
    self.left = 300
    self.top = 300
    self.width = 300
    self.height = 200

    self.setWindowTitle(self.title)
    self.setGeometry(self.left, self.top, self.width, self.height)

    self.name = QtWidgets.QLabel(self)
    self.name.setText('Created by: Parathan Thiyagalingam')
    self.name.setGeometry(QtCore.QRect(20, 40, 500, 30))

    self.email = QtWidgets.QLabel(self)
    self.email.setText('email: parathanlive123@gmail.com')
    self.email.setGeometry(QtCore.QRect(20, 60, 500, 30))

    self.gitLink = QtWidgets.QLabel(self)
    self.gitLink.setOpenExternalLinks(True)
    urlLink="<a href=\"https://github.com/Parathantl/tesseract_gui\">Github Repository</a>"
    self.gitLink.setText(urlLink)
    self.gitLink.setGeometry(QtCore.QRect(20, 90, 500, 20))

    self.license = QtWidgets.QLabel(self)
    self.license.setText('GNU General Public License v2.0')
    self.license.setGeometry(QtCore.QRect(20, 110, 500, 20))

class App(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Tesseract4 GUI Tool'
        self.left = 300
        self.top = 200
        self.width = 500
        self.height = 350
        self.initUI()
    
    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.textEdit = QtWidgets.QLineEdit(self)
        self.textEdit.move(20, 40)
        self.textEdit.setGeometry(QtCore.QRect(90, 40, 180, 20))

        # Browse File Button
        self.button = QtWidgets.QPushButton('Browse PDF', self)
        self.button.setToolTip('Select a PDF file to input')
        self.button.setGeometry(QtCore.QRect(280, 40, 140, 20)) 
        self.button.clicked.connect(self.browseFile)

        # Language Option
        self.Language = QtWidgets.QLabel(self)
        self.Language.setText('Type the Language code you want to do OCR:\nEg: Tamil and English - tam+eng')
        self.Language.setGeometry(QtCore.QRect(90, 70, 500, 50))

        self.line = QtWidgets.QLineEdit(self)
        self.line.move(20, 40)
        self.line.setGeometry(QtCore.QRect(90, 120, 180, 20))

        self.LanguageLink = QtWidgets.QLabel(self)
        self.LanguageLink.setOpenExternalLinks(True)
        urlLink="<a href=\"https://github.com/tesseract-ocr/tesseract/blob/master/doc/tesseract.1.asc#languages\">Click this link to see the available Languages for Tesseract</a>"
        self.LanguageLink.setText(urlLink)
        self.LanguageLink.setGeometry(QtCore.QRect(90, 150, 500, 20))

        # Start Button
        self.startB = QtWidgets.QPushButton('Start', self)
        self.startB.setGeometry(QtCore.QRect(120, 190, 120, 20))
        self.startB.clicked.connect(self.on_start_click)

        #Text Label
        self.labelA = QtWidgets.QLabel(self)
        self.labelA.setText('Click Browse PDF button to select a PDF')
        self.labelA.setGeometry(QtCore.QRect(70, 210, 400, 60))

        self.dlg = QtWidgets.QPushButton('About', self)
        self.dlg.setGeometry(QtCore.QRect(120, 280, 120, 20))
        self.dlg.clicked.connect(self.open_new_dialog)

        self.show()

    def open_new_dialog(self):
        self.nd = NewDialog()
        self.nd.show()

    @pyqtSlot()
    def browseFile(self):
        self.fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        self.textEdit.setText(self.fname[0])

    @pyqtSlot()
    def on_start_click(self):

        self.textboxValue = self.line.text()

        self.startB.setText('On Process..!')

        folder_name = os.path.dirname(self.fname[0])

        self.mydir = os.path.join(folder_name,datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))

        os.makedirs(self.mydir)
        os.makedirs(self.mydir+'/singlepdf')
        os.makedirs(self.mydir+'/jpg')
        os.makedirs(self.mydir+'/text')

        self.single_pdf = self.mydir+'/singlepdf'
        self.jpg_folder = self.mydir+'/jpg'
        self.text_folder = self.mydir+'/text'
        self.single_pdf = self.mydir+'/singlepdf'

        #calling PDF splitter to split
        self.pdf_splitter()
        self.convertpdfToJpg()
        self.convertJpgToText()
        
        self.labelA.setText('Completed. Please Visit the folder '+self.mydir)
        self.startB.setText('Start')

    def pdf_splitter(self):
        pdf = PdfFileReader(self.fname[0])
        
        for page in range(pdf.getNumPages()):
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(pdf.getPage(page))
            output_filename = self.single_pdf+'/'+'page_{}.pdf'.format(page+1)
            
            with open(output_filename, 'wb') as out:
                pdf_writer.write(out)

    def convertpdfToJpg(self):
        
        for root, dirs, file in os.walk(self.single_pdf):

            if (platform.system() == 'Linux' or platform.system() == 'Darwin'):
                for i, files in enumerate(file):

                    name_file = os.path.splitext(files)[0]
                    
                    cmd = r'gs -q -DNOPAUSE -DBATCH -r300x300 -SDEVICE=jpeg -dSAFER -sOutputFile='+self.jpg_folder+'/'+name_file+'.jpg '+ '"'+root+'/'+files+'"'               
            
                    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
                    p.communicate()

                    #line to change progress
                    QtWidgets.QApplication.processEvents() 

                    self.labelA.setText('Processing: '+str(i+1)+' of '+str(len(file)))
                    time.sleep(1)
                
            if (platform.system() == 'Windows'):
                
                for i, files in enumerate(file):
                    
                    name_file = os.path.splitext(files)[0]
                    
                    cmd = r'"C:\Program Files\gs\gs9.52\bin\gswin64c.exe" -q -DNOPAUSE -DBATCH -r300x300 -SDEVICE=jpeg -dSAFER -sOutputFile='+self.jpg_folder+'/'+name_file+'.jpg '+ '"'+root+'/'+files+'"'
                    
                    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
                    
                    p.communicate()

                    QtWidgets.QApplication.processEvents() 

                    #line to change progress
                    self.labelA.setText('Converting PDF to JPG: Page '+str(i+1)+' of '+str(len(file)))
                    time.sleep(1)
                    
    def convertJpgToText(self):
        
        for root, dirs, file in os.walk(self.single_pdf):

            for i, files in enumerate(file):
                name_file = os.path.splitext(files)[0]
                
                cmd1 = 'tesseract '+self.jpg_folder+'/'+name_file+'.jpg '+self.text_folder+'/'+name_file+' -l '+ self.textboxValue
                
                q = subprocess.Popen(cmd1 , shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
                
                q.communicate()

                QtWidgets.QApplication.processEvents() 

                #line to change progress
                self.labelA.setText('Converting JPG to Text: Page '+str(i+1)+' of '+str(len(file)))
                time.sleep(1)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())