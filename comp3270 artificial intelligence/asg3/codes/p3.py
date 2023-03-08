import sys, grader, parse,copy,math

def update_value(value_map,value_map_copy,move,game_map,row_cor, col_cor,living_reward,noise,discount):
    reward = get_reward(game_map,row_cor,col_cor)
    if move == "N":
        value_map[row_cor][col_cor] = (1-2*noise)*(reward+discount*get_value(value_map_copy, game_map, move, row_cor, col_cor))+noise*(reward+discount*get_value(value_map_copy, game_map, "W", row_cor, col_cor))+noise*(reward+discount*get_value(value_map_copy, game_map, "E", row_cor, col_cor))+living_reward
    elif move == "S":
        value_map[row_cor][col_cor] = (1-2*noise)*(reward+discount*get_value(value_map_copy, game_map, move, row_cor, col_cor))+noise*(reward+discount*get_value(value_map_copy, game_map, "W", row_cor, col_cor))+noise*(reward+discount*get_value(value_map_copy, game_map, "E", row_cor, col_cor))+living_reward
    elif move == "W":
        value_map[row_cor][col_cor] = (1-2*noise)*(reward+discount*get_value(value_map_copy, game_map, move, row_cor, col_cor))+noise*(reward+discount*get_value(value_map_copy, game_map, "N", row_cor, col_cor))+noise*(reward+discount*get_value(value_map_copy, game_map, "S", row_cor, col_cor))+living_reward
    elif move == "E":
        value_map[row_cor][col_cor] = (1-2*noise)*(reward+discount*get_value(value_map_copy, game_map, move, row_cor, col_cor))+noise*(reward+discount*get_value(value_map_copy, game_map, "N", row_cor, col_cor))+noise*(reward+discount*get_value(value_map_copy, game_map, "S", row_cor, col_cor))+living_reward
    elif move == "exit":
        value_map[row_cor][col_cor] = reward
    return value_map

def get_reward(game_map,row_cor,col_cor):
    if game_map[row_cor][col_cor][-1].isdigit():
        return float(game_map[row_cor][col_cor])
    return 0

def get_value(value_map, game_map, move, row_cor, col_cor):
    if move == "N":
        if row_cor == 0 or game_map[row_cor-1][col_cor] == "#":
            return value_map[row_cor][col_cor]
        else:
            return value_map[row_cor-1][col_cor]
    elif move == "S":
        if row_cor == len(game_map)-1 or game_map[row_cor+1][col_cor] == "#":
            return value_map[row_cor][col_cor]
        else:
            return value_map[row_cor+1][col_cor]
    elif move == "W":
        if col_cor == 0 or game_map[row_cor][col_cor-1] == "#":
            return value_map[row_cor][col_cor]
        else:
            return value_map[row_cor][col_cor-1]
    elif move == "E":
        if col_cor == len(game_map[0])-1 or game_map[row_cor][col_cor+1] == "#":
            return value_map[row_cor][col_cor]
        else:
            return value_map[row_cor][col_cor+1]
    elif move == "exit":
        return 0

def temp_value(value_map,value_map_copy,move,game_map,row_cor, col_cor,living_reward,noise,discount):
    reward = get_reward(game_map,row_cor,col_cor)
    if not game_map[row_cor][col_cor][-1].isdigit():
        if move == "N":
            return (1-2*noise)*(reward+discount*get_value(value_map_copy, game_map, move, row_cor, col_cor))+noise*(reward+discount*get_value(value_map_copy, game_map, "W", row_cor, col_cor))+noise*(reward+discount*get_value(value_map_copy, game_map, "E", row_cor, col_cor))+living_reward
        elif move == "S":
            return (1-2*noise)*(reward+discount*get_value(value_map_copy, game_map, move, row_cor, col_cor))+noise*(reward+discount*get_value(value_map_copy, game_map, "W", row_cor, col_cor))+noise*(reward+discount*get_value(value_map_copy, game_map, "E", row_cor, col_cor))+living_reward
        elif move == "W":
            return (1-2*noise)*(reward+discount*get_value(value_map_copy, game_map, move, row_cor, col_cor))+noise*(reward+discount*get_value(value_map_copy, game_map, "N", row_cor, col_cor))+noise*(reward+discount*get_value(value_map_copy, game_map, "S", row_cor, col_cor))+living_reward
        elif move == "E":
            return (1-2*noise)*(reward+discount*get_value(value_map_copy, game_map, move, row_cor, col_cor))+noise*(reward+discount*get_value(value_map_copy, game_map, "N", row_cor, col_cor))+noise*(reward+discount*get_value(value_map_copy, game_map, "S", row_cor, col_cor))+living_reward
        return -math.inf
    else:
        if move == "exit":
            return reward
        return -math.inf
        
#this essentiailly works like a more sophisticated policy evaluation
def value_iteration(problem):
    return_value = []
    discount = float(problem[0])
    noise = float(problem[1])
    reward = float(problem[2])
    num_iter = int(problem[3])
    game_map = problem[4]
    #get the number of rows and cols of the map
    row_num = len(game_map)
    col_num = len(game_map[0])
    moves = ["N","E","S","W","exit"]
    #initialize a value map and a policy map
    value_map = [[0.00 for i in range(col_num)] for j in range(row_num)]
    policy_map = [["N" for i in range(col_num)] for j in range(row_num)]
    return_value.append("V_k=0")
    for i in range(len(value_map)):
        line = "\n"
        for j in range(len(value_map[i])):
            if game_map[i][j] == '#':
                line += "| ##### |"
            else:
                line += "|{:7.2f}|".format(float(value_map[i][j]))
        return_value.append(line)
    for k in range(num_iter-1):
        value_map_copy = copy.deepcopy(value_map)
        #for all grid on the map, do value updates
        for i in range(len(game_map)):
            for j in range(len(game_map[i])):
                value_list = []
                for move in moves:
                    value_list.append(temp_value(value_map, value_map_copy,move,game_map,i, j,reward,noise,discount))
                if value_list.count(value_list[0]) == len(value_list):
                    value_map = update_value(value_map, value_map_copy,moves[0],game_map,i, j,reward,noise,discount)
                    policy_map[i][j] = moves[0]
                else:
                    idx = value_list.index(max(value_list))
                    value_map = update_value(value_map, value_map_copy,moves[idx],game_map,i, j,reward,noise,discount)
                    policy_map[i][j] = moves[idx]
        return_value.append("\nV_k="+str(k+1))
        for i in range(len(value_map)):
            line = "\n"
            for j in range(len(value_map[i])):
                if game_map[i][j] == '#':
                    line += "| ##### |"
                else:
                    line += "|{:7.2f}|".format(float(value_map[i][j]))
            return_value.append(line)
        return_value.append("\npi_k="+str(k+1))
        for i in range(len(policy_map)):
            line = "\n"
            for j in range(len(policy_map[i])):
                if game_map[i][j] == '#':
                    line += "| # |"
                else:
                    if policy_map[i][j] == "exit":
                        line += "| "+"x"+" |"
                    else:
                        line += "| "+str(policy_map[i][j])+" |"
            return_value.append(line)
    return "".join(return_value)

if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    #test_case_id = -4
    problem_id = 3
    grader.grade(problem_id, test_case_id, value_iteration, parse.read_grid_mdp_problem_p3)