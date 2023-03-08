import sys, parse,random

import math
import time, os, copy

#this function determines if the game has terminated or not, specifically, it needs to determine
#whether it is pacman or ghost that has won
#if it returns 1, it implies that pacman wins
#if it returns 2, it implies that the ghost wins
#if it returns 0, the game isn't over yet
def game_end(pacmap):
    food_count = 0
    pacman_count = 0
    for i in range(0,len(pacmap)):
        for j in range(0,len(pacmap[-1])-1):
            if pacmap[i][j] == '.' or pacmap[i][j][-1] == "L":
                food_count += 1
            elif pacmap[i][j] == "P":
                pacman_count += 1
    if food_count == 0:
        return 1
    if pacman_count == 0:
        return 2
    return 0

def take_turn(round_num,factor):
    if round_num % factor == 0:
        return "P"
    elif round_num % factor == 1:
        return "W"
    elif round_num % factor == 2:
        return "X"
    elif round_num % factor == 3:
        return "Y"
    elif round_num % factor == 4:
        return "Z"

def switch_turn(flag):
    if flag == True:
        return False
    else:
        return True

def check_ghost_num(pacmap):
    counter = 0
    for i in range(0,len(pacmap)):
        for j in range(0,len(pacmap[1])-1):
            if pacmap[i][j] == 'W' or pacmap[i][j] == 'X' or pacmap[i][j] == 'Y' or pacmap[i][j] == 'Z':
                counter += 1
    return counter

def check_cor(pacmap):
    #find the position of the pacman and the ghost
    g_xcor = []
    g_ycor = []
    g_dict = {}
    label = []
    for i in range(0,len(pacmap)):
        for j in range(0,len(pacmap[-1])-1):
            if pacmap[i][j] == 'P':
                p_xcor = i
                p_ycor = j
            if pacmap[i][j] == 'W' or pacmap[i][j] == 'X' or pacmap[i][j] == 'Y' or pacmap[i][j] == 'Z':
                g_dict[pacmap[i][j]] = (i,j)
            if pacmap[i][j][-1] == "L":
                g_dict[pacmap[i][j][0]] = (i,j)

                #g_xcor.append(i)
                #g_ycor.append(j)


    return p_xcor, p_ycor, g_dict

#determine all possible choices of a pacman or a ghost a a certain position (x,y)
def random_move_choice(entity,xcor,ycor,pacmap):
    choice_lst = []
    if entity == "P":
        if pacmap[xcor-1][ycor] != "%":
            choice_lst.append("N")
        if pacmap[xcor+1][ycor] != "%":
            choice_lst.append("S")
        if pacmap[xcor][ycor-1] != "%":
            choice_lst.append("W")
        if pacmap[xcor][ycor+1] != "%":
            choice_lst.append("E")
    else:
        if pacmap[xcor-1][ycor] != "%" and pacmap[xcor-1][ycor] != "W" and pacmap[xcor-1][ycor] != "X" and pacmap[xcor-1][ycor] != "Y" and pacmap[xcor-1][ycor] != "Z" and pacmap[xcor-1][ycor][-1]!= "L":
            choice_lst.append("N")
        if pacmap[xcor+1][ycor] != "%" and pacmap[xcor+1][ycor] != "W" and pacmap[xcor+1][ycor] != "X" and pacmap[xcor+1][ycor] != "Y" and pacmap[xcor+1][ycor] != "Z" and pacmap[xcor+1][ycor][-1]!= "L":
            choice_lst.append("S")
        if pacmap[xcor][ycor-1] != "%" and pacmap[xcor][ycor-1] != "W" and pacmap[xcor][ycor-1] != "X" and pacmap[xcor][ycor-1] != "Y" and pacmap[xcor][ycor-1] != "Z" and pacmap[xcor][ycor-1][-1]!= "L":
            choice_lst.append("W")
        if pacmap[xcor][ycor+1] != "%" and pacmap[xcor][ycor+1] != "W" and pacmap[xcor][ycor+1] != "X" and pacmap[xcor][ycor+1] != "Y" and pacmap[xcor][ycor+1] != "Z" and pacmap[xcor][ycor+1][-1]!= "L":
            choice_lst.append("E")
    choice_lst = tuple(i for i in choice_lst)
    sorted_tuple = tuple(sorted(choice_lst))
    if len(sorted_tuple) == 0:
        return ""
    else:
        poped_move = random.choice(sorted_tuple)
        return poped_move

