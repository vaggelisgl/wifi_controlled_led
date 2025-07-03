from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

import socket
import time
HOST="192.168.2.8"  #input your arduino's address within your local network
PORT=12345
mysocket =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
mysocket.settimeout(5.0)
on=True
print("UDP Client started. Enter data")

#sry for lack of comments mainly testing git

app = QApplication([])
window= QMainWindow()
window.setWindowTitle('WELCOME to GUI world')
window.setGeometry(100,100,500,300)

widgetContainer=QWidget()
window.setCentralWidget(widgetContainer)
mainLayout =QVBoxLayout(widgetContainer)

label=QLabel("Welcome to my world")
label.setAlignment(Qt.AlignCenter)
label.setStyleSheet("font-size: 24px; color: blue; padding: 5px;")
label.setFixedHeight(50)
mainLayout.addWidget(label)


pushLayout=QHBoxLayout()
mainLayout.addLayout(pushLayout)

pushred = QPushButton("Blink RED")
pushred.setStyleSheet("background-color: red; color:white; font-size: 24; padding:5px;")
pushred.setFixedSize(150,50)

def pushredClicked():
    label.setText("Blink red")
    label.setStyleSheet("color:red; font-size: 34; padding:5px;")
    mydata='br'
    mydata=mydata+'\n'
    mydataEncode=mydata.encode()
    mysocket.sendto(mydataEncode,(HOST,PORT))
    print("Sent" ,mydata,"to HOST",HOST,PORT)
pushred.clicked.connect(pushredClicked)
pushLayout.addWidget(pushred)


pushgreen = QPushButton("Blink green")
pushgreen.setStyleSheet("background-color: green; color:white; font-size: 24; padding:10px;")
pushgreen.setFixedSize(150,50)

def pushgreenClicked():
    label.setText("Blink green")
    label.setStyleSheet("color:green; font-size: 34; padding:10px;")
    mydata='bg'
    mydata=mydata+'\n'
    mydataEncode=mydata.encode()
    mysocket.sendto(mydataEncode,(HOST,PORT))
    print("Sent" ,mydata,"to HOST",HOST,PORT)
pushgreen.clicked.connect(pushgreenClicked)
pushLayout.addWidget(pushgreen)


pushblue = QPushButton("Blink blue")
pushblue.setStyleSheet("background-color: blue; color:white; font-size: 24; padding:10px;")
pushblue.setFixedSize(150,50)

def pushblueClicked():
    label.setText("Blink blue")
    label.setStyleSheet("color:blue; font-size: 34; padding:10px;")
    mydata='bb'
    mydata=mydata+'\n'
    mydataEncode=mydata.encode()
    mysocket.sendto(mydataEncode,(HOST,PORT))
    print("Sent" ,mydata,"to HOST",HOST,PORT)
pushblue.clicked.connect(pushblueClicked)
pushLayout.addWidget(pushblue)

toggleButtonLayout=QHBoxLayout()
mainLayout.addLayout(toggleButtonLayout)

toggleButtonRED=QPushButton("TOGGLE RED")
toggleButtonRED.setCheckable(True)
toggleButtonRED.setStyleSheet("background-color: red; color:white; font-size: 24; padding:10px;")
toggleButtonRED.setFixedSize(150,50)

def ToggleRed(checked):
    if checked:
        label.setText("RED toggle ON")
        mydata='TonR'
        
    if not checked:
        label.setText("RED toggle OFF")
        mydata='ToffR'
    mydata=mydata+'\n'
    mydataEncode=mydata.encode()
    mysocket.sendto(mydataEncode,(HOST,PORT))
    label.setStyleSheet("color:red; font-size: 34; padding:10px;")
    print("Sent" ,mydata,"to HOST",HOST,PORT)

toggleButtonRED.toggled.connect(ToggleRed)
toggleButtonLayout.addWidget(toggleButtonRED)

toggleButtonGREEN=QPushButton("TOGGLE GREEN")
toggleButtonGREEN.setCheckable(True)
toggleButtonGREEN.setStyleSheet("background-color: green; color:white; font-size: 24; padding:10px;")
toggleButtonGREEN.setFixedSize(150,50)

def ToggleGreen(checked):
    if checked:
        label.setText("GREEN toggle ON")
        mydata='TonG'
    if not checked:
        label.setText("GREEN toggle OFF")
        mydata='ToffG'
    mydata=mydata+'\n'
    mydataEncode=mydata.encode()
    mysocket.sendto(mydataEncode,(HOST,PORT))
    label.setStyleSheet("color:green; font-size: 34; padding:10px;")
    print("Sent" ,mydata,"to HOST",HOST,PORT)
    
toggleButtonGREEN.toggled.connect(ToggleGreen)
toggleButtonLayout.addWidget(toggleButtonGREEN)

toggleButtonBLUE=QPushButton("TOGGLE BLUE")
toggleButtonBLUE.setCheckable(True)
toggleButtonBLUE.setStyleSheet("background-color: blue; color:white; font-size: 24; padding:10px;")
toggleButtonBLUE.setFixedSize(150,50)

