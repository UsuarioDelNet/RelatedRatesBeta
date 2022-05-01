import math


def findingdrdt():
    changeH = int(input("Change in height: "))
    changeV = int(input("Change in Volume: "))
    h = int(input("Height: "))
    V = int(input("Volume: "))
    piNum = math.pi
    radSqrd = int(((3*V)/piNum)/h)
    rad = math.sqrt(radSqrd)
    changeR1 = (3*changeV)/piNum
    changeR2 = changeR1 -(radSqrd*changeH)
    changeRFinal = changeR2 /(2*rad)
    print (changeRFinal)
findingdrdt()

def findingdhdt():
    changeR = int(input("Change in radius: "))
    changeV = int(input("Change in Volume: "))
    rad = int(input("Radius: "))
    V = int(input("Volume: "))
    piNum = math.pi
    h = int(((3*V)/piNum)/rad**2)
    changeH1 = (3*changeV)/piNum
    changeH2 = changeH1 -(2*(rad)*(changeR))
    changeHFinal = changeH2 /(rad**2)
    print (changeHFinal)
findingdhdt()

#def findingdVdt():
#    changeR = int(input("Change in radius: "))
#    changeH = int(input("Change in height: "))
#    rad = int(input("Radius: "))
#    H = int(input("Height: "))
#    piNum = math.pi
#    changeV1 = (2/3)(piNum)*(rad)*(changeR)*H
#    changeV2 = (1/3)(piNum)*(math.pow(rad,2))*(changeH)
#    changeVFinal = changeV1 + changeV2
#    print (changeVFinal)
#findingdVdt()


