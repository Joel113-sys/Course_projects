import os, sys,re
def read_layout_problem(file_path):
    #Your p1 code here
    #first entry: random seed; second entry: map of the game (stored in an array)
    problem = []
    pacmap = []
    with open(file_path) as f:
        contents = f.readlines()
        problem.append(contents[0].split()[1])
        for i in range(1,len(contents)):
            if contents[i][-2:] == " \n":
                contents[i] = re.sub(r".$","",contents[i])
            pacmap.append(contents[i])
        problem.append(pacmap)
    f.close()
    return problem

if __name__ == "__main__":
    if len(sys.argv) == 3:
        problem_id, test_case_id = sys.argv[1], sys.argv[2]
        problem = read_layout_problem(os.path.join('test_cases','p'+problem_id, test_case_id+'.prob'))
        print(problem)
    else:
        print('Error: I need exactly 2 arguments!')