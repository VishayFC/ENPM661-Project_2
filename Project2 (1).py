
import numpy as np
import cv2

#defining the queue class to use as a data structure
class queue():
    def __init__(self):
        self.pending = list()

    def add(self, child):
        self.pending.insert(0, child)

    def remove(self):
        if self.pending:
            return self.pending.pop()
        return None

    def peek(self):
        if self.pending:
            return self.pending[-1]


    def size(self):
        return len(self.pending)

    def isempty(self):
        if self.pending == []:
            return True
        return False


#created node class in order to save current node and it's parent
class node():
    def __init__(self, current, parent):
        self.current = current
        self.parent = parent



#defining obstacles as well as the boundaries of the map
#st[0] = y coordinate in cartesian space     st[1] = x coordinate in cartesian space
def obstacles(st):
    if ((st[1] - 90)**2 + (st[0] - 70)**2) <= 1225:
        canvas[canvas_size[0]-1-st[0]][st[1]][:] = 0
        #print("coordinate is in circle")
        return None

    elif (st[0] + st[1] >= 391) and (st[1] - st[0] <= 265) and (st[0] + 0.49646*st[1] <= 305.20202) and (0.89003*st[1] - st[0] >= 148.7438):
        canvas[canvas_size[0]-1-st[0]][st[1]][:] = 0
        #print("coordinate is in polygon")
        return None

    elif (st[0] + 0.49646*st[1] >= 305.20202) and (st[0] + 0.81259*st[1] <= 425.66019) and (st[0] + 0.17512 * st[1] <= 199.99422):
        canvas[canvas_size[0]-1-st[0]][st[1]][:] = 0
        #print("coordinate is in polygon")
        return None

    elif (st[0] + 13.49145*st[1] <= 5256.7216) and (1.43169*st[1] - st[0] >= 368.82072) and (st[0] + 0.81259*st[1] >= 425.66019):
        canvas[canvas_size[0]-1-st[0]][st[1]][:] = 0
        #print("coordinate is in polygon")
        return None

    elif (((st[1] - 246) / 60) ** 2) + (((st[0] - 145) / 30) ** 2) <= 1:
        canvas[canvas_size[0]-1-st[0]][st[1]][:] = 0
        #print("coordinate is in ellipse")
        return None

    elif (st[1] >= 200 and st[1] <= 210 and st[0] <= 280 and st[0] >= 230):
        canvas[canvas_size[0]-1-st[0]][st[1]][:] = 0
        #print("coordinate is in C shape")
        return None

    elif (st[1] >= 200 and st[1] <= 230 and st[0] <= 280 and st[0] >= 270):
        canvas[canvas_size[0]-1-st[0]][st[1]][:] = 0
        #print("coordinate is in C shape")
        return None

    elif (st[1] >= 200 and st[1] <= 230 and st[0] <= 240 and st[0] >= 230):
        canvas[canvas_size[0]-1-st[0]][st[1]][:] = 0
        #print("coordinate is in C shape")
        return None

    elif (st[0]) + (1.42814 * st[1]) >= 176.5511 and (st[0]) - (0.7 * st[1]) >= 74.39 and (st[0]) + (1.42814 * st[1]) <= 428.06815 and (st[0]) - (0.7 * st[1]) <= 98.80545:
        canvas[canvas_size[0]-1-st[0]][st[1]][:] = 0
        #print("coordinate is in rectangle")
        return None

    elif st[1] < 0 or st[1] >= canvas_size[1]:
        #canvas[st[0]][st[1]][:] = 0
        #print("coordinate is out of the map boundary")
        return None
    elif st[0] < 0 or st[0] >= canvas_size[0]:
        #canvas[st[0]][st[1]][:] = 0
        #print("coordinate is out of the map boundary")
        return None
    else :
        return st

#removes from the queue
def removing_from_queue():
    check = queue1.remove()
    visited_list.append(check)
    #for_frames.append(visited_list)
    #print("queue size ",queue1.size())
    return check



#this function performs actions and gets children
def super_move_function(currentnode):

    def moveleft(node1):
        child = node1.copy()
        child[1] = child[1] - 1


        return child

    def moveright(node1):
        child = node1.copy()
        child[1] = child[1] + 1
        return child

    def moveup(node1):
        child = node1.copy()
        child[0] = child[0] + 1
        return child

    def movedown(node1):
        child = node1.copy()
        child[0] = child[0] - 1
        return child

    def up_left(node1):
        child = node1.copy()
        child[0] = child[0] + 1
        child[1] = child[1] - 1
        return child

    def down_left(node1):
        child = node1.copy()
        child[0] = child[0] - 1
        child[1] = child[1] - 1
        return child


    def up_right(node1):
        child = node1.copy()
        child[0] = child[0] + 1
        child[1] = child[1] + 1
        return child

    def down_right(node1):
        child = node1.copy()
        child[0] = child[0] - 1
        child[1] = child[1] + 1
        return child



    new_child = list()
    node = currentnode.current

    new_child.append(moveleft(node))
    new_child.append(moveright(node))
    new_child.append(moveup(node))
    new_child.append(movedown(node))
    new_child.append(up_left(node))
    new_child.append(down_left(node))
    new_child.append(up_right(node))
    new_child.append(down_right(node))

    return new_child, node

