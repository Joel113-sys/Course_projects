def read_grid_mdp_problem_p1(file_path):
    #Your p1 code here
    #position 0: seed; position 1: noise; position 2: living reward;position 3: game map; position 4: policy map
    problem = []
    game_map = []
    policy_map = []
    with open(file_path) as f:
        contents = f.readlines()
        for i in range(3):
            problem.append(contents[i].split()[1])
        #get the number of rows of the gamemap
        #since case 7 and 8 have empty lines at the end
        num_empty_lines = 0
        for i in contents:
            if i.isspace():
                num_empty_lines += 1
        map_len = len(contents)
        #index is the length of the map
        index = int((map_len-5-num_empty_lines)/2)
        for i in range(4,4+index):
            game_map.append(contents[i].split())
        for i in range(index+5,len(contents)-num_empty_lines):
            policy_map.append(contents[i].split())
        problem.append(game_map)
        problem.append(policy_map)
    f.close()
    return problem

def read_grid_mdp_problem_p2(file_path):
    #Your p2 code here
        #position 0: discount; position 1: noise; position 2: living reward;position3: number of iterations;
        #position 4: game map; position 5: policy map
    problem = []
    game_map = []
    policy_map = []
    with open(file_path) as f:
        contents = f.readlines()
        for i in range(4):
            problem.append(contents[i].split()[1])
        #get the number of rows of the gamemap
        #since case 7 and 8 have empty lines at the end
        num_empty_lines = 0
        for i in contents:
            if i.isspace():
                num_empty_lines += 1
        map_len = len(contents)
        #index is the length of the map
        index = int((map_len-6-num_empty_lines)/2)
        for i in range(5,5+index):
            game_map.append(contents[i].split())
        for i in range(index+6,len(contents)-num_empty_lines):
            policy_map.append(contents[i].split())
        problem.append(game_map)
        problem.append(policy_map)
    f.close()
    return problem

def read_grid_mdp_problem_p3(file_path):
    #Your p3 code here
    problem = []
    game_map = []
    with open(file_path) as f:
        contents = f.readlines()
        for i in range(4):
            problem.append(contents[i].split()[1])
        for i in range(5,len(contents)):
            game_map.append(contents[i].split())
        problem.append(game_map)
    f.close()
    return problem

