# Table of Contents
1. [<u>Introduction</u>](#project-introduction)
2. [<u>Folder Structure</u>](#folder-structure)
3. [<u>How to Set Up a ZigBee Mesh Network</u>](#creating-an-xbee-zigbee-mesh-network)
4. [<u>How to Program the Xbees</u>](#programming-the-xbees)

# Project Introduction
This repository is to serve as the home and log for code developed for the SFU Nearspace Ballooning Project. This is the basis of code that was used to power communication between different payloads without the use of wires on the line. It was done using the DIGI XBee devices to communicate via radio waves.  
The Code needed to be developed from scratch and while I try to maintain it I offer no guarantees of it's abilities. This repo is primarily to serve as a home to the **Base** code, meaning that it is expected to be built upon for functionality and I am really only providing the ability to communicate between XBees on a network. There will be other code snippets that were used for the testing phase when I was persoanlly working on the project, including the code used to test commands sent be the Iridium System. 

# Folder Structure
Within the GitHub Repository you will find multiple folders for the storage of code. The two main ones are [<u>the full PyCharm Projects</u>](Code_FullProjectFolders) and [<u>the main.py code only</u>](Code_MainOnly). These two folders hold essentially the same information just operate slightly different. In the project of full projects you should download the entire folder then use PyCharm's *Open as PyCharm Project* option. For the folder that only contains the main.py code snippets you should simply copy the complete file as text and paste it into a main.py file within your PyCharm project. 

# Creating an XBee ZigBee Mesh Network

### Required Software
[<u>Digi XCTU</u>](https://www.digi.com/products/embedded-systems/digi-xbee/digi-xbee-tools/xctu)

___

### Initial Connection
- Connect Xbee devices to XCTU software with default connection settings  
- Ensure firmware is set to latest ZigBee protocol (*Digi XBee3 Zigbee 3.0 1014* as of writing)  

___

### Set Up The Coordinator
> A **Coordinator** is the head of the network, this device will be the one creating the network and establishing the paths to each end node.  

Set up one device, which will be connected to Iridium to be the Coordinator, the head of the network. This makes sense because without the inputs from Iridium the network cannot function anyways  
1. Set the device to a coordinator by changing the device role option (***CE***) to Form Network  
2. Set the PAN ID (***ID***) to a name for the network
    > **Note:** This is similar to an SSID and all components of the network must have the same PAN ID or they will not connect  
3. Change the Node Identifier (***NI***) to a recognizable name, this is the name that will show in XCTU to differentiate the devices easily  
    > **Note:** The default name for the device is a single blank space so ensure that it was deleted before you flash the new firmware settings  
4. Update the Python Autostart (***PS***) parameter to automatically run the python file we will be adding to the XBee  
5. Use the write button at the top of the XCTU page to - flash the new settings to the device  

___

### Set Up The Routers
> A **Router** is the "endpoint" of the network. Routers cannot create a network and must be connected to a Coordinator to be used. Routers can send and recieve info from the entire network through addressed messages or network wide messages. Routers can also pass code along if they are part of a chain of Routers.  

Set up any number of routers for the network to be used in each payload.  
1. Set the device to an endpoint by changing the device role option (***CE***) to Join Network  
2. Set the PAN ID (***ID***) to match that of the coordinator
    > These settings can be saved to a profile to more easily create multiple routers  
3. Change the Node Identifier (***NI***) to a recognizable name, this is the name that will show in XCTU to differentiate the devices easily
    > Note: The default name for the device is a single blank space so ensure that it was deleted before you flash the new firmware settings
4. Update the Python Autostart (***PS***) parameter to automatically run the python file we will be adding to the XBee  
5. Use the write button at the top of the XCTU page to flash the new settings to the device

# Programming the Xbees

### Required Software
[<u>PyCharm Version 25.1.6</u>](https://www.jetbrains.com/pycharm/download/other.html)  
[<u>Digi Xbee Plugin Version 2.1.12</u>](https://plugins.jetbrains.com/plugin/12445-digi-xbee/versions/stable)

### How to connect to and flash the XBee
Upon opening a PyCharm project, if the Digi Xbee Plugin was successfully installer there will be a dropdown menu at the center of the top toolbar that will allow you to connect to an XBee device.   
After the device is successfully connected use the default build settings and simply press the run button in the top toolbar. If the build configuration is not correct set the project path to be the path of the ***Folder*** of the project, not just the main file you want to use.
> Note: Both the ***Folder*** path and the ***Main*** path seem to work well, however in all testing the ***Folder*** path was used so I can only recommend that with certainty.

### Program notes
All necessary code for the running of the Xbee is within one python file for the purposes of simplicity and understanding. With the knowledge that this code will be looked at and modified by people of all expereince levels I thought it was best to keep everything together as opposed to using multiple libraries.  

With that noted, users should primarily work in the ***General Users*** space within the program. Changing other aspects of the code could lead to catastrophic crashes, especially when connecting multiple XBee devices to the same network.   

It must also be noted that anytime you need to send a message to the network must be in the form of ```sendMessage("{'Title0':'StringValue','Title2':'" + str(IntValue) + "'})"``` where String values can be added directly but all other values must be cast to a string and appended in place. Messages ***MUST*** Start and end with ```"{``` and ```}"``` to be processed as a dictionary, and Token-Value pairs ***MUST*** be seperated by ```:``` with ```'``` surrounding each token and value.

Other notes may be found within the comments within the CoordinatorBaseCode and RouterBaseCode files along with examples of code that have been commented out.