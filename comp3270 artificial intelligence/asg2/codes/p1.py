import sys, random, grader, parse

from numpy import round_, true_divide

#this function determines if the game has terminated or not, specifically, it needs to determine
#whether it is pacman or ghost that has won
#if it returns true, it implies that pacman wins
#if it returns false, it implies that the ghost wins
def game_end(pacmap):
    food_count = 0
    pacman_count = 0
    for i in range(0,len(pacmap)):
        for j in range(0,len(pacmap[0])-1):
            if pacmap[i][j] == '.' or pacmap[i][j] == 'L':
                food_count += 1
            elif pacmap[i][j] == "P":
                pacman_count += 1
    if food_count == 0:
        return 1
    if pacman_count == 0:
        return 2
    return 0

def take_turn(flag):
    if flag == True:
        return "P"
    else:
        return "W"

def switch_turn(flag):
    if flag == True:
        return False
    else:
        return True

def check_cor(pacmap):
    #find the position of the pacman and the ghost
    for i in range(0,len(pacmap)):
        for j in range(0,len(pacmap[0])-1):
            if pacmap[i][j] == 'P':
                p_xcor = i
                p_ycor = j
            if pacmap[i][j] == 'W' or pacmap[i][j] == 'L':
                w_xcor = i
                w_ycor = j
    return p_xcor, p_ycor, w_xcor, w_ycor

#determine all possible choices of a pacman or a ghost a a certain position (x,y)
def move_choice(xcor,ycor,pacmap):
    choice_lst = []
    if pacmap[xcor-1][ycor] != "%":
        choice_lst.append("N")
    if pacmap[xcor+1][ycor] != "%":
        choice_lst.append("S")
    if pacmap[xcor][ycor-1] != "%":
        choice_lst.append("W")
    if pacmap[xcor][ycor+1] != "%":
        choice_lst.append("E")
    choice_lst = tuple(i for i in choice_lst)
    sorted_tuple = tuple(sorted(choice_lst))
    poped_move = random.choice(sorted_tuple)
    return poped_move

