#this file contains led functions

def SumLed (L,  x1, y1, x2, y2):
    i  = 0
    j  = 0
    s  = 0
    
    for i in range(y1, y2):
        for j in range(x1, x2):
            s += L[i][j]
    
    print ("SumLed()", s)
    return s
   
   
   
#main program   
#declare 2D array in Python size w,h 
w, h = 5, 3

#Init with 0s
L = [[10 for x in range(w)] for y in range(h)]    


ledson = SumLed(L, 0,0, 5,3)   
print ("Summ", ledson)    





    