def ToggleBlue(checked):
    if checked:
        label.setText("BLUE toggle ON")
        mydata='TonB'
    if not checked:
        label.setText("BLUE toggle OFF")
        mydata='ToffB'      
    mydata=mydata+'\n'
    mydataEncode=mydata.encode()
    mysocket.sendto(mydataEncode,(HOST,PORT))
    label.setStyleSheet("color:blue; font-size: 34; padding:10px;")
    print("Sent" ,mydata,"to HOST",HOST,PORT)
    
toggleButtonBLUE.toggled.connect(ToggleBlue)
toggleButtonLayout.addWidget(toggleButtonBLUE)

redSlider=QSlider(Qt.Horizontal)
redSlider.setMinimum(0)
redSlider.setMaximum(100)
redSlider.setStyleSheet("""
QSlider::groove:horizontal {background: lightpink; height:20px; border-radius:5px;}
QSlider::handle:horizontal {background: red; margin-top: -10px;  margin-bottom: -10px; height:40px; width: 20px; border-radius:5px;}                   
                        
                        """)
redSlider.setFixedHeight(50)
def updateRedSlider():
    label.setText("Red slider:"+str(redSlider.value()))
    label.setStyleSheet("font-size: 24px; color: red; padding:10;")
    redStrength=2**(8*redSlider.value()/100)-1

    mydata="redStrength:"+str(redStrength)
    mydata=mydata+"\n"
    mydataEncode=mydata.encode()
    mysocket.sendto(mydataEncode,(HOST,PORT))
    print("Sent to HOST",HOST,PORT,"DATA red strength",mydata,'\n')
    try:
      response,serveraddress=mysocket.recvfrom(1024)
      print(response)
      if(abs(redSlider.value()-float(response))>2 and on):
          blueStrength=2**(8*redSlider.value()/100)-1
          mydata="redStrength:"+str(redStrength)
          mydata=mydata+"\n"
          mydataEncode=mydata.encode()
          mysocket.sendto(mydataEncode,(HOST,PORT))
    except socket.timeout: print("no response in 5 sec")
    

redSlider.valueChanged.connect(updateRedSlider)
mainLayout.addWidget(redSlider)

greenSlider=QSlider(Qt.Horizontal)
greenSlider.setMinimum(0)
greenSlider.setMaximum(100)
greenSlider.setStyleSheet("""
QSlider::groove:horizontal {background: lightgreen; height:20px; border-radius:5px;}
QSlider::handle:horizontal {background: green; margin-top: -10px;  margin-bottom: -10px; height:40px; width: 20px; border-radius:5px;}                   
                        
                        """)
greenSlider.setFixedHeight(50)
def updateGreenSlider():
    label.setText("Green slider:"+str(greenSlider.value()))
    label.setStyleSheet("font-size: 24px; color: green; padding:10;")
    greenStrength=2**(8*greenSlider.value()/100)-1
    print("green Strength:", greenStrength)
    mydata="greenStrength:"+str(greenStrength)
    mydata=mydata+"\n"
    mydataEncode=mydata.encode()
    mysocket.sendto(mydataEncode,(HOST,PORT))
    try:
      response,serveraddress=mysocket.recvfrom(1024)
      print(response)
      if(abs(greenSlider.value()-float(response))>2 and on):
          greenStrength=2**(8*greenSlider.value()/100)-1
          mydata="greenStrength:"+str(greenStrength)
          mydata=mydata+"\n"
          mydataEncode=mydata.encode()
          mysocket.sendto(mydataEncode,(HOST,PORT))
    except socket.timeout: print("no response in 5 sec")

greenSlider.valueChanged.connect(updateGreenSlider)
mainLayout.addWidget(greenSlider)

blueSlider=QSlider(Qt.Horizontal)
blueSlider.setMinimum(0)
blueSlider.setMaximum(100)
blueSlider.setStyleSheet("""
QSlider::groove:horizontal {background: lightblue; height:20px; border-radius:5px;}
QSlider::handle:horizontal {background: blue; margin-top: -10px;  margin-bottom: -10px; height:40px; width: 20px; border-radius:5px;}                   
                        
                        """)
blueSlider.setFixedHeight(50)
def updateBlueSlider():
    label.setText("Blue slider:"+str(blueSlider.value()))
    label.setStyleSheet("font-size: 24px; color: blue; padding:10;")
    blueStrength=2**(8*blueSlider.value()/100)-1
    print("Blue Strength:", blueStrength)
    mydata="blueStrength:"+str(blueStrength)
    mydata=mydata+"\n"
    mydataEncode=mydata.encode()
    mysocket.sendto(mydataEncode,(HOST,PORT))
    try:
      response,serveraddress=mysocket.recvfrom(1024)
      print(response)
      if(abs(float(blueSlider.value())-float(response))>2 and on):
          blueStrength=2**(8*blueSlider.value()/100)-1
          mydata="blueStrength:"+str(blueStrength)
          mydata=mydata+"\n"
          mydataEncode=mydata.encode()
          mysocket.sendto(mydataEncode,(HOST,PORT))
    except socket.timeout: print("no response in 5 sec")
    


blueSlider.valueChanged.connect(updateBlueSlider)
mainLayout.addWidget(blueSlider)

mainLayout.addStretch()
window.show()

sys.exit(app.exec_())
