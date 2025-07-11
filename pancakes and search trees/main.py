

# Thomas Schaeffer
# 10/5/23
 
# References: 
# [1] https://stackoverflow.com/questions/403421/how-do-i-sort-a-list-of-objects-based-on-an-attribute-of-the-objects
# [2] https://stackoverflow.com/questions/35166633/how-do-i-multiply-each-element-in-a-list-by-a-number

class node:
    def __init__(self,seq,ori):
        self.seq = seq[:]
        self.ori = ori[:]
        self.key = node_str(seq,ori)
        self.parent =[]
        self.flips = 0                        # indice tracks location of flip
        self.heur = 0
        self.g = 0
        self.cost = []
      
    
    def addParent(self,parent_node):            # track node path via 'parents'
        if parent_node.parent != []:            # only append when parent node also has parents
            self.parent.extend(parent_node.parent)
        
        # format parent str to include location of next flip
        parent_str = parent_node.key[:(parent_node.flips*2 + 2)] + '|' + parent_node.key[(parent_node.flips*2 + 2):] 
        self.parent.extend([parent_str])

        # format cost statement
        cost = 'g:'+str(parent_node.g)+',  h:'+str(parent_node.heur)
        if parent_node.cost !=[]:
            self.cost.extend(parent_node.cost)
        
        self.cost.extend([cost])

        
    def h(self):
        oop = []
        
        #check sequence for oop pancakes
        #assign the largest of them to h()
        for i in range(4):

            if self.seq[i] != i + 1:
                oop.append(self.seq[i])

            if oop != []:
                heur = max(oop)
            else:
                heur = 0

        self.heur = heur

        #cost = amount flipped
        #heur = largest oop
    

# function takes string input, returns orientation array of -1/1
def str2ori(string):
    output = []
    
    for i in range(4):
            
        if string[i] == 'b':              
            output.append(-1) # append a -1 when burn side up               
        else:
            output.append(1) # 1 when white side up
            
    return output


# function takes node data (seq/ori), returns string of init structure 
def node_str(seq,ori):
    
    output = ''
    
    for i in range(4):
        output+=(str(seq[i]))
        
        if ori[i] == -1:              
            output+='b' # append a -1 when burn side up               
        else:
            output+='w' # "       " 1 when white side up
            
    return output
    
        
# flip fcn takes node object and returns a new pancake sequence with their new orientations
def flip(nodes,n):                        # n = number of pancakes flipped
    seq = nodes.seq     
    ori = nodes.ori
    
    temp_seq = seq[:n]                    # reverse sequence of pancakes flipped
    temp_seq.reverse()
    new_seq = temp_seq + seq[n:]          # concatinate flipped stack with non-flipped
    
    temp_ori = [i * -1 for i in ori[:n]]  # mult ori by -1 to 'flip'. This syntax was 
    new_ori = temp_ori + ori[n:]          # concatinate with non-flipped
    
    temp_ori2 = new_ori[:n]               # orientation sequence must be re-sorted
    temp_ori2.reverse()                   # to align with new pancake sequence
    new_ori2 = temp_ori2 + ori[n:]
               
    return new_seq, new_ori2

def tie(nodes):

    tie_val = ''
    for i in range(4):
        tie_val += str(nodes.seq[i])
        if nodes.ori[i] == 'w':
            tie_val += '1'
        else:
            tie_val += '0'
    
    return tie_val


def BFS(s):
    str_des = '1w2w3w4w'   # solve condition
    
    visited = []           # visited nodes initialization      
    q = [s]                # initialize queue/fringe at start (s)
          
    while q != []:

        cur_node = q.pop(0)                              # remove first node from queue & assign
        
        if cur_node.key == str_des:                      # check for sol
            cur_node.parent.append(str_des)              # add solution to node path
            return cur_node.parent                       # return path
            
        elif cur_node.key not in visited:
            visited.append(cur_node.key)
              
            
            for i in range(4):
                [flip_seq, flip_ori]=flip(cur_node,i+1)  # create branch node from flip 
                branch_node = node(flip_seq,flip_ori)    # parents include cur_node and cur_node's parents   
                branch_node.addParent(cur_node)          # adds cur_node str to parent list of branch node
                cur_node.flips = i + 1                   # records the flip indice when branch is created
                q.append(branch_node)                    
                   
    return print('failure')       


def Astar(s):
    str_des = '1w2w3w4w'   # solve condition
    
    visited = []           # visited nodes initialization      
    q = [s]                # initialize queue/fringe at start (s)

    while q != []:

        q = sorted(q, key=lambda x: (x.heur + x.g), reverse=False)   # sort queue based on cost = h+g, see [1]   
        
        
        if len(q) > 1:    
            if q[0].heur + q[0].g == q[1].heur + q[1].g:
                if int(tie(q[0])) < int(tie(q[1])):
                    first_ele = q.pop(0)   
                    second_ele = q.pop(0) 
                 # inserting in each others positions
                    q.insert(0, second_ele)  
                    q.insert(1, first_ele)  
                
        cur_node = q.pop(0)                                          # remove first node from queue & assign
                
        if cur_node.key == str_des:                                  # check for sol
            cur_node.parent.append(str_des)                          # add solution to node path
            g_final = cur_node.g + cur_node.flips                    # calculate final g
            last_cost = 'g:'+str(g_final)+',  h:'+str(cur_node.heur) # assign string for final costs
            cur_node.cost.append(last_cost)                          # add this to path costs
            return cur_node.parent , cur_node.cost                   # return path & cost list
                    
        elif cur_node.key not in visited:
            visited.append(cur_node.key)
              
            b_nodes = []
            for i in range(4):
                [flip_seq, flip_ori]=flip(cur_node,i+1)  # obtain new node seq/ori from flip 
                branch_node = node(flip_seq,flip_ori)    # parents include cur_node and cur_node's parents   
                branch_node.addParent(cur_node)          # adds cur_node str to parent list of branch node
                branch_node.h()                          # call heuristic method to calculate  node.heur
                branch_node.g = cur_node.g + (i + 1)     # assign g based on previous flips + new pancakes flipped
                cur_node.flips = i + 1                   # records the flip indice when branch is created
                b_nodes.append(branch_node)              # place new node in branch list

            q.extend(b_nodes)                            # add new nodes to queue
                
    return print('failure')                              # fail-case 
    


init = input()                                                      # take input for initial stack
init_seq = [int(init[0]),int(init[2]),int(init[4]),int(init[6])]    # parse string for seq
init_ori = str2ori([init[1],init[3],init[5],init[7]])               # and for orientations
s = node(init_seq,init_ori)                                         # create start node
method = init[9]

# call method based on innput
if method == 'b':
    path = BFS(s)   
    
elif method == 'a':
    path, cost = Astar(s)

# format output
for i in range(len(path)):

    if method == 'a':                   # a* outputs node path and costs
        print(path[i] +' '+ cost[i])

    elif method == 'b':                 # bfs outputs node path
        print(path[i])


