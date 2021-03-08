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


def obsornot(xcor,ycor):
    
    if ((ycor) + (1.42814 * xcor) >= 176.55) and ((ycor) - (0.7 * xcor) >= 74.39) and ((ycor) + (1.428 * xcor) <= 428.068) and ((ycor) - (0.7 * xcor) <= 98.805):
        loc[299 - ycor][xcor][:] = 0
        #print('Slant Rectangle')
        return 1
    elif (pow((xcor-90),2) + pow((ycor-70),2)) < 1225 :
        loc[299 - ycor][xcor][:] = 0
        #print('Circle')
        return 2
    if xcor<0 or xcor>=400 or ycor<0 or ycor>=300 :
        #print('Out of Map')
        return 3
    elif (xcor>=200 and xcor<= 210 and ycor<=280 and ycor>=230) or (xcor>=200 and xcor<=230 and ycor<=280 and ycor>=270) or (xcor>=200 and xcor<=230 and ycor<=240 and ycor>=230):
        loc[299 - ycor][xcor][:] = 0
        #print('C-Shape')
        return 4
    elif (((xcor - 246) / 60) ** 2) + (((ycor - 145) / 30) ** 2) <= 1:
        loc[299 - ycor][xcor][:] = 0
        #print('Elipse')
        return 5
    elif(ycor + xcor >= 391) and (xcor - ycor <= 265) and (ycor + 0.49646 * xcor <= 305.20202) and (0.89003 * xcor - ycor >= 148.7438):
        loc[299 - ycor][xcor][:] = 0
        #print('Polygon_1')
        return 6
    elif(ycor + 0.49646*xcor >= 305.20202) and (ycor + 0.81259*xcor <= 425.66019) and (ycor + 0.17512 * xcor <= 199.99422):
        loc[299 - ycor][xcor][:] = 0
        #print('Polygon_2')
        return 7
    elif(ycor + 13.49145*xcor <= 5256.7216) and (1.43169*xcor - ycor >= 368.82072) and (ycor + 0.81259*xcor >= 425.66019):
        loc[299 - ycor][xcor][:] = 0
        #print('Polygon_3')
        return 8
    else:
        return None

#loaded MAP
loc =  255 * np.ones((300,400,3))

#Enter Valid Co-ordinates
x1 = int(input("Input the x-coordinate of Start Node "))
y1 = int(input("Input the y-coordinate of Start Node "))
x2 = int(input("Input the x-coordinate of Goal Node "))
y2 = int(input("Input the y-coordinate of Goal Node "))

print("")

#Checking if the points are in any obstacle space and giving the approprite error message
if obsornot(x1,y1) == 1:
    print('Error : Start Node is in the Slanted Rectangle',)
elif obsornot(x1,y1) == 2:
    print('Error : Start Node is in the Circle',)
elif obsornot(x1,y1) == 3:
    print('Error : Start Node is out of map boundary',)
elif obsornot(x1,y1) == 4:
    print('Error : Start Node is in the C-Shape',)
elif obsornot(x1,y1) == 5:
    print('Error : Start Node is in the Elipse',)
elif obsornot(x1,y1) == 6 or obsornot(x1,y1) == 7 or obsornot(x1,y1) == 8:
    print('Error : Start Node is in the Polygon',)
    
if obsornot(x2,y2) == 1:
    print('Error : Goal Node is in the Slanted Rectangle',)
elif obsornot(x2,y2) == 2:
    print('Error : Goal Node is in the Circle',)
elif obsornot(x2,y2) == 3:
    print('Error : Goal Node is out of map boundary',)
elif obsornot(x2,y2) == 4:
    print('Error : Goal Node is in the C-Shape',)
elif obsornot(x2,y2) == 5:
    print('Error : Goal Node is in the Elipse',)
elif obsornot(x2,y2) == 6 or obsornot(x2,y2) == 7 or obsornot(x2,y2) == 8:
    print('Error : Goal Node is in the Polygon',)

