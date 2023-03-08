import sys, parse, grader

#counter the number of attacks at a certain grid
def counter(problem,a,b,recorded_list):
    #traverse all grids on the board
    for k in range(0,8):
        for l in range(0,8):
            #conditions of attacks
            if (k!=a or l!= b):
                if problem[k][l]==1:
                    if ((abs(a-k)==abs(b-l) or a==k or b==l)):
                        if {(k,l),(a,b)} not in recorded_list:
                            recorded_list.append({(k,l),(a,b)})
    return len(recorded_list)

def better_board(problem):
    #Your p7 code here
    solutionlst = [[0,0,0,0,0,0,0,0] for i in range (0,8)]
    
    #i,j for the coordinate of the grid to be investigated
    for i in range (0,8):
        for j in range(0,8):
            #print(i,j,":")
            temp = [[0,0,0,0,0,0,0,0] for i in range(0,8)]
            for a in range(0,8):
                for b in range(0,8):
                    temp[a][b] = problem[a][b]
            temp[i][j] = 1

            for count in range(0,8):
                if temp[count][j]==1 and count!=i:
                    temp[count][j]=0
            sum=0
            #initialize the list
            lst = []
            for x in range(0,8):
                for y in range(0,8):
                    if temp[x][y]==1:
                        sum += counter(temp,x,y,lst)
            solutionlst[i][j]=len(lst)

    #initialize a new 2-d array
    numsolution = [[0,0,0,0,0,0,0,0] for i in range (0,8)]
    for a in range(0,8):
        for b in range(0,8):
            numsolution[a][b] = problem[a][b]

    #next find the grid with the least number of attacks
    min_num = 64
    x_cor = 0
    y_cor = 0
    for i in range(0,8):
        for j in range(0,8):
            if solutionlst[i][j] < min_num:
                min_num = solutionlst[i][j]
                x_cor = i
                y_cor = j
    
    numsolution[x_cor][y_cor] = 1
    for i in range(0,8):
        for j in range(0,8):
            if x_cor != i and y_cor == j:
                if numsolution[i][j] == 1:
                    numsolution[i][j] = 0

    solution = [list("........") for i in range(0,8)]
    for i in range(0,8):
        for j in range(0,8):
            if numsolution[i][j] == 1:
                solution[i][j] = 'q'

    return " ".join(solution[0])+'\n'+" ".join(solution[1])+'\n'+" ".join(solution[2])+'\n'+" ".join(solution[3])+'\n'+" ".join(solution[4])+'\n'+" ".join(solution[5])+'\n'+" ".join(solution[6])+'\n'+" ".join(solution[7])

if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    problem_id = 7
    grader.grade(problem_id, test_case_id, better_board, parse.read_8queens_search_problem)