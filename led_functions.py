import re # we import Regex

##########################################
# This part of file contains led functions
###########################################

#
# This function counts all leds that are on. We just go 
# through array and count leds that "true" 
#
def SumLed (L,  arrSize):
    i  = 0
    j  = 0
    s  = 0
    
    for i in range(arrSize):
        for j in range(arrSize):
            if (L[i][j] == True):
                s += 1;
    return s

#
#  This function switches on or off leds - depends on value 
#
#    Note on indexing.  for arrSize of = 10, the indexes
#    user should put will be from 0..9 - inclusive. so, for our example
#    SwithcOnOffLed(L, (0,9) , (0,9), 10 , True) will switch on 100 leds - whole 2D array.
#
def SwitchOnOffLed (L, x1, y1, x2, y2, arrSize, value):
    i  = 0
    j  = 0
    for i in range(max(0, y1), min(arrSize, y2 + 1)):
        for j in range(max(0, x1), min(arrSize, x2 + 1)):
            L[i][j] = value
    
    return L

#
#  This function switches on or off leds - depends on value 
#
#    Note on indexing.  for arrSize of = 10, the indexes
#    user should put will be from 0..9 - inclusive. so, for our example
#    InvertLed(L, (0,9) , (0,9), 10 , True) will invert 100 leds - whole 2D array.
#
def InvertLed (L,  x1, y1, x2, y2, arrSize):
    i  = 0
    j  = 0
    for i in range(max(0, y1), min(arrSize, y2 + 1)):
        for j in range(max(0, x1), min(arrSize, x2 + 1)):
            if (L[i][j] == True):
                L[i][j] = False
            else:
                L[i][j] = True
    return L
    


##########################################
# This part of file contains test functions
###########################################

# This function prints and checks result 
# of test
def CheckTest(i, res, succVal):
    print ("\tTest ", i, ":  Sum=", res)    
    if  res == succVal:
        print ("   PASS")
    else:
        print("   FAIL")
    return

# Function has series of tests
def TestLed(L, arraySize):
    # Set some leds on/off
    L = SwitchOnOffLed (L, 0,0, 5,3, arraySize, True)  # 24 leds are on
    CheckTest(1, SumLed(L, arraySize), 24)
    
    L = SwitchOnOffLed(L, 0,0, 2,2, arraySize, False) # 9 leds are off
    CheckTest(2, SumLed(L, arraySize), 15)
    
    #invert some leds
    L = InvertLed(L, 0,0, 9,9, arraySize) # 100 leds are inverted
    CheckTest(3, SumLed(L, arraySize), 85)

    return L

#
# This function parses string using Regex
#
def ParseString(s, arraySize):
    m = re.search(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*", s)    
        
    if m: 
        print("\tPARSING: ", s)   
        x1 = int(m.group(2))
        y1 = int(m.group(3))
        x2 = int(m.group(4))
        y2 = int(m.group(5))

        if m.group(1) == "turn on":    
            SwitchOnOffLed (L, x1, y1, x2, y2, arraySize, True)
        elif m.group(1) == "turn off":
            SwitchOnOffLed (L, x1, y1, x2, y2, arraySize, False)
        elif m.group(1) == "switch":
            InvertLed (L, x1, y1, x2, y2, arraySize)
        else:
            print("Error in command parsing.") # actually we never should get here
        return 1
    else:
        print("WARNING: Can't recognize command ", s, ". Ignored.")
        return 0
    
    
def TestParser(L, arr):
    ParseString("turn on 0,0 through 9,4", arr)
    ParseString("turn off 0,5 through 9,9", arr)
    
    CheckTest(4, SumLed(L, arr), 50)
  
    ParseString("switch 1,5 through 9,9", arr)
    CheckTest(5, SumLed(L, arr), 95)
        
    return
    
    
# 
# main program   
#############################

arraySize = 10  # our max array size

# NOTE, L is our array. We declare it as 2D and init with "False"
L = [[False for x in range(arraySize)] for y in range(arraySize)]    

# Now let's do some internal tests:
print("\nInternal LED functions tests...")
TestLed(L, arraySize)

print("\nInternal parser tests..")
TestParser(L, arraySize)

