#####-----Imports-----######
import xbee #Allows communicating with the Xbee board
import machine #Allows access to pin definitions
from machine import Pin
import time #Use board clock for timing

#####-----Pins----#####
# Use this space to declare all pins in and out of the device
#D0 -> DIO0
#D1 -> DIO1
#D2 -> DIO2
#D3 -> DIO3
#D4 -> DIO4

Output0 = Pin(machine.Pin.board.D0, Pin.OUT)
Output0.value(1)
Output1 = Pin(machine.Pin.board.D1, Pin.OUT)
Output1.value(1)
Output2 = Pin(machine.Pin.board.D2, Pin.OUT)
Output2.value(1)



#####-----Global Variables-----#####
# Use this space to house all GLOBAL Variables
name = '[ROUTER NAME]' #Name to be sent along with all messages for datalogging purposes
State = 0 #Used to store the current state of iridium input to reduce network message load

#####-----'Back end' Methods-----#####
# Space for code that is specifically used to send and recieve messages from
# other parts of the network. Do not modify this code without backing up data
# and ensuring that you know what you are doing


#Method used to get a message from the network. Runs every iteration of the main loop
# Do not modify without cause
def getMessage():
    message = xbee.receive()
    if message:
        #print(message) # Debug print only seen in console
        return eval(message.get('payload').decode('utf-8'))

# Method to send an exact string to the entire network. Includes error
# handling for too many consecutive messages
# Do not modify OR call without cause
def sendExactMessage(message = ''):
    try:
        xbee.transmit(xbee.ADDR_BROADCAST, message)
    except OSError as e:
        print('OS error: {0}'.format(e.args))
        time.sleep(0.3)
        sendExactMessage(message)

# Method to send a message out to the entire network after formatting
# Messages must be in the format of "{'KEY1':'ITEM1','KEY2',ITEM2',...}"
# Do not modify without cause
def sendMessage(message = ''):
    message = "{'from':'" + name + "','msg':'" + message + "'}"
    sendExactMessage(message)





#####-----SPACE FOR GENERAL USERS-----#####
# Space for User to define all needed methods and use the provided methods to
# call them for use when timing permits it. All code developed by users and not
# directly pertaining to the operation of the XBee itself should be put here


# Method to allow router to complete tasks, limited to every second to save
# processing power
# DO NOT INCLUDE PYTHON CODE IN MESSAGES
def proactiveSpace():
#    sendMessage("{'temp':'25','vel':'32'}") # Example of how to send data that can be proccessed on other routers in the network
    pass #Satisfies python requirement for funciton to do something
    #print('Proactive Space') # Debug print

# Method to allow router reactions to incoming messages, activates every time a
# message is recieved
def reactiveSpace(message):
# Example of how to process incoming messages within the reactive space
    if(message.get('from') == '[COORDINATOR NAME]'): # Check where the message is coming from
         message = message.get('msg') # Strip the sender and just use the actual message
         message = dict(message) # Convert the message into a dictionary for easier processing
         if(message.get('Command')): # Check if the information you want is avilible in the message
            if message.get('Command') != State: #If the iridium command is different than the current stored state, then pass the new state to the active funciton
                outputState(int(message.get('Command')))


    print(message) # Debug print

#Process the current state of Iridium inputs and map them to a LED set based on binary breakdown
def outputState(newState):
    #Declare intent to modify glocal variable "State" and update it to the new State
    global State
    State = newState

    #Breakdown the numer back into it's binary compnents and display on LEDs
    if(newState/4 >= 1):
        newState = newState % 4
        Output2.value(1)
        print("Turning on LED 3 (Blue), Remaining value", newState) # Debug print
    else:
        Output2.value(0)
    if (newState / 2 >= 1):
        newState = newState % 2
        Output1.value(1)
        print("Turning on LED 2 (Green), Remaining value", newState) # Debug print
    else:
        Output1.value(0)
    if (newState / 1 >= 1):
        newState = newState % 1
        Output0.value(1)
        print("Turning on LED 1 (Red), Remaining value", newState) # Debug print
    else:
        Output0.value(0)









#####-----Connect To Network-----#####
# Code to allow the Xbee to connect to the Coordinator at the head of the
# network Do not modify this code without backing up data and ensuring that you
# know what you are doing

print("Waiting for XBee to join network...")
while xbee.atcmd('AI') != 0:
    time.sleep(0.1)
print(name, " joined network.")
sendMessage('Joined network')


#####-----Main Loop-----#####
# The main code to be run on the device. This loop includes specific timings
# to ensure device does not crash due to overflows or extra usage. Do not
# modify this code without backing up data and ensuring that you know what you
# are doing

iterations = 0
while True:
    # Check if connected to the Network
    if xbee.atcmd('AI') == 0:

        #Check for a new message in the stack
        message = getMessage()

        #If there is a new message react to it
        if message:
            reactiveSpace(message) # Call the user defined method

        # Every 5 Iteration(s) complete actions in proactive space and reset the
        # Iterations counter to zero
        if iterations % 5 == 0:
            proactiveSpace()
            iterations = 0

        #Slight buffer to save resources
        time.sleep(0.2)
        iterations += 1