#Entering the input points in a start and goal array     
start = np.array([x1,y1])
goal = np.array([x2,y2])

start_parent = None

vis = list()
path = list()

#Adding the root to the queue
q.enqueue(start)

#Appending root and its parent to visited list
vis.append((start,start_parent))

#Updating the parent node by dequeueing the previous parent after it has produced all its children
def currentnode():

    cn1 = q.dequeue()
    
    a = cn1[0]
    b = cn1[1]
    
    return cn1,a,b

#String functions to convert the array elements into strings
def string(cn):
    string=""
    for i in range(len(cn)):
        string=string+" "+str(cn[i])
    return string

#All 8 possible move functions
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


#This function calls the appropriate move functions and calls functions to check if they --
# are in obstacle space and in the visited list 

#The function returns the child nodes created of the current parent, the parent itself and the valid chidren 
def move(i,j,cn1):
    
    children = list ()
   
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
    
    valid_childs = obstacle(children)
    
    fchilds = visitornot(valid_childs,cn1) 
     
    return valid_childs,cn1,fchilds 


#Checking if the co-ordinates of the points passed are in any obstacle space
def obstacle(children):
    
    valid_childs = list()
    
    for i in range(len(children)):
        val = obsornot(children[i][0],children[i][1])
        if val == None:
            valid_childs.append(children[i])
    return valid_childs  
      
#The list of valid children is passed to this functions which returns if --
# they are in the visited list or not by comparing them with the elements in the list
def visitornot(vchilds,cn1):

    filter_child = list()
    check = 0 
    for j in range(len(vchilds)):
        for i in range(len(vis)):
            if string(vis[i][0]) == string(vchilds[j]):
                check = 1
                break
            else:
                check = 0
        if check == 0:
            vis.append((vchilds[j],cn1))
            filter_child.append(vchilds[j])
    return filter_child        

#Comparing the filtered children with goal node 
def gsornot(parent, filtered) :
    
    childs = np.asarray(filtered)
    
    for i in range(len(filtered)):
        if np.array_equiv(childs[i],goal) == True:
           print('Goal Reached') 
           return childs[i],parent
        else: 
            q.enqueue(childs[i])
    return 

#Running the loop till the goal node is reached
y = None

while y is None :
    
    cn1,i,j = currentnode()
    
    lis, parent, flist = move(i,j,cn1)
    
    y = gsornot(parent, flist)

child=y[0]

#Tracking back from goal node to the first child
while np.array_equiv(parent,start) ==  False:
    
    for i in range(len(vis)):
         
        if string(child) == string(vis[i][0]):
            parent = vis[i][1] 
            child  = vis[i][1]                           
            path.append(vis[i][0])
            break

#Appending the root node and reversing to get the path             
path.append(start)
#path.reverse()

out = cv2.VideoWriter('P.avi',cv2.VideoWriter_fourcc(*'XVID'), 30, (400,300))
         
#Visualization
vislist =[]
for i in range(len(vis)):
    vislist.append(vis[i][0].tolist())
vislist.pop(0)
one = list()

for i in range(300):
    for j in range(400):
        obsornot(j,i)

for i in range(len(vis)-6):
    one = one + [vislist[i]]
    for j in one:
        loc[299 - j[1]][j[0]][0] = 0
        loc[299 - j[1]][j[0]][1] = 255
        loc[299 - j[1]][j[0]][2] = 255
    
    loc = loc.astype(np.uint8)
    cv2.imshow("Loc",loc)
    out.write(loc)
    cv2.waitKey(1)
    
#Path Visualization    
for i in range(len(path)):
    loc[299 - path[i][1]][path[i][0]][:] = (255,0,0)
    cv2.imshow('Loc',loc)
    out.write(loc)
    cv2.waitKey(1)
  
cv2.waitKey(0)    
cv2.destroyAllWindows()     