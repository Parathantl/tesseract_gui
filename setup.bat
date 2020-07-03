
#!/bin/bash

# Execute Python EXE File
"./python.exe"

# Install Tesseract
"./tesseract.exe"

# Execute Ghost Script EXE file
"./gs.exe"

# Install Python PyPDF2 Module
pip install PyPDF2

# Add Environmental Variables
setx path "%localappdata%\Programs\Python\Python38-32\Scripts;C:\Program Files\Tesseract-OCR;%localappdata%\Programs\Python\Python38-32;%path%;"
