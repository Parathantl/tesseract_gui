import PySimpleGUI as sg
import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import subprocess

sg.theme('Light Blue 2')

layout = [[sg.Text('PDF to Text - Tesseract4 GUI')],
          [sg.Text('Enter the PDF File:', size=(12, 1)), sg.Input(), sg.FileBrowse()],
          [sg.Text('Enter the JPG FOLDER:', size=(12, 1)), sg.Input(), sg.FolderBrowse()],
          [sg.Text('Enter the Text FOLDER:', size=(12, 1)), sg.Input(), sg.FolderBrowse()],
          [sg.Text('GS File Path:', size=(12, 1)), sg.Input(), sg.FileBrowse()],
          [sg.Button("Start"), sg.Cancel()]]

window = sg.Window('Tesseract4 PDF to Text', layout)

current_path = os.path.dirname(os.path.abspath(__file__))

if not os.path.exists(current_path+'/singles'):
	os.mkdir(current_path+'/singles')

event, values = window.read()

path = values[0]

def pdf_splitter(path):
	pdf = PdfFileReader(path)
	for page in range(pdf.getNumPages()):
		pdf_writer = PdfFileWriter()
		pdf_writer.addPage(pdf.getPage(page))
		output_filename = single_pdf+'/'+'page_{}.pdf'.format(page+1)
		
		with open(output_filename, 'wb') as out:
			pdf_writer.write(out)
		print('Created: {}'.format(output_filename))

single_pdf = current_path+'/singles'
pdf_splitter(path)

jpg_folder = values[1]
text_folder = values[2]
gs_file_path = values[3]

print("JPG:",jpg_folder)
print("Text:",text_folder)

for root, dirs, file in os.walk(single_pdf):
	for files in file:
		name_file = os.path.splitext(files)[0]

		cmd = r'"'+values[3] + '" -q -DNOPAUSE -DBATCH -r300x300 -SDEVICE=jpeg -dSAFER -sOutputFile='+jpg_folder+'/'+name_file+'.jpg '+ '"'+root+'/'+files+'"'
		p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
		#print("Converting PDF to JPG: ",name_file)

for root, dirs, file in os.walk(single_pdf):
	for files in file:
		name_file = os.path.splitext(files)[0]

		cmd1 = 'tesseract '+jpg_folder+'/'+name_file+'.jpg '+text_folder+'/'+name_file+' -l eng+tam'
		q = subprocess.Popen(cmd1 , shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
		#print("Converting JPG to Text: ",name_file)

try:
	os.remove(single_pdf)
except:
	print("Error\n")

window.close()