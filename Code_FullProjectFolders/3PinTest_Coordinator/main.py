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

#Example of how to use Pin's to read from Iridium
Iridium0 = Pin(machine.Pin.board.D0, Pin.IN, Pin.PULL_DOWN)
Iridium1 = Pin(machine.Pin.board.D1, Pin.IN, Pin.PULL_DOWN)
Iridium2 = Pin(machine.Pin.board.D2, Pin.IN, Pin.PULL_DOWN)





#####-----Global Variables-----#####
# Use this space to house all GLOBAL Variables
name = '[COORDINATOR NAME]' #Name to be sent along with all messages for datalogging purposes
State = 0 #Used to store the current state of iridium input to reduce network message load

#####-----'Back end' Methods-----#####
# Space for code that is specifically used to send and recieve messages from
# other parts of the network. Do not modify this code without backing up data
# and ensuring that you know what you are doing


# Method used to get a message from the network. Runs every iteration of the main loop
# Do not modify without cause
def getMessage():
    message = xbee.receive()
    if message:
        print(message) # Debug print only seen in console
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
# Do not modify without cause
def sendMessage(message = ''):
    message = "{'from':'" + name + "','msg':" + message + "}"
    print(message)  # Debug print
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


    print(Iridium0.value(), Iridium1.value(), Iridium2.value()) # Debug print
    readIridium() #Read the current values of the Iridium Inputs and determine if they have changed, if so then send a message to the network

# Method to allow router reactions to incoming messages, activates every time a
# message is recieved
def reactiveSpace(message):
# Example of how to process incoming messages within the reactive space
#    if(message.get('from') == '[COORDINATOR NAME]'): # Check where the message is coming from
#         message = message.get('msg') # Strip the sender and just use the actual message
#         message = dict(message) # Convert the message into a dictionary for easier processing
#         if(message.get('temp')): # Check if the information you want is avilible in the message
#            print('The Temperature is ' + message.get('temp')) # Print the information (Or act on it through another method)

    print(message) # Debug print



# Example method to read data from iridium Pins
def readIridium():
    #Declare intent to modify global variable "State"
    global State
    #Sum the binary code of Iridium to determine code number
    newState = (1 * Iridium0.value()) + (2 * Iridium1.value()) + (4 * Iridium2.value())

    #If the new state is different than the old state, notify the network of the change
    if newState != State:
        #Update State value
        State = newState
        #Send that code to the network as a message
        print('Sending code ', State) #Debug Print
        sendMessage("{'Command':'"+str(State)+"'}")









#####-----Main Loop-----#####
# The main code to be run on the device. This loop includes specific timings
# to ensure device does not crash due to overflows or extra usage. Do not
# modify this code without backing up data and ensuring that you know what you
# are doing

iterations = 0 # Flag to keep track of loop iterations
while True:
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

    # Slight buffer to save resources
    time.sleep(0.2)
    iterations += 1


