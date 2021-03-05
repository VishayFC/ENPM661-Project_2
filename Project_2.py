import numpy as np

#Creating a QUEUE CLASS to access queue methods
class Queue:
    
    def __init__(self):
        self.items = []
    #To insert an element at the back of the queue 
    
    def enqueue(self, item):
        self.items.insert(0 , item)
        
    #To remove the back element     
    def dequeue(self):
        if self.items:
            return self.items.pop()
        return None
    #To return the back element   
    def peek(self):
        if self.items:
            return self.items[-1]
        return None
    #To get the length of the queue
    def size(self):
        return len(self.items)
    #To see if the queue is empty    
    def is_empty(self):
        return self.items == []

q = Queue()
b = None
c = None

def obstacle():
    
    if y1>=90 and y1<= 110 and x1>=40 and x1<=60  :
        #print('Given Node is in OBSTACLE SPACE 1')
        b = 1
        #return b

    elif (pow((y1-160),2) + pow((x1-50),2)) < 225 :
        #print('Given Node is in OBSTACLE SPACE 2')
        b = 2
        #return b
    else:
        b = 0
        
    if y2>=90 and y2<= 110 and x2>=40 and x2<=60  :
        #print('Given Node is in OBSTACLE SPACE 1')
        c = 1
        #return c

    elif (pow((y2-160),2) + pow((x2-50),2)) < 225 :
        #print('Given Node is in OBSTACLE SPACE 2')
        c = 2
        #return c
    else:
        c = 0
    return b,c

#loaded MAP
loc = cv2.imread('ref_marker.png')

#Enter Valid Co-ordinates
x1 = int(input("Input the x-coordinate of Start Node "))
y1 = int(input("Input the y-coordinate of Start Node "))
x2 = int(input("Input the x-coordinate of Goal Node "))
y2 = int(input("Input the y-coordinate of Goal Node "))
    