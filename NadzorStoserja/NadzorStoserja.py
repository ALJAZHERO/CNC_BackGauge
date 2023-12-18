
from tkinter import *
from time import sleep
#import RPi.GPIO as GPIO #izkomenteraj ko laufa na RaspberryPi 


root = Tk()
root.title("CNC BackGuage")
'''
xpadframe=0
xpadbutton=10
xpadnums=15
xpadsymbols=15
ypadbutton=10

fenceframe=LabelFrame(root, text= "Fence", padx= xpadframe, pady=20 )
fenceframe.grid(row=0, column=1, sticky= N, padx= 5, pady=10)
'''

#pin setup
DIR = 000 #smer
PUL = 000 #pulzi za koraène motorje
MAX_disp= 2000 #prikaz vrednosti pri skrajnem desnem položaju
MIN_disp= 0 #prikaz vrednosti pri skrajnem levem položaju
CW = 0
CCW = 1

#senzorji
limit_MIN = 000
limit_MAX = 000
estop = 000 #ustavi vse gibe

#nastavitve motorja
RPM= 400
steps_rev = 400
m_deg= 0.9 #stopinje motorja 400 -> 0.9 200 -> 1.8
Dp_zobnik= 14 #Dp vrednost zobnika
m_delay = ((1/(RPM/60))/360) * m_deg
steps_mm = 9.0945

#Premikanje mororja

 '''  
fen = Entry(fenceframe, width=10, borderwidth=5)
fen.grid(row=0, column=0, columnspan=2, padx=0, pady=10)
fen.insert(0, 0)
 
C_fence_position =Label (fenceframe, text = "Current Position = ", font=("Arial", 12))
C_fence_position.grid (row=3, column=0)

Current_fence_position = Entry(fenceframe, width=7, borderwidth=2)
Current_fence_position.grid(row=3, column=1)
Current_fence_position.insert(0,0)
'''
 
root.mainloop()