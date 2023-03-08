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


def number_of_attacks(problem):
    #Your p6 code here
    solution = [[0,0,0,0,0,0,0,0] for i in range (0,8)]
    
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
            lst = []
            for x in range(0,8):
                for y in range(0,8):
                    if temp[x][y]==1:
                        sum += counter(temp,x,y,lst)
            solution[i][j]=len(lst)

    for index1 in range(0,8):
        for index2 in range(0,8):
            solution[index1][index2] = str(solution[index1][index2])

    storer = []

    for row in solution:
        storer.append('{:^3s}{:^3s}{:^3s}{:^3s}{:^3s}{:^3s}{:^3s}{:>2s}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

    return storer[0]+"\n"+storer[1]+"\n"+storer[2]+"\n"+storer[3]+"\n"+storer[4]+"\n"+storer[5]+"\n"+storer[6]+"\n"+storer[7]


if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    problem_id = 6
    grader.grade(problem_id, test_case_id, number_of_attacks, parse.read_8queens_search_problem)