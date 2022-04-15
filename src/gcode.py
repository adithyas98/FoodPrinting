#!/usr/bin/env python3




class GCode:
    '''
    This class will help abstract away from the complexity of gcode and allow 
    for focus on creating complex food structures
    '''

    def __init__(self):
        self.absolute = True
        self.absoluteCordinates = None
        self.imperial = False
    def moveZ(self,Z):
        '''
        This method will quick move the nozzle in the Z direction. Depending
        on the setting it will to the following:
            Absolute: Will move to the specified location relative to the 
                    current origin
            Relative: Will move the nozzle along the Z relative to the current
                        position
        Inputs:
            - Z - the z input for movement
        Outputs:
            - the gcode required to take the action
        '''
        return "G0 Z{}".format(Z)
    def startup(self,fanSpeed=255,extruder=0):
        '''
        This will handle all of the startup tasks that you need to complete
        before you start printing
        Inputs:
            - fanSpeed: range from 0-255 that controls the fan speed
        Output:
            - Code to start up the printing process
        '''
        code = ''
        code += "M106 S{}".format(fanSpeed)
        return code

    def switchExtruder(self,extruder=0):
        '''
        Will switch th extruder to the specified extruder
        Input:
            -extruder: a value 0 or 1 to pick the extruder
        Output:
            - the code required to change the extruder
        '''
        assert extruder in [0,1]
        return "T{}".format(extruder)
    def line(self,p1,p2,movSpeed,extrude):
        '''
        Will move/draw a line between points p1 and p2
        Inputs:
            - p1: a tuple (x1,y1) representing point p1
            - p2: a tuple (x2,y2) representing point p2
            - movSpeed: Moving Speed of the nozzle
            - extrude:how much the extruder will extrude
        Outputs:
            - Gcode required to make the change
        '''
        #TODO: Handle the relative case
        code = '' 
        #first move the extruder to point p1
        code += 'G0 X{} Y{}\n'.format(p1[0],p1[1])
        code += 'G1 X{} Y{} E{} F{}\n'.format(p2[0],p2[1],extrude,movSpeed)

        #Now we can return the gcode
        return code
    def setAbsolute(self,absolute=True):
        '''
        Will change the status of absolute or relative
        Input:
            - Absolute: (boolean) True if you want absolute coordinates
                        False if you want relative coordinates
        Output:
            - Gcode required to make the change
        '''
        if absolute:
            #Then we want to switch to absolute
            code = 'G90\n'
        else:
            #Then we want to switch to relative
            code = 'G91\n'
        self.absolute = absolute
        return code
    def setAbsoluteCoordinates(self,point):
        '''
        Will set the absolute coordinate and switch the status to absolute
        Inputs:
            - point: A tuple (x,y,z) to set as the absolute reference
        Output:
            - Gcode required to make change
        '''
        code = 'G92 X{} Y{} Z{}'.format(point[0],point[1],point[2])
        #We want to save the coordinates so we can retrieve them later
        self.absoluteCordinates = point

        return code
    def getAbsoluteCoordinates(self):
        '''
        Output:
            - Will return the absolute coordinates currently set
                Tuple (x,y,z)
            - None if no absolute coordinates have been set
        '''
        return self.absoluteCordinates
    def setImperial(self,imperial=True):
        '''
        Will set the units to imperial (if input is True) and metric
        (if input is False).
        Inputs:
            - imperial: (Boolean) True if you want units to be inches. False,
                    for centimeters.
        Outputs:
            - gcode required to make the change
        '''
        self.imperial = imperial
        if imperial:
            #Then we want to set it it to imperial
            return 'G20\n'
        else:
            #we want to set to metric
            return 'G21\n'

    def move(self,point):
        '''
        Will move the printer away
        Input:
            - point:will move the printer to the point (absolute mode)
                or by the specified amount (relative mode)
                point is a tuple (x,y,z)

        '''
        return "G0 X{} Y{} Z{}".format(point[0],point[1],point[2])
    def getUnits(self):
        '''
        Will get the units currently being used
        Input:
            - None
        Output:
            - will get the units currently being used
        '''
        if self.imperial:
            #Then we are using imperial
            return "Imperial(in)"
        else:
            #metric
            return "Metric(mm)"
    def filledRectangle(self,
        '''
        Will create a rectangle and fill it the specified desity
        '''
        #TODO: Implement this method
        pass
