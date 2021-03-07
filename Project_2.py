import numpy as np
import cv2

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

def obsornot(xcor,ycor):
    
    if ycor>=90 and ycor<= 110 and xcor>=40 and xcor<=60  :
        return 1
    elif (pow((ycor-160),2) + pow((xcor-50),2)) < 225 :
        return 2
    if ycor<0 or ycor>200 or xcor<0 or xcor>100 :
        return 3
    else:
        return 

#loaded MAP
loc = cv2.imread('ref_marker.png')

#Enter Valid Co-ordinates
x1 = int(input("Input the x-coordinate of Start Node "))
y1 = int(input("Input the y-coordinate of Start Node "))
x2 = int(input("Input the x-coordinate of Goal Node "))
y2 = int(input("Input the y-coordinate of Goal Node "))

print("")

if obsornot(x1,y1) == 1:
    print('Error : Start Node is in Obstacle Space 1',)
elif obsornot(x1,y1) == 2:
    print('Error : Start Node is in Obstacle Space 2',)
elif obsornot(x1,y1) == 3:
    print('Error : Start Node is out of map boundary',)
    
if obsornot(x2,y2) == 1:
    print('Error : Goal Node is in Obstacle Space 1',)
elif obsornot(x2,y2) == 2:
    print('Error : Goal Node is in Obstacle Space 2',)
elif obsornot(x2,y2) == 3:
    print('Error : Goal Node is out of map boundary',)

    
#start = np.array([x1,y1])
#goal = np.array([x2,y2])

start = np.array([0,0])
goal = np.array([30,30])

#start = root[3][2]
#goal = root[2][1]
#val = loc[x1][y1]
#print(start)
#print(goal)
#print(val)

#start_parent = None

vis = list()
path = list()
vis_str = list()

#Adding the root to the queue
q.enqueue(start)

#Appending root to visited list
vis.append(start)
#vis.append((start,start_parent))

def currentnode():

    cn1 = q.dequeue()
    
    #print('Queue FULL : ',q.items)
    
    a = cn1[0]
    b = cn1[1]
    
    #check if cn1 is in obstacle space
    
    return cn1,a,b

def string(cn):
    string=""
    for i in range(len(cn)):
        #for j in range(len(cn[0])):
        string=string+" "+str(cn[i])
    return string

def up(i,j):
    cn2 = cn1.copy()
    i = i 
    j = j + 1
    cn2 = np.array([i,j])
    #print('CN2 UP',cn2)
    return cn2
   
def down(i,j):
    cn3 = cn1.copy()
    i = i 
    j = j - 1
    cn3 = np.array([i,j])
    #print('CN2 DOWN',cn3)
    return cn3

def right(i,j):
    cn4 = cn1.copy()
    i = i + 1
    j = j 
    cn4 = np.array([i,j])
    #print('CN2 RIGHT',cn4)
    return cn4
   
def left(i,j):
    cn5 = cn1.copy()
    i = i - 1
    j = j 
    cn5 = np.array([i,j])
    #print('CN2 LEFT',cn5)
    return cn5

def upright(i,j):
    cn6 = cn1.copy()
    i = i + 1
    j = j + 1
    cn6 = np.array([i,j])
    #print('CN2 UR',cn6)
    return cn6
    
def upleft(i,j):
    cn7 = cn1.copy()
    i = i - 1
    j = j + 1
    cn7 = np.array([i,j])
    #print('CN2 UL',cn7)
    return cn7
  
def downright(i,j):
    cn8 = cn1.copy()
    i = i + 1
    j = j - 1
    cn8 = np.array([i,j])
    #print('CN2 DR',cn8)
    return cn8
     
def downleft(i,j):
    cn9 = cn1.copy()
    i = i - 1
    j = j - 1
    cn9 = np.array([i,j])
    #print('CN2 DL',cn9)
    return cn9

def move(i,j,cn1):
    
    children = list ()
    #children_string = list()
    #valid_childs = list()
   
    cn = upright(i,j)
    children.append(cn)
    cn = upleft(i,j)
    children.append(cn)
    cn = downright(i,j)
    children.append(cn)
    cn = downleft(i,j)
    children.append(cn)
    cn = up(i,j)
    children.append(cn)
    cn = down(i,j)
    children.append(cn)
    cn = right(i,j)
    children.append(cn)
    cn = left(i,j)
    children.append(cn)
    #print('CN1 : ',cn1)
    #print('CHILDREN LIST : ',children)
    #Node in Obstacle Space or not 
         
    #print(children) 
    #print(valid_childs)
    #print(children_string)
    
    
    valid_childs = obstacle(children)
    
    #vstring = list()
    
    #for i in range(len(valid_childs)):
    #    vstring.append(string(valid_childs[i]))
    #print(vstring)
    
    fchilds = visitornot(valid_childs,cn1) 
     
    return valid_childs,cn1,fchilds 