#checking if the node is in obstacle space and returns ones which are not in the obstacle space in a list and the parent node
def check_if_in_obstacle_space(children, parent):
    valid_children = list()
    for i in children:
        poss = obstacles(i)
        if poss != None:
            valid_children.append(i)

    return valid_children, parent


#checking if the node is in the queue or has been visited previously and then appending the parent to the visited_list
def check_if_visited_or_in_queue(valid_children, parent):
    note = list()

    for i in valid_children:
        for j in range(queue1.size()):
            if i == queue1.pending[j].current:
                note.append(i)
                #new_valid_children.pop(i)
                break
    new_valid_children = list()
    for i in valid_children:
        if i not in note:
            new_valid_children.append(i)


    note = list()

    for i in new_valid_children:
        for j in visited_list:
            if i == j.current:
                note.append(i)
                break
    ultimate_children = list()
    for i in new_valid_children:
        if i not in note:
            ultimate_children.append(i)


    return ultimate_children, parent


#compares new children with goal state and adds them to the queue if tthe child is not the goal state
def compare_with_goal(ultimate_children, parent):
    for child in ultimate_children:

        if child == goal:
            print("\n Goal has been reached \n")
            return child, parent
        else:
            queue1.add(node(child, parent))
    #print("size of queue in goal ", queue1.size())
    return None




#main body of the code from this line and below
canvas_size = [300,400, 3]
canvas = 255 * np.ones((canvas_size[0],canvas_size[1], canvas_size[2]))
visited_list = list()
canvas = canvas.astype(np.uint8)
for_frames = list()


#taking the start and goal node from the user and checking if in obstacle space
n = 1
while n > 0:
    start = list()
    goal = list()
    x1 = input("Enter the x co-ordinate of the start point: ")
    y1 = input("Enter the y co-ordinate of the start point: ")
    x2 = input("Enter the x co-ordinate of the goal point: ")
    y2 = input("Enter the y co-ordinate of the goal point: ")
    start.append(int(y1))
    start.append(int(x1))
    #start.append(0)
    goal.append(int(y2))
    goal.append(int(x2))
    #goal.append(1)
    lis = [start, goal]
    strt = list()
    count = 0
    for i in lis:
        strt.append(obstacles(i))
    if strt[0] == None or strt[1] == None:
        print("Error: One of the entered point is either in obstacle space or out of map boundary")
        continue
    else:
        n = 0

first_node = node(start, None)
queue1 = queue()
queue1.add(first_node)
#print(queue1.pending[0].current)
#print(start,goal)
#print(first_node.current)
#print("it is this ",queue1.size())

#calling the main functions of the BFS
while True:
    new_node = removing_from_queue()
    children_list, parent = super_move_function(new_node)
    valid_child, parent1 = check_if_in_obstacle_space(children_list, parent)
    ultimate_child, parent2 = check_if_visited_or_in_queue(valid_child, parent1)
    child_parent = compare_with_goal(ultimate_child, parent2)
    if child_parent is not None:
        break


parent_info = child_parent[1]

#searching for the route to the goal node or backtracking
route = list()
while parent_info is not None:
    for i in range(len(visited_list)):
        if parent_info == visited_list[i].current:
            parent_info = visited_list[i].parent
            route.append(i)
            break
#print(route)

#showing the obstacles in the canvas
for i in range(canvas_size[0]):
    for j in range(canvas_size[1]):
        obstacles([i,j])

out = cv2.VideoWriter('Exploration.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 60, (400,300))

#visualization of the exploration of nodes
print("Video is saving....")
sum = list()
for i in range(len(visited_list)):
    sum = sum + [visited_list[i].current]
    for j in sum:
        canvas[(canvas_size[0]-1) - j[0]][j[1]][0] = 0
        canvas[(canvas_size[0]-1) - j[0]][j[1]][1] = 255
        canvas[(canvas_size[0]-1) - j[0]][j[1]][2] = 255
    out.write(canvas)
    #cv2.imshow("canvas1",canvas)
    cv2.waitKey(1)


#visualizing the route to the goal node
for i in route:
    #print("route ",visited_list[i].current)
    canvas[(canvas_size[0]-1) - visited_list[i].current[0]][visited_list[i].current[1]][0] = 255
    canvas[(canvas_size[0]-1) - visited_list[i].current[0]][visited_list[i].current[1]][1] = 0
    canvas[(canvas_size[0]-1) - visited_list[i].current[0]][visited_list[i].current[1]][2] = 0
    out.write(canvas)
    #cv2.imshow("canvas1",canvas)
    cv2.waitKey(1)

out.release()
print("\n Video file of visualization has been saved")
cv2.waitKey(0)
cv2.destroyAllWindows()
