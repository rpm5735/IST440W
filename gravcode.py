from m5stack import *
from m5ui import *
from uiflow import *
lcd.setRotation(3)
import time
import machine
import unit

setScreenColor(0x222222)
weigh0 = unit.get(unit.WEIGHT, unit.PORTC)


targetWeight = None


label0 = M5TextBox(146, 149, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)
title0 = M5Title(title="Gravity Puzzle", x=100, fgcolor=0xFFFFFF, bgcolor=0x494997)
label1 = M5TextBox(38, 30, "Find the correct combinations of rocks ", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label2 = M5TextBox(38, 57, "to determine if the gravitational force ", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label3 = M5TextBox(60, 83, "is consistant with Earth's moon. ", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label4 = M5TextBox(143, 193, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)



def buttonA_wasPressed():
  global targetWeight
  targetWeight = 500
  setScreenColor(0x666666)
  wait_ms(100)
  weigh0.zero()
  wait_ms(1)
  timerSch.run('timer1', 500, 0x00)
  timerSch.run('timer2', 100, 0x00)
  pass
btnA.wasPressed(buttonA_wasPressed)

@timerSch.event('timer1')
def ttimer1():
  global targetWeight
  lcd.font(lcd.FONT_DejaVu56)
  lcd.print((weigh0.weight), 100, 100, 0xffffff)
  if (weigh0.weight) > 121:
    lcd.font(lcd.FONT_DejaVu40)
    lcd.print('get less weight', 0, 0, 0xff0000)
    wait(1)
    lcd.clear()
  if (weigh0.weight) < 90:
    lcd.font(lcd.FONT_DejaVu24)
    lcd.print('get more weight', 0, 0, 0xffff00)
    wait_ms(1000)
    lcd.clear()
  else:
    pass
  if (weigh0.weight) > 90 and (weigh0.weight) < 120:
    lcd.font(lcd.FONT_DejaVu40)
    lcd.print('Congratulation!!!', 0, 0, 0x33ff33)
    wait_ms(1000)
    lcd.clear()
  pass

@timerSch.event('timer2')
def ttimer2():
  global targetWeight
  pass


lcd.clear()
lcd.font(lcd.FONT_DejaVu18)
lcd.print('Find the correct combination of', 0, 0, 0xffffff)
lcd.print(' rocks to determine if the ', 0, 20, 0xffffff)
lcd.print(" gravitational force is consistent with Earth's moon.", 0, 40, 0xffffff)
lcd.print('Please press the first button to play', 0, 180, 0xffffff)
pin0 = machine.Pin(1, mode=machine.Pin.OUT, pull=0x00)
pin0.on()
