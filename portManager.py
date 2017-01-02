#-------------------------------------------------------------------------------
# Name:        portManager
# Purpose:
#
# Author:      anand
#
# Created:     07/10/2016
# Copyright:   (c) anand 2016
# Licence:     none
#-------------------------------------------------------------------------------
## Questions / To Do
## Device class' "List<PhysicalPort> port_list"
## 1-1 mapping for port - device
## string action on TrafficXPort
## ID Issue

class Device:
# List<PhysicalPort> port_list
    def __init__(self, id, name="", port_list=""):
        self.id = id
        self.name = name
        self.port_list = port_list

    def displayPort_list(self):
        return self.port_list

class PhysicalPort:
    def __init__(self, id):
        self.id = id

    def displayID(self):
        return self.id()

class Copper(PhysicalPort, Device):
    def __init__(self, id, deviceName):
        self.id = id
        self.deviceName = deviceName

    def displayDeviceName(self):
        return self.deviceName

    def displayDevice(self):
        if Device.port_list == self.id:
            print "Associated Device: " + Device.port_list
        else:
            print "No associated device"

class Fiber(PhysicalPort, Device):
    def __init__(self, id, wavelength, deviceName):
        self.id = id
        self.wavelength = wavelength

    def displayWavelength(self):
        return self.wavelength

    def displayDeviceName(self):
        return self.deviceName

    def displayDevice(self):
        if Device.port_list == self.id:
            print "Associated Device: " + Device.port_list
        else:
            print "No associated device"

class Traffic:
    def __init__(self, name="", trafficType="", layer4_port=0):
        self.name = name
        self.trafficType = trafficType
        self.layer4_port = layer4_port

    def displayPortNumber(self):
        return self.layer4_port

class TrafficXPort:
    def __init__(self, protocolName="", protocolType="", portNumber=""):
        self.protocolName = protocolName
        self.protocolType = protocolType

        if portNumber == PhysicalPort.id:
            self.portNumber = portNumber
            print "port number and type matches"

def main():
    pass

if __name__ == '__main__':
    main()
