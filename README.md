# Creating an XBee ZigBee Mesh Network

# Process

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