#this function calculates the distance of two objects
def cal_dist(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

#the evaluation function needs to be modified to accomodate the case where there are multiple ghosts
def eval_func(xcor,ycor,pacmap):
    if game_end(pacmap) == 1:
        return math.inf
    if game_end(pacmap) == 2:
        return -math.inf

    #find the coordinates of foods and ghosts
    food_x = []
    food_y = []
    ghost_x = []
    ghost_y = []
    for i in range(0,len(pacmap)):
        for j in range(0,len(pacmap[-1])-1):
            if pacmap[i][j] == "." or pacmap[i][j][-1] == "L" :
                food_x.append(i)
                food_y.append(j)
            if pacmap[i][j] == 'W' or pacmap[i][j] == 'X' or pacmap[i][j] == 'Y' or pacmap[i][j] == 'Z' or pacmap[i][j][-1] == "L":
                ghost_x.append(i)
                ghost_y.append(j)

    sum_dist = 0
    #find the sum of distance between the pacman and all ghosts
    for i in range(0,len(ghost_x)):
        sum_dist += cal_dist(xcor,ycor,ghost_x[i],ghost_y[i])


    #find the index of the closest food that is not below ghosts
    idx_food = 0
    min_dist_food = math.inf
    for i in range(0,len(food_x)):
        if min_dist_food > cal_dist(xcor,ycor,food_x[i],food_y[i]):
            if pacmap[food_x[i]][food_y[i]][-1]!="L":
                min_dist_food = cal_dist(xcor,ycor,food_x[i],food_y[i])
                idx_food = i

    #define a ghost_score, which increases as the distance from the pacman and the ghost decreases
    #it is the value of the sum of 1/distance from the pacman to the ghost
    ghost_score = 0
    ghost_dist = 0
    for i in range(0,len(ghost_x)):
        ghost_dist += cal_dist(xcor,ycor,ghost_x[i],ghost_y[i])
        if cal_dist(xcor,ycor,ghost_x[i],ghost_y[i]) <= 3:
            ghost_score += 100/(cal_dist(xcor,ycor,ghost_x[i],ghost_y[i])-0.8)
    if len(food_y) == 0:
        return math.inf
    #score = 10*cal_dist(xcor,ycor,ghost_x[idx],ghost_y[idx])+sum_dist+10*sum(weight)+5*cal_dist(xcor,ycor,food_x[idx_food],food_y[idx_food])
    score = -10*cal_dist(xcor,ycor,food_x[idx_food],food_y[idx_food])+(2000/(len(food_y)-0.6))-ghost_score+10*ghost_dist
    return score

#this function determines a better move than random ones by adopting evaluating functions
def better_move(xcor,ycor,pacmap):
    #find all possible moves first
    choice_lst = []
    if pacmap[xcor-1][ycor] != "%":
        choice_lst.append("N")
    if pacmap[xcor+1][ycor] != "%":
        choice_lst.append("S")
    if pacmap[xcor][ycor-1] != "%":
        choice_lst.append("W")
    if pacmap[xcor][ycor+1] != "%":
        choice_lst.append("E")
    score_lst = []
    for i in choice_lst:
        if i == "N":
            pacmap_copy = copy.deepcopy(pacmap)
            successor,score_in = generate_successor(pacmap_copy,"P",xcor,ycor,"N",0)
            score_lst.append(eval_func(xcor-1,ycor,successor))
        elif i == "S":
            pacmap_copy = copy.deepcopy(pacmap)
            successor,score_in = generate_successor(pacmap_copy,"P",xcor,ycor,"S",0)
            score_lst.append(eval_func(xcor+1,ycor,successor))
        elif i == "W":
            pacmap_copy = copy.deepcopy(pacmap)
            successor,score_in = generate_successor(pacmap_copy,"P",xcor,ycor,"W",0)
            score_lst.append(eval_func(xcor,ycor-1,successor))
        elif i == "E":
            pacmap_copy = copy.deepcopy(pacmap)
            successor,score_in = generate_successor(pacmap_copy,"P",xcor,ycor,"E",0)
            score_lst.append(eval_func(xcor,ycor+1,successor))
    #return the move which has the highest evaluation score
    return choice_lst[score_lst.index(max(score_lst))]

#this function generates a successor of the last state based on the action
def generate_successor(pacmap,entity,xcor,ycor,poped_move,score):
    if entity == "P":
        score -= 1
        if poped_move == "N":
            if pacmap[xcor-1][ycor] == ".":
                score += 10
                pacmap[xcor-1][ycor] = "P"
                pacmap[xcor][ycor] = " "
                if game_end(pacmap):
                    score += 500
            elif pacmap[xcor-1][ycor] == "W" or pacmap[xcor-1][ycor] == "X" or pacmap[xcor-1][ycor] == "Y" or pacmap[xcor-1][ycor] == "Z":
                score -= 500
                pacmap[xcor][ycor] = " "
            elif pacmap[xcor-1][ycor] == " ":
                pacmap[xcor-1][ycor] = "P"
                pacmap[xcor][ycor] = " "
            elif pacmap[xcor-1][ycor][-1] == "L":
                pacmap[xcor][ycor] = " "
                score -= 500
        if poped_move == "S":
            if pacmap[xcor+1][ycor] == ".":
                score += 10
                pacmap[xcor+1][ycor] = "P"
                pacmap[xcor][ycor] = " "
                if game_end(pacmap):
                    score += 500
            elif pacmap[xcor+1][ycor] == "W" or pacmap[xcor+1][ycor] == "X" or pacmap[xcor+1][ycor] == "Y" or pacmap[xcor+1][ycor] == "Z":
                score -= 500
                pacmap[xcor][ycor] = " "
            elif pacmap[xcor+1][ycor] == " ":
                pacmap[xcor+1][ycor] = "P"
                pacmap[xcor][ycor] = " "
            elif pacmap[xcor+1][ycor][-1] == "L":
                pacmap[xcor][ycor] = " "
                score -= 500
        if poped_move == "W":
            if pacmap[xcor][ycor-1] == ".":
                score += 10
                pacmap[xcor][ycor-1] = "P"
                pacmap[xcor][ycor] = " "
                if game_end(pacmap):
                    score += 500
            elif pacmap[xcor][ycor-1] == "W" or pacmap[xcor][ycor-1] == "X" or pacmap[xcor][ycor-1] == "Y" or pacmap[xcor][ycor-1] == "Z":
                score -= 500
                pacmap[xcor][ycor] = " "
            elif pacmap[xcor][ycor-1] == " ":
                pacmap[xcor][ycor-1] = "P"
                pacmap[xcor][ycor] = " "
            elif pacmap[xcor][ycor-1][-1] == "L":
                score -= 500
                pacmap[xcor][ycor] = " "
        if poped_move == "E":
            if pacmap[xcor][ycor+1] == ".":
                score += 10
                pacmap[xcor][ycor+1] = "P"
                pacmap[xcor][ycor] = " "
                if game_end(pacmap):
                    score += 500
            elif pacmap[xcor][ycor+1] == "W" or pacmap[xcor][ycor+1] == "X" or pacmap[xcor][ycor+1] == "Y" or pacmap[xcor][ycor+1] == "Z":
                score -= 500
                pacmap[xcor][ycor] = " "
            elif pacmap[xcor][ycor+1] == " ":
                pacmap[xcor][ycor+1] = "P"
                pacmap[xcor][ycor] = " "
            elif pacmap[xcor][ycor+1][-1] == "L":
                score -= 500
                pacmap[xcor][ycor] = " "
    if entity == "W":
        if poped_move == "N":
            if pacmap[xcor-1][ycor] == ".":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor-1][ycor] = "WL"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor-1][ycor] = "WL"
                    pacmap[xcor][ycor] = " "
            elif pacmap[xcor-1][ycor] == "P":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor] = "."
                    pacmap[xcor-1][ycor] = "W"
                else:
                    pacmap[xcor][ycor] = " "
                    pacmap[xcor-1][ycor] = "W"
                score -= 500
            elif pacmap[xcor-1][ycor] == " ":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor-1][ycor] = "W"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor-1][ycor] = "W"
                    pacmap[xcor][ycor] = " "
        if poped_move == "S":
            if pacmap[xcor+1][ycor] == ".":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor+1][ycor] = "WL"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor+1][ycor] = "WL"
                    pacmap[xcor][ycor] = " "
            elif pacmap[xcor+1][ycor] == "P":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor] = "."
                    pacmap[xcor+1][ycor] = "W"
                else:
                    pacmap[xcor][ycor] = " "
                    pacmap[xcor+1][ycor] = "W"
                score -= 500
            elif pacmap[xcor+1][ycor] == " ":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor+1][ycor] = "W"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor+1][ycor] = "W"
                    pacmap[xcor][ycor] = " "
        if poped_move == "W":
            if pacmap[xcor][ycor-1] == ".":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor-1] = "WL"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor][ycor-1] = "WL"
                    pacmap[xcor][ycor] = " "
            elif pacmap[xcor][ycor-1] == "P":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor] = "."
                    pacmap[xcor][ycor-1] = "W"
                else:
                    pacmap[xcor][ycor] = " "
                    pacmap[xcor][ycor-1] = "W"
                score -= 500
            elif pacmap[xcor][ycor-1] == " ":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor-1] = "W"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor][ycor-1] = "W"
                    pacmap[xcor][ycor] = " "
        if poped_move == "E":
            if pacmap[xcor][ycor+1] == ".":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor+1] = "WL"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor][ycor+1] = "WL"
                    pacmap[xcor][ycor] = " "
            elif pacmap[xcor][ycor+1] == "P":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor] = "."
                    pacmap[xcor][ycor+1] = "W"
                else:
                    pacmap[xcor][ycor] = " "
                    pacmap[xcor][ycor+1] = "W"
                score -= 500
            elif pacmap[xcor][ycor+1] == " ":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor+1] = "W"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor][ycor+1] = "W"
                    pacmap[xcor][ycor] = " "
    if entity == "X":
        if poped_move == "N":
            if pacmap[xcor-1][ycor] == ".":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor-1][ycor] = "XL"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor-1][ycor] = "XL"
                    pacmap[xcor][ycor] = " "
            elif pacmap[xcor-1][ycor] == "P":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor] = "."
                    pacmap[xcor-1][ycor] = "X"
                else:
                    pacmap[xcor][ycor] = " "
                    pacmap[xcor-1][ycor] = "X"
                score -= 500
            elif pacmap[xcor-1][ycor] == " ":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor-1][ycor] = "X"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor-1][ycor] = "X"
                    pacmap[xcor][ycor] = " "
        if poped_move == "S":
            if pacmap[xcor+1][ycor] == ".":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor+1][ycor] = "XL"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor+1][ycor] = "XL"
                    pacmap[xcor][ycor] = " "
            elif pacmap[xcor+1][ycor] == "P":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor] = "."
                    pacmap[xcor+1][ycor] = "X"
                else:
                    pacmap[xcor][ycor] = " "
                    pacmap[xcor+1][ycor] = "X"
                score -= 500
            elif pacmap[xcor+1][ycor] == " ":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor+1][ycor] = "X"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor+1][ycor] = "X"
                    pacmap[xcor][ycor] = " "
        if poped_move == "W":
            if pacmap[xcor][ycor-1] == ".":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor-1] = "XL"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor][ycor-1] = "XL"
                    pacmap[xcor][ycor] = " "
            elif pacmap[xcor][ycor-1] == "P":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor] = "."
                    pacmap[xcor][ycor-1] = "X"
                else:
                    pacmap[xcor][ycor] = " "
                    pacmap[xcor][ycor-1] = "X"
                score -= 500
            elif pacmap[xcor][ycor-1] == " ":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor-1] = "X"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor][ycor-1] = "X"
                    pacmap[xcor][ycor] = " "
        if poped_move == "E":
            if pacmap[xcor][ycor+1] == ".":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor+1] = "XL"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor][ycor+1] = "XL"
                    pacmap[xcor][ycor] = " "
            elif pacmap[xcor][ycor+1] == "P":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor] = "."
                    pacmap[xcor][ycor+1] = "X"
                else:
                    pacmap[xcor][ycor] = " "
                    pacmap[xcor][ycor+1] = "X"
                score -= 500
            elif pacmap[xcor][ycor+1] == " ":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor+1] = "X"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor][ycor+1] = "X"
                    pacmap[xcor][ycor] = " "
    if entity == "Y":
        if poped_move == "N":
            if pacmap[xcor-1][ycor] == ".":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor-1][ycor] = "YL"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor-1][ycor] = "YL"
                    pacmap[xcor][ycor] = " "
            elif pacmap[xcor-1][ycor] == "P":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor] = "."
                    pacmap[xcor-1][ycor] = "Y"
                else:
                    pacmap[xcor][ycor] = " "
                    pacmap[xcor-1][ycor] = "Y"
                score -= 500
            elif pacmap[xcor-1][ycor] == " ":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor-1][ycor] = "Y"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor-1][ycor] = "Y"
                    pacmap[xcor][ycor] = " "
        if poped_move == "S":
            if pacmap[xcor+1][ycor] == ".":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor+1][ycor] = "YL"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor+1][ycor] = "YL"
                    pacmap[xcor][ycor] = " "
            elif pacmap[xcor+1][ycor] == "P":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor] = "."
                    pacmap[xcor+1][ycor] = "Y"
                else:
                    pacmap[xcor][ycor] = " "
                    pacmap[xcor+1][ycor] = "Y"
                score -= 500
            elif pacmap[xcor+1][ycor] == " ":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor+1][ycor] = "Y"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor+1][ycor] = "Y"
                    pacmap[xcor][ycor] = " "
        if poped_move == "W":
            if pacmap[xcor][ycor-1] == ".":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor-1] = "YL"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor][ycor-1] = "YL"
                    pacmap[xcor][ycor] = " "
            elif pacmap[xcor][ycor-1] == "P":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor] = "."
                    pacmap[xcor][ycor-1] = "Y"
                else:
                    pacmap[xcor][ycor] = " "
                    pacmap[xcor][ycor-1] = "Y"
                score -= 500
            elif pacmap[xcor][ycor-1] == " ":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor-1] = "Y"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor][ycor-1] = "Y"
                    pacmap[xcor][ycor] = " "
        if poped_move == "E":
            if pacmap[xcor][ycor+1] == ".":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor+1] = "YL"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor][ycor+1] = "YL"
                    pacmap[xcor][ycor] = " "
            elif pacmap[xcor][ycor+1] == "P":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor] = "."
                    pacmap[xcor][ycor+1] = "Y"
                else:
                    pacmap[xcor][ycor] = " "
                    pacmap[xcor][ycor+1] = "Y"
                score -= 500
            elif pacmap[xcor][ycor+1] == " ":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor+1] = "Y"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor][ycor+1] = "Y"
                    pacmap[xcor][ycor] = " "
    if entity == "Z":
        if poped_move == "N":
            if pacmap[xcor-1][ycor] == ".":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor-1][ycor] = "ZL"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor-1][ycor] = "ZL"
                    pacmap[xcor][ycor] = " "
            elif pacmap[xcor-1][ycor] == "P":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor] = "."
                    pacmap[xcor-1][ycor] = "Z"
                else:
                    pacmap[xcor][ycor] = " "
                    pacmap[xcor-1][ycor] = "Z"
                score -= 500
            elif pacmap[xcor-1][ycor] == " ":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor-1][ycor] = "Z"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor-1][ycor] = "Z"
                    pacmap[xcor][ycor] = " "
        if poped_move == "S":
            if pacmap[xcor+1][ycor] == ".":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor+1][ycor] = "ZL"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor+1][ycor] = "ZL"
                    pacmap[xcor][ycor] = " "
            elif pacmap[xcor+1][ycor] == "P":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor] = "."
                    pacmap[xcor+1][ycor] = "Z"
                else:
                    pacmap[xcor][ycor] = " "
                    pacmap[xcor+1][ycor] = "Z"
                score -= 500
            elif pacmap[xcor+1][ycor] == " ":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor+1][ycor] = "Z"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor+1][ycor] = "Z"
                    pacmap[xcor][ycor] = " "
        if poped_move == "W":
            if pacmap[xcor][ycor-1] == ".":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor-1] = "ZL"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor][ycor-1] = "ZL"
                    pacmap[xcor][ycor] = " "
            elif pacmap[xcor][ycor-1] == "P":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor] = "."
                    pacmap[xcor][ycor-1] = "Z"
                else:
                    pacmap[xcor][ycor] = " "
                    pacmap[xcor][ycor-1] = "Z"
                score -= 500
            elif pacmap[xcor][ycor-1] == " ":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor-1] = "Z"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor][ycor-1] = "Z"
                    pacmap[xcor][ycor] = " "
        if poped_move == "E":
            if pacmap[xcor][ycor+1] == ".":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor+1] = "ZL"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor][ycor+1] = "ZL"
                    pacmap[xcor][ycor] = " "
            elif pacmap[xcor][ycor+1] == "P":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor] = "."
                    pacmap[xcor][ycor+1] = "Z"
                else:
                    pacmap[xcor][ycor] = " "
                    pacmap[xcor][ycor+1] = "Z"
                score -= 500
            elif pacmap[xcor][ycor+1] == " ":
                if pacmap[xcor][ycor][-1] == "L":
                    pacmap[xcor][ycor+1] = "Z"
                    pacmap[xcor][ycor] = "."
                else:
                    pacmap[xcor][ycor+1] = "Z"
                    pacmap[xcor][ycor] = " "
    return pacmap,score

