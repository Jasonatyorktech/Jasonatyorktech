# Jason Quinn
#Four Buttions, One LED
import RPi.GPIO as GPIO
GPIO.setwarning(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10,GPIO.IN,pull_up_down=GPIO.PUD_UP)
LEDlit=False
while true:
    if GPIO.input(10)==GPio.HIGH:
        print("Button was pushed!")
        if LEDlit=True:
            LEDlit= False

