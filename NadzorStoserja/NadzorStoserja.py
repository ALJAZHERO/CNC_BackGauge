
from ast import Delete
import glob
from hmac import new
from tkinter import *
from time import sleep
#import RPi.GPIO as GPIO #izkomenteraj ko laufa na RaspberryPi 


root = Tk()
root.title("CNC Stoser")

xpadframe=0
xpadbutton=10
xpadnums=15
xpadsymbols=15
ypadbutton=10

calframe= LabelFrame(root, text="Calculator", padx= xpadframe, pady=20)
calframe.grid(row=0, column=0, padx=5, pady=10)

controlframe=LabelFrame(root, text= "Stoser", padx= xpadframe, pady=20 )
controlframe.grid(row=0, column=1, sticky= N, padx= 5, pady=10)


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


cal = Entry(calframe, width=10, borderwidth=5)
cal.grid(row=0, column=0, columnspan=3, padx=0, pady=10)

control = Entry(controlframe, width=10, borderwidth=5)
control.grid(row=0, column=0, columnspan=2, padx=0, pady=10)
control.insert(0, 0)
 
C_control_position =Label (controlframe, text = "Trenutni popozaj = ", font=("Arial", 12))
C_control_position.grid (row=3, column=0)

Current_control_position = Entry(controlframe, width=7, borderwidth=2)
Current_control_position.grid(row=3, column=1)
Current_control_position.insert(0,0)


#Funkcija notepada
def button_click(number):
    current = cal.get()
    cal.delete(0, END)
    cal.insert(0, str(current) + str(number))

def button_clear():
    cal.delete(0, END)

def button_add():
    first_number = cal.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    cal.delete(0, END)

def button_equal():
    second_number = cal.get()
    cal.delete(0, END)
    
    if math == "addition":
        cal.insert(0, f_num + float(second_number))

    if math == "subtraction":
        cal.insert(0, f_num - float(second_number))

    if math == "multiplication":
        cal.insert(0, f_num * float(second_number))

    if math == "division":
        cal.insert(0, f_num / float(second_number))

    

def button_subtract():
    first_number = cal.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    cal.delete(0, END)

def button_multiply():
    first_number = cal.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    cal.delete(0, END)

def button_divide():
    first_number = cal.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    cal.delete(0, END)




#Funkcija premikanja
def motor():
    #zaèetne spremenljivke
    global Current_control_position
    Startposition= Current_control_position.get()
    new_position = float(control.get())
    
    #nastavitev pinov
    control.delete(0, END)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(PUL, GPIO.OUT)
    GPIO.setup(limit_MIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(limit_MAX, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(estop,GPIO.IN)

    if float(Startposition) < float(new_position) :
        dis_to_move= float(new_position) - float(Startposition)
        move_steps = int(steps_mm * float(dis_to_move))
        
        for steps in range(move_steps):
            
            if GPIO.input(limit_MAX) == True:
                Current_control_position.delete(0, END)
                Current_control_position.insert(0, str(MAX_disp))
                break
            GPIO.output(DIR, CW)
            GPIO.output(PUL, GPIO.HIGH)
            sleep(m_delay)
            GPIO.output(PUL, GPIO.LOW)
            sleep(m_delay)
            Current_control_position.delete(0,END)
            Current_control_position.insert(0, str(new_position))
            
    elif float(Startposition) > float(new_position):
        dis_to_move = float(Startposition) - float(new_position)
        move_steps = int(float(steps_mm * dis_to_move))
        
        for steps in range(move_steps):
            if GPIO.input(limit_MIN)==True:
                Current_control_position.delete(0,END)
                Current_control_position.insert(0,str(MIN_disp))
                break
            GPIO.output(DIR, CCW)
            GPIO.output(PUL, GPIO.HIGH)
            sleep(m_delay)
            GPIO.output(PUL, GPIO.HIGH)
            sleep(m_delay)
            Current_control_position.delete(0,END)
            Current_control_position.insert(0, str(new_position))
            
    elif Startposition == new_position:
        return
         
    GPIO.cleanup()
        
        



                                        
        

            
            
        
   
        




button_1 = Button(calframe, text="1", padx=xpadnums, pady=ypadbutton, command=lambda: button_click(1))
button_2 = Button(calframe, text="2", padx=xpadnums, pady=ypadbutton, command=lambda: button_click(2))
button_3 = Button(calframe, text="3", padx=xpadnums, pady=ypadbutton, command=lambda: button_click(3))
button_4 = Button(calframe, text="4", padx=xpadnums, pady=ypadbutton, command=lambda: button_click(4))
button_5 = Button(calframe, text="5", padx=xpadnums, pady=ypadbutton, command=lambda: button_click(5))
button_6 = Button(calframe, text="6", padx=xpadnums, pady=ypadbutton, command=lambda: button_click(6))
button_7 = Button(calframe, text="7", padx=xpadnums, pady=ypadbutton, command=lambda: button_click(7))
button_8 = Button(calframe, text="8", padx=xpadnums, pady=ypadbutton, command=lambda: button_click(8))
button_9 = Button(calframe, text="9", padx=xpadnums, pady=ypadbutton, command=lambda: button_click(9))
button_0 = Button(calframe, text="0", padx=xpadnums, pady=ypadbutton, command=lambda: button_click(0))
button_decimal = Button(calframe, text=".", padx=xpadbutton, pady=ypadbutton, command=lambda: button_click("."))
button_add = Button(calframe, text="+", padx=xpadsymbols, pady=ypadbutton, command=button_add)
button_equal = Button(calframe, text="=", padx=30, pady=ypadbutton, command=button_equal)
button_clear = Button(calframe, text="Clear", padx=20, pady=ypadbutton, command=button_clear)
button_subtract = Button(calframe, text="-", padx=xpadsymbols, pady=ypadbutton, command=button_subtract)
button_multiply = Button(calframe, text="*", padx=xpadsymbols, pady=ypadbutton, command=button_multiply)
button_divide = Button(calframe, text="/", padx=xpadsymbols, pady=ypadbutton, command=button_divide)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)
button_decimal.grid(row=6, column=3)


root.mainloop()