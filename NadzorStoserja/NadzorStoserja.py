
from tkinter import *
from time import sleep
import numpy
import RPi.GPIO as GPIO


root = Tk()
root.title("Nadzor žage")

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

def move_motor():
    

 
root.mainloop()