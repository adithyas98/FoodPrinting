#!/usr/bin/env python3



from gcode import GCode



def pyramid():
    

    #initialize the gcode class

    gcode = GCode()


    pyramid = []#list where we will hold everything

    #Startup the printer

    pyramid.append(gcode.startup(fanSpeed=255,extruder=0))

    #set to absolute
    pyramid.append(gcode.setAbsolute(absolute=True))

    #set the absolute coordinates

    pyramid.append(gcode.setAbsoluteCoordinates((0,0,0)))#set to 0,0,0

    #set to imperial (inches)

    pyramid.append(gcode.setImperial())


    ####################################
    ##########Your Code Here###########
    '''
    Put your code here for the pyramid!
    Whenever you want to add a line to the gcode
    use 
    pyramid.append(#Function here)
    '''


    #Move the extruder away from the print
    pyramid.append(gcode.move((0,0,8))


if __name__ == '__main__':

    lines  = pyramid()
    with open('pyramid.gcode', 'w') as f:
        f.writelines(lines)
