# tesseract_gui
Simple Python GUI Tool for Tesseract4

This is a very simple Graphical User Interface created in Python PyQT5 module to do Optical Character Recognition using Open-Source 
Tesseract4. OCR with Tesseract is available only in Command Line. To ease, the usability of Tesseract for normal users this simple tool 
will help.

# For Windows

Download the EXE file from [Release Repository](https://github.com/Parathantl/tesseract_gui/releases).

It is currently available for 64 bit only. Soon, this will be available to 32 bit too.

Download the ZIP file from the Release Repository.
Click the setup.bat file
A Command-Line will be opened and asks you to install Python, Tesseract and GhostScript in the respective order.
While setting up Tesseract don not forget to select the languages you are going to use to do OCR.

That's it. You are all done.!!

# For Linux/Ubuntu

Clone this repository

CHANGE YOUR DIRECTORY into this repo
Run the following command inside the folder

```
chmod +x setup.sh
````
This will download you all the necessary modules to do OCR.
While installing the Language set to be downloaded for Tesseract is Tamil.
If you want any other languages, just change the tam with your language you want to do OCR.

Then run the **Tesseract_GUI_Tool.py**	file.

# How to Use

When yo open the tool, you can browse the PDF file through a File browser and select the PDF you want to OCR.
Type the languages your PDF file has. So that, OCR can use those languages and find the characters.
If you don't know which languages Tesseract is available or the language code you don't know. You can find a link to get the languages
Tesseract is available.
Just find out it and input the languages.

Then click **Start**

In the directory path of the selected PDF, you  can see a folder is created with TimeStamp(YY-MM-DD) inside the folder you can 
see 3 folders.
1. single_pdf: Contains all the pages of PDF as a seperate PDF files
2. jpeg: every single PDF will be in JPEG format
3. text: every single pages will be in a Text document

Finally inside the folder, a Single Text file will be created

That's it...

**Happy OCR ing**
