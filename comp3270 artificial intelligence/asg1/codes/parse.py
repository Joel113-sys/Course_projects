import os, sys

#For q1-q5, I will put the problem set in lists, where the first entry stores the start state, the second entry marks the goal state, and the third entry is a
#dictionary which keeps track of all the connectivity of different nodes and the cost to go to another node; what's more, the fourth entry is another dictionary 
#that stores the heuristic values of all nodes, while the fourth entry is another state space graph.
def read_graph_search_problem(file_path):
    #Your p1 code here
    problem = []
    dict1={}
    dict2={}
    dict3={}
    with open(file_path) as f:
        contents = f.readlines()
        problem.append(contents[0].split()[1])
        goal_lst = []
        for i in range(1,len(contents[1].split())):
            goal_lst.append(contents[1].split()[i])
        problem.append(goal_lst)
        for i in range (2,len(contents)):
            if len(contents[i].split()) == 2:
                dict2[contents[i].split()[0]]=float(contents[i].split()[1])
            elif len(contents[i].split()) == 3:
                if contents[i].split()[0] not in dict1:
                    dict1[contents[i].split()[0]]=[(float(contents[i].split()[2]),contents[i].split()[1])]                
                else:
                    dict1[contents[i].split()[0]].append((float(contents[i].split()[2]),contents[i].split()[1]))                 

                if contents[i].split()[0] not in dict3:
                    dict3[contents[i].split()[0]]=[contents[i].split()[1]]
                elif contents[i].split()[1] not in dict3[contents[i].split()[0]]:
                    dict3[contents[i].split()[0]].append(contents[i].split()[1])

        problem.append(dict1)
        problem.append(dict2)
        problem.append(dict3)
    f.close()
    return problem

def read_8queens_search_problem(file_path):
    #Your p6 code here
    with open(file_path) as f:
        contents = f.readlines()
        problem = [[0,0,0,0,0,0,0,0] for i in range (0,8)]
        for i in range(0,8):
            for j in range(0,8):
                    if contents[i][j*2]=='q':
                        problem[i][j]=1
    f.close()
    return problem

if __name__ == "__main__":
    if len(sys.argv) == 3:
        problem_id, test_case_id = sys.argv[1], sys.argv[2]
        if int(problem_id) <= 5:
            problem = read_graph_search_problem(os.path.join('test_cases','p'+problem_id, test_case_id+'.prob'))
        else:
            problem = read_8queens_search_problem(os.path.join('test_cases','p'+problem_id, test_case_id+'.prob'))
        print(problem)
    else:
        print('Error: I need exactly 2 arguments!')