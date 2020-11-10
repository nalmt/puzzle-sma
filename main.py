# TP1 SMA 
# 10/11/20

import numpy as np
from enum import Enum
import random

n = 5
matrix = np.full((n, n), '0')


def add_agent(agent):
    if matrix[agent.position[0]][agent.position[1]] == '0':
        matrix[agent.position[0]][agent.position[1]] = agent.name
    else:
        print("Erreur ajout agent : agent deja present")

class Agent:
    position: tuple
    goal: tuple
    name: str

    def __init__(self, name, position, goal):
        self.name = name
        self.position = position
        self.goal = goal

    def checkPath(self, path):
        i=0
        for case in path:
            if matrix[case[0]][case[1]] != '0':
                i = +1
        if i > 0:
            return False
        else:
            return True

    def findSP(self):
        path = [[1, 2], [1, 4], [4, 4]] #test true
        #path = [[1, 2], [1, 3], [4, 4]] #test false
        return path















def main():
    a = Agent('A', (0, 1), (0, 2))
    b = Agent('B', (1, 3), (0, 1))
    c = Agent('C', (4, 1), (4, 1))
    d = Agent('D', (2, 2), (4, 4))

    for agent in (a, b, c, d):
        add_agent(agent)

    print(matrix)
    print(a.checkPath(a.findSP()))




if __name__ == "__main__":
    main()