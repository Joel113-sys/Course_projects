import sys, parse, grader
from heapq import heappush, heappop, heapify

#The main idea of the greedy_search function comes from the lecture notes.
def greedy_search(problem):
    frontier = []
    heappush(frontier, (0, problem[0]))
    exploredSet = []
    while frontier: 
        node = heappop(frontier)
        if type(node[1]) == type("1"):
            node = (node[0],[node[1]])
        if (node[1][-1] in problem[1]):
            ans1 = ' '.join(node[1])
            ans2 = ' '.join(list(exploredSet))
            return ans2+"\n"+ans1
        if node[1][-1] not in exploredSet:
            exploredSet.append(node[1][-1])
            if node[1][-1] in problem[4]:
                for child in problem[4][node[1][-1]]: 
                    if child not in exploredSet:
                        hvalue = 0
                        temp = []
                        for i in node[1]:
                            temp.append(i)
                        temp.append(child)
                        hvalue = problem[3][child]
                        heappush(frontier,(hvalue,temp))

if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    problem_id = 4
    grader.grade(problem_id, test_case_id, greedy_search, parse.read_graph_search_problem)