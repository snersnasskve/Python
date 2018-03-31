import RPi.GPIO as GPIO

#   This is not an infinite loop - it's just once each way
GPIO.setmode(GIO.BOARD)
#   Only pin 12 and one other does pulse.width.modulation
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 50)
# Duty cycle = 0
pwm.start(0)
#   Iterate through duty cycle 0 to 100
#   99 = 180 degree turn
foreach i in range(100):
    pwm.ChangeDutyCycle(i)
    time.sleep(0.1)
foreach i in range(100, 0, -1):
    pwm.ChangeDutyCycle(i)
    time.sleep(0.1)