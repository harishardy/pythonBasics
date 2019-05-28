'''
Created on 27 May 2019

@author: harishhardy
'''



def compareTriplets(x,y):
    #print(x,y)
    initialArray = [0,0]
    
    for c in range(0,len(x)):
        if x[c] > y[c]:
            initialArray[0] += 1
        if x[c] < y[c]:
            initialArray[1] += 1
    print(initialArray)         
    
        
a = [95,67,88]
b = [85,37,79]


compareTriplets(a,b) 

  
    

    


