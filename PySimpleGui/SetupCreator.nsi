; This script shows how to make your applicaton uninstallable

;--------------------------------

; The name of the installer
Name "UninstallExample1"

; The file to write
OutFile "Tesseract_GUI.exe"

; The default installation directory
InstallDir $PROGRAMFILES\TesseractGUI\

; The text to prompt the user to enter a directory
DirText "This will install My Cool Program on your computer. Choose a directory"

;--------------------------------

; The stuff to install

Section -Prerequisites

  SetOutPath $INSTDIR\Prerequisites

  MessageBox MB_YESNO "Install Python?" /SD IDYES IDNO endPython
    File "py3.8.0.exe"
    ExecWait "$INSTDIR\Prerequisites\py3.8.0.exe"
  endPython:

  MessageBox MB_YESNO "Install GhostScript?" /SD IDYES IDNO endGS
    File "gs.exe"
    ExecWait "$INSTDIR\Prerequisites\gs.exe"
  endGS:

  MessageBox MB_YESNO "Install Tesseract?" /SD IDYES IDNO endTess
    File "tesseractsetup.exe"
    ExecWait "$INSTDIR\Prerequisites\tesseractsetup.exe"
  endTess:

  MessageBox MB_YESNO "Add Environment Variables?" /SD IDYES IDNO endENV
    ExecWait 'setx path "%path%;%localappdata%\Programs\Python\Python38-32\Scripts;C:\Program Files\Tesseract-OCR;%localappdata%\Programs\Python\Python38-32"'
  endENV:

  MessageBox MB_YESNO "Install PyPDF2?" /SD IDYES IDNO endPyPDF2
    ExecWait "pip install PyPDF2"
  endPypdf2:

SectionEnd

Section ""

; Set output path to the installation directory.
SetOutPath $INSTDIR

; Put a file there
File Tesseract_PySimpleGUI.exe

; Tell the compiler to write an uninstaller and to look for a "Uninstall" section
WriteUninstaller $INSTDIR\Uninstall.exe

SectionEnd

Section "Desktop Shortcut" SectionX
    SetShellVarContext current
    CreateShortCut "$DESKTOP\Tesseract_PySimpleGUI.lnk" "$INSTDIR\Tesseract_PySimpleGUI.exe"
SectionEnd

;-------------------

; The uninstall section
Section "Uninstall"

Delete $INSTDIR\Uninstall_Tesseract_GUIl.exe
Delete $INSTDIR\Tesseract_GUI.exe
RMDir $INSTDIR

SectionEnd