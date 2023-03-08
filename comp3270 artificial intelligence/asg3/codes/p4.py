import copy,random,math
#To run the code, type "python3 p4.py" in the terminal. 
# Please note that it takes about 5 seconds to run the program with 10 iteration.
#Findings:
#1. it is helpful for temporal difference learning to decay the lr of different q values respectively
#decay the learning rate of each q value respectively, decay it every time it is updated
#decay the episilon every time the game restarts
#2. To train the policy towards the optimal one, we can make it risk-averse by amplifying the reward of winning or the negative reward of losing
#3. It is helpful to use the modified sigmoid function to decay the learning rate and episilon, that makes the decaying rate decrease, which is helpful for convergence of the policy
#4. Sometimes the policy can converge with constant lr and episilon, but decaying might make the convergence faster.
#5. The overall probability of finding the optimal policy ranges from about 60%-90%.
#6. Adequate samples (experiences) are needed for the accuracy of temperal difference learning, in this program, the number of required iteration for each finalized policy should be no less than 2000.
def game_end(game_map):
    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            if game_map[i][j] == "P":
                return False
    return True

def generate_successor(game_map,move,row_cor,col_cor):
    if move == "N":
        if (row_cor == 0):
            return game_map
        elif game_map[row_cor-1][col_cor] == "#":
            return game_map
        elif game_map[row_cor-1][col_cor][-1].isdigit() == True:
            game_map[row_cor][col_cor] = "_"
        else:
            game_map[row_cor][col_cor] = "_"
            game_map[row_cor-1][col_cor] = "P"
    elif move == "S":
        if (row_cor == len(game_map)-1):
            return game_map
        elif game_map[row_cor+1][col_cor] == "#" :
            return game_map
        elif game_map[row_cor+1][col_cor][-1].isdigit() == True:
            game_map[row_cor][col_cor] = "_"
        else:
            game_map[row_cor][col_cor] = "_"
            game_map[row_cor+1][col_cor] = "P"
    elif move == "W":
        if  (col_cor == 0):
            return game_map
        elif game_map[row_cor][col_cor-1] == "#":
            return game_map
        elif game_map[row_cor][col_cor-1][-1].isdigit() == True:
            game_map[row_cor][col_cor] = "_"
        else:
            game_map[row_cor][col_cor] = "_"
            game_map[row_cor][col_cor-1] = "P"
    elif move == "E":
        if  (col_cor == len(game_map[row_cor])-1):
            return game_map
        elif game_map[row_cor][col_cor+1] == "#":
            return game_map
        elif game_map[row_cor][col_cor+1][-1].isdigit() == True:
            game_map[row_cor][col_cor] = "_"
        else:
            game_map[row_cor][col_cor] = "_"
            game_map[row_cor][col_cor+1] = "P"
    return game_map

def move_choice(move,n):
    if move == "exit":
        return move
    d = {"N":["N","E","W"],"E":["E","S","N"],"S":["S","W","E"],"W":["W","N","S"]}
    return random.choices(population=d[move], weights=[1-n*2,n,n])[0]

def cor_change(game_map, move,row_cor,col_cor):
    if move == "N":
        if (row_cor == 0):
            return row_cor, col_cor
        elif game_map[row_cor-1][col_cor] == "#":
            return row_cor, col_cor
        else:
            row_cor -= 1
    elif move == "S":
        if (row_cor == len(game_map)-1):
            return row_cor, col_cor
        elif game_map[row_cor+1][col_cor] == "#" :
            return row_cor, col_cor
        else:
            row_cor += 1
    elif move == "W":
        if  (col_cor == 0):
            return row_cor, col_cor
        elif game_map[row_cor][col_cor-1] == "#":
            return row_cor, col_cor
        else:
            col_cor -= 1
    elif move == "E":
        if  (col_cor == len(game_map[row_cor])-1):
            return row_cor, col_cor
        elif game_map[row_cor][col_cor+1] == "#":
            return row_cor, col_cor
        else:
            col_cor += 1
    return row_cor, col_cor

#the function returns 1 if it acts randomly, and returns 0 if it acts on the current policy
def episilon_greedy(episilon):
    return_lst = [0,1]
    return random.choices(population=return_lst,weights=[1-episilon,episilon])[0]

#According to the game map, the living reward is -0.01, we can split the value of the sample in two cases:
#return the max Q value of the next grid. 
def sample_value(q_value_dict, actual_move,game_map,row_cor, col_cor,discount,lr,index,reward):
    #seek_row,seek_col refers to the location of s'
    seek_row, seek_col = cor_change(game_map,actual_move,row_cor,col_cor)
    #in order to make the model more risk-averse, we need to modify the weight for winning and losing respectively
    if len(q_value_dict[(seek_row,seek_col)]) == 1 and q_value_dict[(seek_row,seek_col)][0] < 0:
        return (1-lr)*q_value_dict[(row_cor,col_cor)][index]+100*lr*discount*max(q_value_dict[(seek_row,seek_col)])+reward
    return (1-lr)*q_value_dict[(row_cor,col_cor)][index]+lr*discount*max(q_value_dict[(seek_row,seek_col)])+reward

