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

tesla = [[439.67],[430.83],[421.94],[422.64],[425.79],[420.63],[420.28],[424.68],[406.02],[410.83],[388.04],[400.51],[423.90],[420.98],[438.09],[429.95],[421.26],[410.36],[417.13],[411.76],[408.50],[408.09],[441.61],[486.64],[499.27],[489.61],[521.85],[555.38],[574.00],[585.76],[567.60],[584.76],[568.82],[593.38],[599.04],[641.76],[649.88],[604.48],[627.07],[609.99],[639.83],[633.25],[622.77],[655.90]]

obvious = [[0,0,0,0,1],[0,0,0,1,0],[0,0,1,0,0],[0,1,0,0,0],[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1],[0,0,0,1,0],[0,0,1,0,0],[0,1,0,0,0],[1,0,0,0,0]]

a = unit([1,4,1])

a.learn(tesla,0.00001,100000000)

print(a.extend(tesla[0],100))
