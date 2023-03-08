import sys, grader, parse,copy
from tabnanny import check

def check_policy(policy_map,row_cor,col_cor):
    return policy_map[row_cor][col_cor]

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

def policy_evaluation(problem):
    return_value = []
    discount = float(problem[0])
    noise = float(problem[1])
    reward = float(problem[2])
    num_iter = int(problem[3])
    game_map = problem[4]
    policy_map = problem[5]
    #get the number of rows and cols of the map
    row_num = len(game_map)
    col_num = len(game_map[0])
    #initialize a map storing the value of each position
    value_map = [[0.00 for i in range(col_num)] for j in range(row_num)]
    return_value.append("V^pi_k=0")
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
                
                move = check_policy(policy_map,i,j)
                value_map = update_value(value_map, value_map_copy,move,game_map,i, j,reward,noise,discount)
        return_value.append("\nV^pi_k="+str(k+1))
        for i in range(len(value_map)):
            line = "\n"
            for j in range(len(value_map[i])):

                if game_map[i][j] == '#':
                    line += "| ##### |"
                else:
                    line += "|{:7.2f}|".format(float(value_map[i][j]))
            return_value.append(line)

    return "".join(return_value)

if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    #test_case_id = -7
    problem_id = 2
    grader.grade(problem_id, test_case_id, policy_evaluation, parse.read_grid_mdp_problem_p2)