#this functions takes move for the pacman or the ghost, and make changes to the pacmap. the score changes along with different moves
#note a few cases:
#1.a pacman moves to an empty place
#2.a ghost moves to an empty place
#3.a pacman eats a food
#4.a ghost moves above a food, here we denote this case as "L"
#5.a pacman gets eaten by a ghost
def move(entity,xcor,ycor,score,pacmap):
    poped_move = move_choice(xcor,ycor,pacmap)
    if entity == "P":
        score -= 1
        if poped_move == "N":
            if pacmap[xcor-1][ycor] == ".":
                score += 10
                pacmap[xcor-1][ycor] = "P"
                pacmap[xcor][ycor] = " "
                if game_end(pacmap):
                    score += 500
            elif pacmap[xcor-1][ycor] == "W":
                score -= 500
                pacmap[xcor][ycor] = " "
            elif pacmap[xcor-1][ycor] == " ":
                pacmap[xcor-1][ycor] = "P"
                pacmap[xcor][ycor] = " "
            elif pacmap[xcor-1][ycor] == "L":
                pacmap[xcor][ycor] = " "
                score -= 500
        if poped_move == "S":
            if pacmap[xcor+1][ycor] == ".":
                score += 10
                pacmap[xcor+1][ycor] = "P"
                pacmap[xcor][ycor] = " "
                if game_end(pacmap):
                    score += 500
            elif pacmap[xcor+1][ycor] == "W":
                score -= 500
                pacmap[xcor][ycor] = " "
            elif pacmap[xcor+1][ycor] == " ":
                pacmap[xcor+1][ycor] = "P"
                pacmap[xcor][ycor] = " "
            elif pacmap[xcor+1][ycor] == "L":
                pacmap[xcor][ycor] = " "
                score -= 500
        if poped_move == "W":
            if pacmap[xcor][ycor-1] == ".":
                score += 10
                pacmap[xcor][ycor-1] = "P"
                pacmap[xcor][ycor] = " "
                if game_end(pacmap):
                    score += 500
            elif pacmap[xcor][ycor-1] == "W":
                score -= 500
                pacmap[xcor][ycor] = " "
            elif pacmap[xcor][ycor-1] == " ":
                pacmap[xcor][ycor-1] = "P"
                pacmap[xcor][ycor] = " "
            elif pacmap[xcor][ycor-1] == "L":
                score -= 500
                pacmap[xcor][ycor] = " "
        if poped_move == "E":
            if pacmap[xcor][ycor+1] == ".":
                score += 10
                pacmap[xcor][ycor+1] = "P"
                pacmap[xcor][ycor] = " "
                if game_end(pacmap):
                    score += 500
            elif pacmap[xcor][ycor+1] == "W":
                score -= 500
                pacmap[xcor][ycor] = " "
            elif pacmap[xcor][ycor+1] == " ":
                pacmap[xcor][ycor+1] = "P"
                pacmap[xcor][ycor] = " "
            elif pacmap[xcor][ycor+1] == "L":
                score -= 500
                pacmap[xcor][ycor] = " "
    if entity == "W":
        if poped_move == "N":
            if pacmap[xcor-1][ycor] == ".":
                if pacmap[xcor][ycor] == "L":
                    pacmap[xcor-1][ycor] = "L"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor-1][ycor] = "L"
                    pacmap[xcor][ycor] = " "
            elif pacmap[xcor-1][ycor] == "P":
                if pacmap[xcor][ycor] == "L":
                    pacmap[xcor][ycor] = "."
                    pacmap[xcor-1][ycor] = "W"
                else:
                    pacmap[xcor][ycor] = " "
                    pacmap[xcor-1][ycor] = "W"
                score -= 500
            elif pacmap[xcor-1][ycor] == " ":
                if pacmap[xcor][ycor] == "L":
                    pacmap[xcor-1][ycor] = "W"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor-1][ycor] = "W"
                    pacmap[xcor][ycor] = " "
        if poped_move == "S":
            if pacmap[xcor+1][ycor] == ".":
                if pacmap[xcor][ycor] == "L":
                    pacmap[xcor+1][ycor] = "L"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor+1][ycor] = "L"
                    pacmap[xcor][ycor] = " "
            elif pacmap[xcor+1][ycor] == "P":
                if pacmap[xcor][ycor] == "L":
                    pacmap[xcor][ycor] = "."
                    pacmap[xcor+1][ycor] = "W"
                else:
                    pacmap[xcor][ycor] = " "
                    pacmap[xcor+1][ycor] = "W"
                score -= 500
            elif pacmap[xcor+1][ycor] == " ":
                if pacmap[xcor][ycor] == "L":
                    pacmap[xcor+1][ycor] = "W"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor+1][ycor] = "W"
                    pacmap[xcor][ycor] = " "
        if poped_move == "W":
            if pacmap[xcor][ycor-1] == ".":
                if pacmap[xcor][ycor] == "L":
                    pacmap[xcor][ycor-1] = "L"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor][ycor-1] = "L"
                    pacmap[xcor][ycor] = " "
            elif pacmap[xcor][ycor-1] == "P":
                if pacmap[xcor][ycor] == "L":
                    pacmap[xcor][ycor] = "."
                    pacmap[xcor][ycor-1] = "W"
                else:
                    pacmap[xcor][ycor] = " "
                    pacmap[xcor][ycor-1] = "W"
                score -= 500
            elif pacmap[xcor][ycor-1] == " ":
                if pacmap[xcor][ycor] == "L":
                    pacmap[xcor][ycor-1] = "W"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor][ycor-1] = "W"
                    pacmap[xcor][ycor] = " "
        if poped_move == "E":
            if pacmap[xcor][ycor+1] == ".":
                if pacmap[xcor][ycor] == "L":
                    pacmap[xcor][ycor+1] = "L"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor][ycor+1] = "L"
                    pacmap[xcor][ycor] = " "
            elif pacmap[xcor][ycor+1] == "P":
                if pacmap[xcor][ycor] == "L":
                    pacmap[xcor][ycor] = "."
                    pacmap[xcor][ycor+1] = "W"
                else:
                    pacmap[xcor][ycor] = " "
                    pacmap[xcor][ycor+1] = "W"
                score -= 500
            elif pacmap[xcor][ycor+1] == " ":
                if pacmap[xcor][ycor] == "L":
                    pacmap[xcor][ycor+1] = "W"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor][ycor+1] = "W"
                    pacmap[xcor][ycor] = " "
    move_des = entity+" moving "+poped_move
    return score,pacmap,move_des

def random_play_single_ghost(problem):
    #Your p1 code here
    solution = []
    solution.append("seed: "+problem[0]+"\n")
    solution.append("0\n")
    for i in problem[1]:
        solution.append(i)
    seed = problem[0]
    random.seed(int(seed),version = 1)
    round_num = 0
    pacmap_str = problem[1]
    pacmap = []
    for i in pacmap_str:
        pacmap.append([j for j in i])
    score = 0
    entity = "P"
    flag = True
    move_des = ""

    while game_end(pacmap) == 0:
        entity = take_turn(flag)
        pacman_x, pacman_y, ghost_x, ghost_y = check_cor(pacmap)
        if flag:
            score,pacmap,move_des = move(entity,pacman_x,pacman_y,score,pacmap)
        else:
            score,pacmap,move_des = move(entity,ghost_x,ghost_y,score,pacmap)
        flag = switch_turn(flag)
        round_num += 1
        solution.append("\n"+str(round_num)+": "+move_des+"\n")
        printpacmap = [row[:] for row in pacmap]
        for i in range(0,len(printpacmap)):
            for j in range(0,len(printpacmap[0])-1):
                if printpacmap[i][j] == "L":
                    printpacmap[i][j] = "W"
        for i in printpacmap:
            solution.append("".join(i))
        solution.append("\nscore: "+str(score))
    
    if game_end(pacmap) == 1:
        solution.append("\nWIN: Pacman")
    else:
        solution.append("\nWIN: Ghost")
    return "".join(solution)

if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    problem_id = 1
    grader.grade(problem_id, test_case_id, random_play_single_ghost, parse.read_layout_problem)