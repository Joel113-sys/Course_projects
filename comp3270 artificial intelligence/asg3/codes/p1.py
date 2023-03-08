import sys, grader, parse
import random

def game_end(game_map):
    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            if game_map[i][j] == "P":
                return False
    return True

def check_policy(policy_map,row_cor,col_cor):
    return policy_map[row_cor][col_cor]

def move_choice(seed,move,n):
    if move == "exit":
        return move
    d = {"N":["N","E","W"],"E":["E","S","N"],"S":["S","W","E"],"W":["W","N","S"]}
    return random.choices(population=d[move], weights=[1-n*2,n,n])[0]

def generate_successor(game_map,move,row_cor,col_cor,posi_dict,reward):
    if move == "N":
        if (game_map[row_cor-1][col_cor] == "#" or row_cor == 0):
            return game_map,reward,row_cor,col_cor
        else:
            game_map[row_cor-1][col_cor] = "P"
            if (row_cor,col_cor) == posi_dict["start"]:
                game_map[row_cor][col_cor] = "S"
                row_cor -= 1
                
            else:
                game_map[row_cor][col_cor] = "_"
                row_cor -= 1
                
    elif move == "S":
        if (game_map[row_cor+1][col_cor] == "#" or row_cor == len(game_map)-1):
            return game_map,reward,row_cor,col_cor
        else:
            game_map[row_cor+1][col_cor] = "P"
            if (row_cor,col_cor) == posi_dict["start"]:
                game_map[row_cor][col_cor] = "S"
                row_cor += 1
                
            else:
                game_map[row_cor][col_cor] = "_"
                row_cor += 1
                
    elif move == "W":
        if  (game_map[row_cor][col_cor-1] == "#" or col_cor == 0):
            return game_map, reward, row_cor, col_cor
        else:
            game_map[row_cor][col_cor-1] = "P"
            if (row_cor,col_cor) == posi_dict["start"]:
                game_map[row_cor][col_cor] = "S"
                col_cor -= 1
                
            else:
                game_map[row_cor][col_cor] = "_"
                col_cor -= 1
    elif move == "E":
        if  (game_map[row_cor][col_cor+1] == "#" or col_cor == len(game_map[row_cor])-1):
            return game_map, reward, row_cor, col_cor
        else:
            game_map[row_cor][col_cor+1] = "P"
            if (row_cor,col_cor) == posi_dict["start"]:
                game_map[row_cor][col_cor] = "S"
                col_cor += 1
                
            else:
                game_map[row_cor][col_cor] = "_"
                col_cor += 1
    elif move == "exit":
        game_map[row_cor][col_cor] = posi_dict[(row_cor,col_cor)]
        reward = 100*float(posi_dict[(row_cor,col_cor)])
        
    return game_map,reward,row_cor,col_cor

def check_cor(game_map):
    posi_dict = {}
    #take note of the start place for printing later
    start_row_cor = 0
    start_col_cor = 0
    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            if game_map[i][j] == "S":
                posi_dict["start"] = (i,j)
    #take note of the winning position
    win_row_cor = 0
    win_col_cor = 0
    posi_dict["win"] = []
    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            if game_map[i][j].isdigit() == True and game_map[i][j][0] != "-":
                posi_dict["win"].append((i,j))
                posi_dict[(i,j)] = game_map[i][j]
    #take note of the losing position
    lose_row_cor = 0
    lose_col_cor = 0
    posi_dict["lose"] = []
    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            if game_map[i][j][0] == "-":
                posi_dict["lose"].append((i,j))
                posi_dict[(i,j)] = game_map[i][j]
    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            if game_map[i][j][0] == "#":
                posi_dict["wall"] = (i,j)
    return posi_dict


def play_episode(problem):
    seed = int(problem[0])
    if seed != -1:
        random.seed(seed,version= 1)
    noise = float(problem[1])
    reward = float(problem[2])*100
    game_map = problem[3]
    policy_map = problem[4]
    #because of the representation error, multiply the sum by 100 and divide by 100 eventually
    cul_sum = 0
    experience = []
    experience.append("Start state:")
    for i in game_map:
        experience.append("\n")
        for j in i:
            if j == "S":
                experience.append((5-len(j))*" "+"P")
            else:
                experience.append((5-len(j))*" "+j)
    experience.append("\nCumulative reward sum: 0.0")
    posi_dict = check_cor(game_map)
    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            if game_map[i][j] == "S":
                game_map[i][j] = "P"
    #cur_row_cor and cur_col_cor keeps track of the position of "P"
    cur_row_cor = posi_dict["start"][0]
    cur_col_cor = posi_dict["start"][1]
    while True:
        if game_end(game_map):
            break
        experience.append(("\n-------------------------------------------- "))
        policy_move = check_policy(policy_map,cur_row_cor,cur_col_cor)
        actual_move = move_choice(seed,policy_move,noise)
        experience.append("\nTaking action: "+actual_move+" (intended: "+policy_move+")")
        game_map, reward, cur_row_cor, cur_col_cor = generate_successor(game_map,actual_move,cur_row_cor,cur_col_cor,posi_dict,reward)
        experience.append("\nReward received: "+str(reward/100))
        experience.append("\nNew state:")
        for i in game_map:
            experience.append("\n")
            for j in i:
                experience.append((5-len(j))*" "+j)
        cul_sum += reward
        experience.append("\nCumulative reward sum: "+str(cul_sum/100))

    return "".join(experience)

if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    #test_case_id = 1
    problem_id = 1
    grader.grade(problem_id, test_case_id, play_episode, parse.read_grid_mdp_problem_p1)