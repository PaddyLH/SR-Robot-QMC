import numpy as np 
import matplotlib.pyplot as plt 
import time
import math

# currently not accurate and working neural network 
# There is a working model that I will upload here soon

file = open("out.txt")
text = file.read()
file.close()

iss = []
oss = []

t = []
c = ""
for i in range(len(text)):
    if text[i] == '''
''':
        t.append(c)
        c = ""
    else:
        c += text[i]

for item in t:
    c = ""
    v = []
    for i in range(len(item)):
        if item[i] == ",":
            v.append(c)
            c = ""
        else: c+= item[i]
    if c != "": v.append(c)

    v[0] = (math.degrees(float(v[0])) % 360) / 360
    if (v[0] < 0): print(v[0])
    v[1] = (math.degrees(float(v[1])) % 360) / 360
    if (v[1] < 0): print(v[1])
    v[2] = (math.degrees(float(v[2])) % 360) / 360
    if (v[2] < 0): print(v[2])
    v[3] = float(int(v[3]) / 3000) 
    v[4] = int(v[4])

    iss.append([v[0], v[1], v[2], v[3]])
    if v[4] == 1: oss.append([1])
    else: oss.append([0])

print("DONE")
#print(iss)
#print([oss])

class NeuralNetwork:

    # intialize variables in class
    def __init__(self, inputs, outputs):
        self.inputs  = inputs
        self.outputs = outputs
        # initialize weights as .50 for simplicity
        self.weights = np.array([[.50], [.50], [.50], [.50]])
        self.error_history = []
        self.epoch_list = []

    #activation function ==> S(x) = 1/1+e^(-x)
    def sigmoid(self, x, deriv=False):
        if deriv == True:
            return x * (1 - x)
        return 1 / (1 + np.exp(-x))

    # data will flow through the neural network.
    def feed_forward(self):
        self.hidden = self.sigmoid(np.dot(self.inputs, self.weights))

    # going backwards through the network to update weights
    def backpropagation(self):
        self.error  = self.outputs - self.hidden
        delta = self.error * self.sigmoid(self.hidden, deriv=True)
        self.weights += np.dot(self.inputs.T, delta)

    # train the neural net for 25,000 iterations
    def train(self, epochs=25000):
        for epoch in range(epochs):
            self.feed_forward()
            self.backpropagation()    
            self.error_history.append(np.average(np.abs(self.error)))
            self.epoch_list.append(epoch)

    def predict(self, new_input):
        prediction = self.sigmoid(np.dot(new_input, self.weights))
        return prediction

NN = NeuralNetwork(np.array(iss), np.array(oss))
NN.train()

correct = 0
for i in range(len(iss)):
    inp = iss[i]
    out = oss[i]
    output = NN.predict(np.array(inp))
    print("output", output)
    if output >= 0.5: output = 1
    else: output = 0
    if (out[0] == output):correct += 1

print(correct / len(iss) * 100)


plt.figure(figsize=(15,5))
plt.plot(NN.epoch_list, NN.error_history)
plt.xlabel('Epoch')
plt.ylabel('Error')
plt.show()