import NeuralNetworkV6 as n

import random as r

class unit:
    def __init__(self,structure):
        a = structure
        a[0] += a[len(a) - 1]
        self.brain = n.network(a)
        self.memory = []
        for x in range(a[len(a) - 1]):
            self.memory.append(0)

    def guess(self,input_list):
        self.brain.predict(input_list + self.memory)
        result = self.brain.output()
        for x in range(len(self.memory)):
            self.memory[x] = (self.memory[x] + result[x]) / 2
        return result

    def reset(self):
        for x in range(len(self.memory)):
            self.memory[x] = 0

    def learn(self,data,LearnRate,iterations):
        self.reset()
        l = LearnRate
        optimemory = self.memory
        inputlist = []
        outputlist = []
        for x in range(len(data) - 1):
            inputlist.append(data[x] + optimemory)
            for y in range(len(optimemory)):
                optimemory[y] = (optimemory[y] + data[x + 1][y]) / 2
            outputlist.append(data[x + 1])
            #print(data[x],data[x + 1])
        self.brain.train(inputlist,outputlist,l,iterations)
        self.reset()

    def extend(self,context,length):
        self.reset()
        hype = [context]
        for x in range(length):
            hype.append(self.guess(hype[len(hype) - 1]))
        return hype
