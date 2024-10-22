# Write your code here :-)
import time
import board
import digitalio
import pwmio

led = digitalio.DigitalInOut(board.D1) #was d13
led.switch_to_output

button = digitalio.DigitalInOut(board.BUTTON_A)
button.switch_to_input(pull=digitalio.Pull.DOWN)

while True:
    if button.value:
        led.value = True
    else:
        led.value = False
    time.sleep(0.1)

MAX_CYCLE = 2**16
led = pwmio.PWMOut(board.D1)
while True:
    for cycle in range(0, MAX_CYCLE):
        led.duty_cycle = cycle
    for cycle in range(MAX_CYCLE-1, 0, -1):
        led.duty_cycle = cycle
time.sleep(0.1)

#from analogio import AnalogOut
#led = AnalogOut(board.A0)
#keep 2 for button
#while True:
#   for cycle in range(0, MAX_CYCLE):
    # led.duty_cycle = cycle
#   for i in range(0, 65535,64): #no fade?
#       led.value = i
#       time.sleep(0.01)
#   for i in range(MAX_CYCLE-1,0,64): #no fade?
#       led.value = i
#       time.sleep(0.001) #bigger number or smaller?
