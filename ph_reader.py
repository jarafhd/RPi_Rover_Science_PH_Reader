import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

pad_1=
pad_2=
pad_3=
pad_4=
pad_5=
pad_6=
pad_7=
pad_8=
pwr_btn=
mode_btn=
pd_1=0
pd_2=0
pd_3=0
pd_4=0
pd_5=0
pd_6=0
pd_7=0
pd_8=0

GPIO.setup(pad_1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pad_2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pad_3,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pad_4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pad_5,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pad_6,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pad_7,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pad_8,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pwr_btn,GPIO.OUT)
GPIO.setup(mode_btn,GPIO.OUT)

While TRUE:
  if GPIO.input(pad_1)==1:
    pd_1=1
    sleep(.1)
  if GPIO.input(pad_2)==1:
    pd_2=1
    sleep(.1)
  if GPIO.input(pad_3)==1:
    pd_3=1
    sleep(.1)    
  if GPIO.input(pad_4)==1:
    pd_4=1
    sleep(.1)            
  if GPIO.input(pad_5)==1:
    pd_5=1
    sleep(.1)
  if GPIO.input(pad_6)==1:
    pd_6=1
    sleep(.1)
  if GPIO.input(pad_7)==1:
    pd_7=1
    sleep(.1)    
  if GPIO.input(pad_8)==1:
    pd_8=1
    sleep(.1)    
    
 
