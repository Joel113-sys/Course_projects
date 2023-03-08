import collections
import sys, grader, parse

#The main idea of the bfs_search function comes from the lecture notes.
def bfs_search(problem): 
    frontier = collections.deque([problem[0]])
    exploredSet = []
    while frontier: 
        node = []
        node.append(frontier.popleft())
        if type(node[0]) == type("1"):
            node = [node]
        if (node[0][-1] in problem[1]):
            ans1 = ' '.join(list(node[0]))
            ans2 = ' '.join(list(exploredSet))
            return ans2+"\n"+ans1
        if node[0][-1] not in exploredSet:
            exploredSet.append(node[0][-1])
            if node[0][-1] in problem[4]:
                for child in problem[4][node[0][-1]]: 
                    if child not in exploredSet:
                        temp = []
                        for i in node:
                            for j in i:
                                temp.append(j)
                        temp.append(child)
                        frontier.append(temp)

if __name__ == "__main__":
    test_case_id = int(sys.argv[1])
    problem_id = 2
    grader.grade(problem_id, test_case_id, bfs_search, parse.read_graph_search_problem)