# tesseract_gui
Simple Python GUI's for Tesseract4 in Windows with EXE file

This is a very simple Graphical User Interface created in Python PyQT5 module to do Optical Character Recognition using Open-Source 
Tesseract4.OCR with Tesseract is available only in Command Line. To ease, the usability of Tesseract for normal users this simple tool 
will help.

# For Windows

Download the EXE file from [Release Repository](https://github.com/Parathantl/tesseract_gui/releases).

It is currently available for 64 bit only. Soon, this will be available to 32 bit too.
When executing the EXE you might face some security issues/ get blocked by Windows stating that you can't execute. So, may have to off 
the protection / anti-virus protection. You will be asked to install Python3, Ghostscript, Tesseract in the order respectively.
Just install them as it goes. While installing Tesseract please choose the Languages you want to do OCR. Then only the data will be 
downloaded to the PC and can do OCR.

# For Linux/Ubuntu

Clone this repository and run the **Tesseract_GUI_Tool.py**	file.
To run successully, you need to have Python, pip, Ghostscript and Tesseract needs to be installed.
Other that that, PyQT5 module needs to be installed.

To install PyQT5 run

```
pip install PyQT5
```

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

That's it...

**Happy OCR ing**