def sigmoid_decay(var,n):
    return (1/(1+0.5*math.exp(-n)))*var

#This is the function that mainly inplements the temporal difference learning
def td_learning(problem):
    discount = float(problem[0])
    noise = float(problem[1])
    reward = float(problem[2])
    #note that this parameter will not be utilized in this question
    num_iter = int(problem[3])
    game_map = problem[4]

    #get the number of rows and columns
    row_num = len(game_map)
    col_num = len(game_map[0])
    
    episilon = 0.08
    epi_decay = 1
    strat_row = 0
    start_col = 0
    #use a dictionary to store the q_value in each grid
    #initialize the value of each grid with 0
    #in order for standardization, actions are ranked as north, west, south, east
    q_value_dict = {}
    lr_dict = {}
    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            lr_dict[(i,j)] = [[0.6,0] for i in range(4)]
            if game_map[i][j][-1].isdigit():
                #store the reward for exitting grid, store the q values otherwise
                q_value_dict[(i,j)] = [float(game_map[i][j])]
            elif game_map[i][j] == "#":
                q_value_dict[(i,j)] = "#"
            else:
                q_value_dict[(i,j)] = [0,0,0,0]
            #take note of the start location
            if game_map[i][j] == "P":
                strat_row = i
                start_col = j
            
    moves = ["N","W","S","E"]
    move = ""
    policy_map = [["N" for i in range(col_num)] for j in range(row_num)]
    policy_store = []
    #this variable keeps track of the time of iteration, which can help with the decay function
    iter_count = 0
    #the loop continues if the policy has not converged
    #Here the converge condition is that the policy is the same as the twentieth last iteration
    #And the iteration time must be no less than 2000 (Adequate samples are needed for temporal difference learning)
    while len(policy_store) < 2000 or policy_store[-1] != policy_store[-10] :
        iter_count += 1
        #restart from the beginning
        cur_row = strat_row
        cur_col = start_col
        #refresh the game map
        game_map_copy = copy.deepcopy(game_map)
        #decrease the learning rate and episilon
        #lr = lr * lr_decay
        #lr = sigmoid_decay(lr,iter_count)
        #episilon = episilon * epi_decay
        episilon = sigmoid_decay(episilon,iter_count)
        #start over if the game ends, till the policy converges
        while not game_end(game_map_copy):
            #skip the grids where the policy is to exit
            #if it is to move according to the policy
            if episilon_greedy(episilon) == 0:
                #if all q values are equal, random select one move
                if q_value_dict[(cur_row,cur_col)].count(q_value_dict[(cur_row,cur_col)][0]) == len(q_value_dict[(cur_row,cur_col)]):
                    move = random.choice(["N","W","S","E"])
                    #move = "N"
                else:
                    for l in range(len(moves)):
                        if q_value_dict[(cur_row,cur_col)][l] == max(q_value_dict[(cur_row,cur_col)]):
                            move = moves[l]
            #if it is to move randomly
            else:
                move = random.choice(["N","W","S","E"])
            #the actual move can be different because of the noise
            actual_move = move_choice(move, noise)
            game_map_copy = generate_successor(game_map_copy,actual_move,cur_row,cur_col)
            for i in range(len(moves)):
                #note that the q value of the intended move(rather than the actual) gets updated
                if moves[i] == move:
                    if len(q_value_dict[(cur_row,cur_col)])>1:
                        #the q value of the last location will be updated according to the supposed move
                        q_value_dict[(cur_row,cur_col)][i] = sample_value(q_value_dict, actual_move,game_map,cur_row, cur_col,discount,lr_dict[(cur_row,cur_col)][i][0],i,reward)
                        lr_dict[(cur_row,cur_col)][i][1] += 1
                        lr_dict[(cur_row,cur_col)][i][0] = sigmoid_decay(lr_dict[(cur_row,cur_col)][i][0],lr_dict[(cur_row,cur_col)][i][1])
            #update the current location till now because it was used to update the q values
            cur_row, cur_col = cor_change(game_map, actual_move,cur_row,cur_col)
            for i in range(len(game_map)):
                for j in range(len(game_map[i])):
                    if game_map[i][j][-1].isdigit():
                        policy_map[i][j] = "x"
                    elif game_map[i][j] == "#":
                        policy_map[i][j] = "#"
                    else:
                        for l in range(len(moves)):
                            if q_value_dict[(i,j)][l] == max(q_value_dict[(i,j)]):
                                policy_map[i][j] = moves[l]
        policy_store.append(policy_map)
    return policy_map

#This is exactly the same problem as parsed in problem 3 testcase 2
problem = ['1', '0.1', '-0.01', '20', [['_', '_', '_', '1'], ['_', '#', '_', '-1'], ['P', '_', '_', '_']]]
#This is the desired or the optimal policy.
solution = [['E', 'E', 'E', 'x'], ['N', '#', 'W', 'x'], ['N', 'W', 'W', 'S']]

#counter counts the number of cases where the trained policy is the same as the desired policy.
counter = 0
for i in range(10):
    if td_learning(problem) == solution:
        counter += 1
print("The optimal solution can be found for",counter,"times out of 10 trials!")
