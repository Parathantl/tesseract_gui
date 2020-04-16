import PySimpleGUI as sg
import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import subprocess
import time
from datetime import datetime

def pdf_splitter(path):
	pdf = PdfFileReader(path)

	for page in range(pdf.getNumPages()):
		pdf_writer = PdfFileWriter()
		pdf_writer.addPage(pdf.getPage(page))
		output_filename = single_pdf+'/'+'page_{}.pdf'.format(page+1)
		
		with open(output_filename, 'wb') as out:
			pdf_writer.write(out)

def convertpdfToJpg(single_pdf):
    for root, dirs, file in os.walk(single_pdf):

        layout1 = [[sg.Text('Converting PDF to JPG')],[sg.ProgressBar(len(file), orientation='h', size=(20, 20), key='progressbar')],[sg.Cancel()]]
        window1 = sg.Window('Converting PDF to JPG', layout1)

        for i, files in enumerate(file):
            progress_bar1 = window1['progressbar']
            event1, values1 = window1.read(timeout=10)

            if event1 == 'Cancel'  or event1 is None:
                break

            name_file = os.path.splitext(files)[0]
            cmd = r'"C:\Program Files\gs\gs9.52\bin\gswin64c.exe" -q -DNOPAUSE -DBATCH -r300x300 -SDEVICE=jpeg -dSAFER -sOutputFile='+jpg_folder+'/'+name_file+'.jpg '+ '"'+root+'/'+files+'"'
            p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)

            progress_bar1.UpdateBar(i + 1)
            time.sleep(1)

        window1.close()

def convertJpgToText(single_pdf):
    for root, dirs, file in os.walk(single_pdf):
        layout2 = [[sg.Text('Converting JPG to Text')],[sg.ProgressBar(len(file), orientation='h', size=(20, 20), key='progressbar')],[sg.Cancel()]]
        window2 = sg.Window('Converting JPG to Text', layout2)

        for i, files in enumerate(file):
            progress_bar2 = window2['progressbar']
            event2, values2 = window2.read(timeout=10)

            if event2 == 'Cancel'  or event2 is None:
                break

            name_file = os.path.splitext(files)[0]
            cmd1 = 'tesseract '+jpg_folder+'/'+name_file+'.jpg '+text_folder+'/'+name_file+' -l tam+eng'
            q = subprocess.Popen(cmd1 , shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)

            progress_bar2.UpdateBar(i + 1)
            time.sleep(1)

    window2.close()

tab2_layout = [[sg.T('Creator: Parathan')],[sg.T('License: GNU General Public License v2.0')],[sg.T('email: parathanlive123@gmail.com')]]

tab1_layout = [[sg.T('PDF to Text - Tesseract4 GUI')],
               [sg.T('Enter the PDF File:', size=(16, 1)), sg.Input(), sg.FileBrowse()],
               [sg.Button("Start"), sg.Cancel()]]

layout = [[sg.TabGroup([[sg.Tab('Home', tab1_layout), sg.Tab('About', tab2_layout)]])]]

#[sg.Text('Enter the ISO 639-3 code of the language you want: '),sg.InputText()],

window = sg.Window('Tesseract4 PDF to Text', layout)

event, values = window.read()

folder_name = os.path.dirname(values[0])

mydir = os.path.join(folder_name,datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))

os.mkdir(mydir)
os.mkdir(mydir+'/singlepdf')
os.mkdir(mydir+'/jpg')
os.mkdir(mydir+'/text')

single_pdf = mydir+'/singlepdf'
pdf_splitter(values[0])

jpg_folder = mydir+'/jpg'
text_folder = mydir+'/text'

convertpdfToJpg(single_pdf)

convertJpgToText(single_pdf)

if event == 'Cancel' or event is None:
    window.close()