#this functions takes move for the pacman or the ghost, and make changes to the pacmap. the score changes along with different moves
#note a few cases:
#1.a pacman moves to an empty place
#2.a ghost moves to an empty place
#3.a pacman eats a food
#4.a ghost moves above a food, here we denote this case as "WL","XL","YL" or "ZL"
#5.a pacman gets eaten by a ghost
def move(entity,xcor,ycor,score,pacmap):
    if entity == "W" or entity == "X" or entity == "Y" or entity == "Z":
        poped_move = random_move_choice(entity,xcor,ycor,pacmap)
    else:
        poped_move = better_move(xcor,ycor,pacmap)
    pacmap,score = generate_successor(pacmap,entity,xcor,ycor,poped_move,score)
    move_des = entity+" moving "+poped_move
    return score,pacmap,move_des

def better_play_mulitple_ghosts(problem):

    solution = []
    solution.append("seed: "+problem[0]+"\n")
    solution.append("0\n")
    for i in problem[1]:
        solution.append(i)
    seed = problem[0]
    random.seed(version = 1)
    round_num = 0
    pacmap_str = problem[1]
    pacmap = []
    for i in pacmap_str:
        pacmap.append([j for j in i])
    ghost_num = check_ghost_num(pacmap)
    factor = ghost_num+1
    score = 0
    entity = "P"
    move_des = ""

    while game_end(pacmap) == 0:
        entity = take_turn(round_num,factor)
        pacman_x, pacman_y, ghost_dict = check_cor(pacmap)
        if round_num % factor == 0:
            score,pacmap,move_des = move(entity,pacman_x,pacman_y,score,pacmap)
        else:
            score,pacmap,move_des = move(entity,ghost_dict[entity][0],ghost_dict[entity][1],score,pacmap)
        #flag = switch_turn(flag)
        round_num += 1
        solution.append("\n"+str(round_num)+": "+move_des+"\n")
        printpacmap = [row[:] for row in pacmap]
        for i in range(0,len(printpacmap)):
            for j in range(0,len(printpacmap[-1])-1):
                if printpacmap[i][j][-1] == "L":
                    printpacmap[i][j] = printpacmap[i][j][0]
        for i in printpacmap:
            solution.append("".join(i))
        
        #try
        try_lst = []
        for i in pacmap:
            try_lst.append("".join(i))
        print("".join(try_lst))

        solution.append("\nscore: "+str(score))

    
    if game_end(pacmap) == 1:
        solution.append("\nWIN: Pacman")
        winner = "Pacman"
    else:
        solution.append("\nWIN: Ghost")
        winner = "Ghost"
    return "".join(solution),winner

if __name__ == "__main__":
    test_case_id = int(sys.argv[1])    
    problem_id = 4
    file_name_problem = str(test_case_id)+'.prob' 
    file_name_sol = str(test_case_id)+'.sol'
    path = os.path.join('test_cases','p'+str(problem_id)) 
    problem = parse.read_layout_problem(os.path.join(path,file_name_problem))
    num_trials = int(sys.argv[2])
    verbose = bool(int(sys.argv[3]))
    print('test_case_id:',test_case_id)
    print('num_trials:',num_trials)
    print('verbose:',verbose)
    start = time.time()
    win_count = 0
    for i in range(num_trials):
        solution, winner = better_play_mulitple_ghosts(copy.deepcopy(problem))
        if winner == 'Pacman':
            win_count += 1
        if verbose:
            print(solution)
    win_p = win_count/num_trials * 100
    end = time.time()
    print('time: ',end - start)
    print('win %',win_p)