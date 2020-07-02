
#!/bin/bash

# Execute Python EXE File
"./python.exe"

# Execute Ghost Script EXE file
"./gs.exe"

# Install Tesseract
"./tesseract.exe"

# Install Python PyPDF2 Module
pip3 install PyPDF2

# Add Environmental Variables
setx path "%path%;%localappdata%\Programs\Python\Python38-32\Scripts;C:\Program Files (x86)\Tesseract-OCR;%localappdata%\Programs\Python\Python38-32;"