# TP1 SMA 
# 10/11/20

import numpy as np
from enum import Enum
from threading import Thread, Lock
import random

mutex = Lock()

n = 5
matrix = np.full((n, n), '0')

def add_agent(agent):
    if matrix[agent.position[0]][agent.position[1]] == '0':
        matrix[agent.position[0]][agent.position[1]] = agent.name
    else:
        print("Erreur ajout agent : agent deja present")

class Agent:
    best_path = []

    def __init__(self, name, position, goal):
        self.name = name
        self.position = position
        self.goal = goal



    def move(self):
        mutex.acquire()
        path = findSP()
        if checkPath(path):
            matrix[self.position[0]][self.position[1]] = '0'
            matrix[path[0][0]][path[0][1]] = self.name
            print(matrix)
        else:
            print("ne peut pas bouger")
            print(matrix)
            mutex.release()
        else:
            print(self.name, "ne bouge pas")


    def checkPath(self, path):
        i = 0
        for case in path:
            if matrix[case[0]][case[1]] != '0':
                i = +1
        if i > 0:
            return False
        else:
            return True


    def findSP(self):
        path = [[1, 2], [1, 4], [4, 4]]  # test true
        # path = [[1, 2], [1, 3], [4, 4]] #test false
        return path

def agent_schedule(agent):
    while True:
        # set_best_path(agent)
        agent.move()

def main():
    a = Agent('A', (0, 1), (0, 2))
    b = Agent('B', (1, 3), (0, 1))
    c = Agent('C', (4, 1), (4, 1))
    d = Agent('D', (2, 2), (4, 4))

    agents = [a, b, c, d]
    for agent in agents:
        add_agent(agent)
    
    for agent in agents:
        t = Thread(target = agent_schedule, args = (agent,))
        t.start()

if __name__ == "__main__":
    main()