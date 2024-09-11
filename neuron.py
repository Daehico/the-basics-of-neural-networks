class Neuron:
    def __init__(self, xList, wList):
        self.x = xList
        self.w = wList

    def onStep(self, x):
        if x >= 0:
            return 1
        else:
            return 0

    def y(self):
        sum = 0
        i = 0

        for x in self.x:
            sum += self.x[i] * self.w[i]
            i += 1

        return sum


bias = 27
array1 = [1, 2, 4, 5]
array2 = [3, 6, 7, 8]

n = Neuron(array1, array2)
s = n.y() - bias
y = n.onStep(s)
print("S = ", s)
print("Y = ", y)
