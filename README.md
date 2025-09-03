# XBee Mesh

Process (ROUGH)
connect Xbee devices to XCTU software with default connection settings
ensure firmware is set to latest ZigBee protocol (Digi XBee3 Zigbee 3.0 1014 as of writing)


SET UP THE COORDINATOR
Set up one device, which will be connected to Iridium to be the coordinator, the head of the network. This makes sense because without iridium the network cannot function anyways so having them on the same power source makes sense
Set the device to a coordinator by changing the device role option (CE) to Form Network
Set the PAN ID (ID) to a name for the network, this is similar to an SSID and all components of the network must have the same PAN ID or they will not connect
Change the Node Identifier (NI) to a recognizable name, this is the name that will show in XCTU to differentiate the devices easily
    Note the default name for the device is a single blank space so ensure that it was deleted before you flash the new firmware settings
update the Python Autostart (PS) parameter to automatically run the python file we will be adding to the XBee
Use the write button at the top of the XCTU page to flash the new settings to the device

SET UP THE ROUTERS
Set up any number of routers for the network to be used in each payload.
Set the device to an endpoint by changing the device role option (CE) to Join Network
Set the PAN ID (ID) to match that of the coordinator
These settings can be saved to a profile to more easily create multiple routers
Change the Node Identifier (NI) to a recognizable name, this is the name that will show in XCTU to differentiate the devices easily
    Note the default name for the device is a single blank space so ensure that it was deleted before you flash the new firmware settings
update the Python Autostart (PS) parameter to automatically run the python file we will be adding to the XBee
Use the write button at the top of the XCTU page to flash the new settings to the device
