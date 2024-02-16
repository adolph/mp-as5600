from time import sleep
from math import trunc
from machine import SoftI2C
from ssd1306 import SSD1306_I2C
from as5600 import AS5600
import servo

i2c = SoftI2C(sda=9,scl=8)

dsp = SSD1306_I2C(128,64,i2c)
height = 30

mag = AS5600(i2c)

svo = servo.Servo(0)

def makeAvg(inList):
  sum=0
  count = 0
  for itm in inList:
    count+=1
    sum+=itm
  return (sum/count)

def ctrUpdate(ctr=0,dir=1,max=10,lineStr=""):

  figure = "-"

  if dir == 1:
    ctr+=1
  else:
    ctr-=1

  if ctr > max:
    ctr = max - 1
    dir = 0
  if ctr < 0:
    ctr = 1
    dir = 1
  
  if dir == 1:
    lineStr = figure * ctr
  else:
    lineStr = (" " * (max - ctr) ) + ( figure * ctr )

  return (ctr,dir,max,lineStr)

ctr = 0
dir = 1
max = 15
lineStr = ""

angle = 0
angleNew = 0
angles = []

msg = ""

while True:
  msg = ""
  try:
    angleNew = trunc(mag.readAngle())
    angle = angleNew
    angles.append(angle)
    if len(angles) > 10:
      angles.pop(0)
  except:
    msg = "Cannot read mag. "
    pass

  try:
    svo.move(makeAvg(angles)/2)
  except ZeroDivisionError:
    svo.move(0)
  except:
    msg = msg + "Cannot move servo."
  
  (ctr,dir,max,lineStr) = ctrUpdate(ctr,dir,max,lineStr)

  dsp.fill(0)
  dsp.text("Angle: "+str(angle),10,height)
  dsp.text(lineStr,10,0)
  if msg != "":
    dsp.text(msg,10,height+20)
  dsp.show()

  sleep(.25)
