# Names: Emmanuel Francis
# Student Number: FRNEMM004
# Prac: Prac 1
# Date: 30/07/2019


# import Relevant Librares
import RPi.GPIO as GPIO
import time
import itertools

makeList = list(itertools.product(range(2), repeat=3)) #List of outputs created
pinOutput_list =[11,12,13] #Output pins list
pinInput_list=[35,36] #Input pins list
currentVal =0 #CurrentVal Initiated. Used later in functions as a count

#Use BOARD numbering sytem
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinOutput_list, GPIO.OUT)
GPIO.setup(pinInput_list, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def ledSwitch():             #Swicthes a single LED on and off
    	GPIO.output(11,GPIO.HIGH)
    	time.sleep(1)
    	GPIO.output(11, GPIO.LOW)
    	time.sleep(1)

def buttonSubtract(button36): #When button36 is pressed subtract from value
    	print("subtracted")
    	global currentVal
    	if currentVal ==0:
        	currentVal =7
    	else:
        	currentVal-=1
    	GPIO.output(pinOutput_list, makeList[currentVal])

def buttonAdd(button35): #When button35 is pressed add to value
	print("add")
    	global currentVal
    	if currentVal ==7:
        	currentVal=0
    	else:
        	currentVal +=1
    	GPIO.output(pinOutput_list, makeList[currentVal])

#Interrupts to detect when a button has been pressed
GPIO.add_event_detect(35, GPIO.FALLING, callback=buttonAdd, bouncetime=300)
GPIO.add_event_detect(36, GPIO.FALLING, callback=buttonSubtract, bouncetime=300)

# Logic that you write
def main(): 
    	print("Bobo, write your logic here king")
	#ledSwitch()
	time.sleep(12)

# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
    	print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.output(pinOutput_list, GPIO.LOW)
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)


