from platform import node
import sys, parse,random
#from turtle import position
import time, os, copy
import math

#this function determines if the game has terminated or not, specifically, it needs to determine
#whether it is pacman or ghost that has won
#if it returns 1, it implies that pacman wins
#if it returns 2, it implies that the ghost wins
#if it returns 0, the game isn't over yet
def game_end(pacmap):
    food_count = 0
    pacman_count = 0
    for i in range(0,len(pacmap)):
        for j in range(0,len(pacmap[1])-2):
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

    posi_dict = {}
    for i in range(0,len(pacmap)):
        for j in range(0,len(pacmap[1])-1):
            if pacmap[i][j] == 'P':
                posi_dict["P"] = (i,j)
            if pacmap[i][j] == 'W' or pacmap[i][j] == 'X' or pacmap[i][j] == 'Y' or pacmap[i][j] == 'Z':
                posi_dict[pacmap[i][j]] = (i,j)
            if pacmap[i][j][-1] == "L":
                posi_dict[pacmap[i][j][0]] = (i,j)


    return posi_dict

#determine all possible choices of a pacman or a ghost a a certain position (x,y)
def move_choice(entity,xcor,ycor,pacmap):
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

    if len(choice_lst) == 0:
        return ""
    else:
        return choice_lst

#this function calculates the distance of two objects
def cal_dist(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

#modify the evaluation function
def eval_func(pacmap,score):
    if game_end(pacmap) == 1:
        return math.inf
    elif game_end(pacmap) == 2:
        return -math.inf
    #find the coordinates of pacman, foods and ghosts
    food_x = []
    food_y = []
    ghost_x = []
    ghost_y = []
    for i in range(0,len(pacmap)):
        for j in range(0,len(pacmap[1])-1):
            if pacmap[i][j] == "." or pacmap[i][j][-1] == "L":
                food_x.append(i)
                food_y.append(j)
            if pacmap[i][j] == 'W' or pacmap[i][j] == 'X' or pacmap[i][j] == 'Y' or pacmap[i][j] == 'Z' or pacmap[i][j][-1] == "L":
                ghost_x.append(i)
                ghost_y.append(j)
            if pacmap[i][j] == "P":
                xcor = i
                ycor = j
    #find the position of the pacman
    posi_dict = check_cor(pacmap)

    #define a ghost_score, which increases as the distance from the pacman and the ghost decreases
    #it is the value of the sum of 1/distance from the pacman to the ghost
    ghost_score = 0
    ghost_dist = 0
    for i in range(0,len(ghost_x)):
        ghost_dist += cal_dist(xcor,ycor,ghost_x[i],ghost_y[i])
        if cal_dist(xcor,ycor,ghost_x[i],ghost_y[i]) <= 4:
            ghost_score += 100/(cal_dist(xcor,ycor,ghost_x[i],ghost_y[i])-0.8)

    #find the index of the closest food that is not below ghosts
    idx_food = 0
    min_dist_food = math.inf
    for i in range(0,len(food_x)):
        if min_dist_food > cal_dist(posi_dict["P"][0],posi_dict["P"][1],food_x[i],food_y[i]):
            if pacmap[food_x[i]][food_y[i]][-1]!="L":
                min_dist_food = cal_dist(posi_dict["P"][0],posi_dict["P"][1],food_x[i],food_y[i])
                idx_food = i

    #this evaluation function: distance to the nearest food+sum of weights of ghost (weight equals the distance between food 
    if len(food_y) == 0:
        return math.inf
    eval_score = -20*cal_dist(xcor,ycor,food_x[idx_food],food_y[idx_food])+(2000/(len(food_y)-0.6))-(len(food_y)**3)-10*ghost_score+ghost_dist
    return eval_score

#this function generates a successor of the last state based on the action
def generate_successor(pacmap,score,poped_move,entity,xcor,ycor):
    if entity == "P":
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
#4.a ghost moves above a food, here we denote this case as "L"
#5.a pacman gets eaten by a ghost
def move(index,score,pacmap,factor,depth):
    entity = entity_deter(index,factor)
    posi_dict = check_cor(pacmap)
    poped_move = minimax_algo(index,1,depth,posi_dict,pacmap,score,factor)
    pacmap_copy = copy.deepcopy(pacmap)
    pacmap_copy,score = generate_successor(pacmap_copy,score,poped_move,entity,posi_dict[entity][0],posi_dict[entity][1])
    if poped_move == None:
        poped_move = ""
    move_des = entity+" moving "+poped_move
    return score,pacmap_copy,move_des

def entity_deter(index,factor):
    if index % factor == 0:
        return "P"
    elif index % factor == 1:
        return "W"
    elif index % factor == 2:
        return "X"
    elif index % factor == 3:
        return "Y"
    elif index % factor == 4:
        return "Z"

def minimax_algo(index,depth_counter,depth,posi_dict,pacmap,score,factor):
   
    node_val = []
    entity = entity_deter(index,factor)
    pacmap_copy = [row[:] for row in pacmap]
    actions = move_choice(entity,posi_dict[entity][0],posi_dict[entity][1],pacmap_copy)
    for action in actions:
        posi_dict = check_cor(pacmap)
        pacmap_copy = copy.deepcopy(pacmap)
        successor,score_in = generate_successor(pacmap_copy,score,action,entity,posi_dict[entity][0],posi_dict[entity][1])
        posi_dict = check_cor(successor)

        if entity == "P":
            if index == factor - 1:
                node_val.append(max_value(0,depth_counter+1,depth,posi_dict,successor,score,factor))
            else:
                node_val.append(max_value(index+1,depth_counter,depth,posi_dict,successor,score,factor))
        else:
            if index == factor - 1:
                node_val.append(min_value(0,depth_counter+1,depth,posi_dict,successor,score_in,factor))
            else:
                node_val.append(min_value(index+1,depth_counter,depth,posi_dict,successor,score_in,factor))

    random_list = []
    if entity == "P":
        for i in range(len(node_val)):
            if abs(node_val[i]) == math.inf:
                for j in range(len(node_val)):
                    if node_val[j] == max(node_val):
                        return actions[i]
            elif abs(node_val[i] - max(node_val))<50:
                random_list.append(actions[i])
        #add some random factor in case the pacman gets stuck
        return random.choice(random_list)
    else:
        for i in range(len(node_val)):
            if abs(node_val[i] - min(node_val)) < 50:
                random_list.append(actions[i])
        if len(random_list) == 0:
            return None
        return random.choice(random_list)

def max_value(index,depth_counter,depth,posi_dict,pacmap,score,factor):
    if game_end(pacmap) == 1:
        return math.inf
    elif game_end(pacmap) == 2:
        return -math.inf
    if depth_counter > depth:
        return eval_func(pacmap,score)
    v = -math.inf
    entity = entity_deter(index,factor)
    pacmap_copy = [row[:] for row in pacmap]
    actions = move_choice(entity,posi_dict[entity][0],posi_dict[entity][1],pacmap_copy)
    if len(actions) == 0:
        return eval_func(pacmap_copy,score)
    for action in actions:
        pacmap_copy = copy.deepcopy(pacmap)
        posi_dict = check_cor(pacmap)
        successor,score_in = generate_successor(pacmap_copy,score,action,entity,posi_dict[entity][0],posi_dict[entity][1])
        posi_dict = check_cor(successor)
        if index == factor - 1:
            v = max(v,min_value(0,depth_counter+1,depth,posi_dict,successor,score_in,factor))
        else:
            v = max(v,min_value(index+1,depth_counter,depth,posi_dict,successor,score_in,factor))
    return v

def min_value(index,depth_counter,depth,posi_dict,pacmap,score,factor):
    if game_end(pacmap) == 1:
        return math.inf
    elif game_end(pacmap) == 2:
        return -math.inf
    if depth_counter > depth:
        return eval_func(pacmap,score)
    v = math.inf
    entity = entity_deter(index,factor)
    pacmap_copy = [row[:] for row in pacmap]
    actions = move_choice(entity,posi_dict[entity][0],posi_dict[entity][1],pacmap_copy)
    if len(actions) == 0:
        return eval_func(pacmap_copy,score)
    for action in actions:
        pacmap_copy = copy.deepcopy(pacmap)
        posi_dict = check_cor(pacmap)
        successor,score_in = generate_successor(pacmap_copy,score,action,entity,posi_dict[entity][0],posi_dict[entity][1])
        posi_dict = check_cor(successor)
        if index == factor - 1:
            v = min(v,max_value(0,depth_counter+1,depth,posi_dict,successor,score_in,factor))
        else:
            v = min(v,max_value(index+1,depth_counter,depth,posi_dict,successor,score_in,factor))
    return v

def min_max_mulitple_ghosts(problem, k):
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
    #flag = True
    move_des = ""

    while game_end(pacmap) == 0:
        score,pacmap,move_des = move(round_num%factor,score,pacmap,factor,k)
        round_num += 1
        
        solution.append("\n"+str(round_num)+": "+move_des+"\n")
        printpacmap = [row[:] for row in pacmap]
        for i in range(0,len(printpacmap)):
            for j in range(0,len(printpacmap[1])-1):
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
    problem_id = 5
    file_name_problem = str(test_case_id)+'.prob' 
    file_name_sol = str(test_case_id)+'.sol'
    path = os.path.join('test_cases','p'+str(problem_id)) 
    problem = parse.read_layout_problem(os.path.join(path,file_name_problem))
    k = int(sys.argv[2])
    num_trials = int(sys.argv[3])
    verbose = bool(int(sys.argv[4]))
    print('test_case_id:',test_case_id)
    print('k:',k)
    print('num_trials:',num_trials)
    print('verbose:',verbose)
    start = time.time()
    win_count = 0
    for i in range(num_trials):
        solution, winner = min_max_mulitple_ghosts(copy.deepcopy(problem), k)
        if winner == 'Pacman':
            win_count += 1
        if verbose:
            print(solution)
    win_p = win_count/num_trials * 100
    end = time.time()
    print('time: ',end - start)
    print('win %',win_p)