
def update(duty):
##    pwm.ChangeDutyCycle(float(duty))
    print(duty)


from tkinter import *
master = Tk()

w = Scale(master, from_=0, to=100, orient=HORIZONTAL, command = update);
w.pack()

# command = specifies the callback fucntion when scale changes
