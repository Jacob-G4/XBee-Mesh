#####-----Imports-----######
import xbee #Allows communicating with the Xbee board
import machine #Allows access to pin definitions
from machine import Pin
import time #Use board clock for timing

#####-----Pins----#####
#D0 -> DIO0
#D1 -> DIO1
#D2 -> DIO2
#D3 -> DIO3
#D4 -> DIO4
Iridium0 = Pin(machine.Pin.board.D0, Pin.IN)
Iridium1 = Pin(machine.Pin.board.D1, Pin.IN)
Iridium2 = Pin(machine.Pin.board.D2, Pin.IN)

#####-----Global Variables-----#####
name = '[COORDINATOR NAME]'
iterations = 0
networkConnections = 0

#####-----Methods-----#####
#Method used to get a message from the network. Runs every iteration of the main loop
def getMessage():
    message = xbee.receive()
    if message:
        print(message)
        return message.get('payload').decode('utf-8')

#Method to send an exact string to the entire network. Includes error handling for too many consecutive messages
def sendExactMessage(message = ''):
    try:
        xbee.transmit(xbee.ADDR_BROADCAST, message)
    except OSError as e:
        print('OS error: {0}'.format(e.args))
        time.sleep(0.3)
        sendExactMessage(message)

#Method to send a message out to the entire network after formatting
def sendMessage(message = ''):
    message = "{'from':'"+name+"','msg':"+message+"}"
    sendExactMessage(message)


#####-----SPACE FOR GENERAL USERS-----#####
#Method to allow router to complete tasks, limited to every second to save processing power
def proactiveSpace():
    sendMessage("{'temp':'25','vel':'32'}")
    print('Sending')

#Method to allow router reactions to incoming messages, activates every time a message is recieved
def reactiveSpace(message):
    print(message)

def readIridium():
    State = (1 * Iridium0.value()) + (2 * Iridium1.value()) + (4 * Iridium2.value())
    sendMessage(str(State))









#####-----Main Loop-----#####
while True:
    #Check for a new message in the stack
    message = getMessage()

    #If there is a new message react to it
    if message:
        reactiveSpace(message)

    #Every 5 seconds complete actions on board
    if iterations % 5 == 0:
        proactiveSpace()
        iterations = 0

    #Slight buffer to save resources
    time.sleep(0.2)
    iterations += 1


