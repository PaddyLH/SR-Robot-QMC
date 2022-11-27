import numpy as np 
import matplotlib.pyplot as plt 
import time
import math

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

    v[0] = float(v[0])
    if (v[0] < 0): print(v[0])
    v[1] = float(v[1])
    if (v[1] < 0): print(v[1])
    v[2] = float(v[2])
    if (v[2] < 0): print(v[2])
    v[3] = int(v[3]) / 1000
    v[4] = int(v[4])

    print(v)

    iss.append([v[0], v[1], v[2], v[3]])
    oss.append(v[4])

print("DONE")
#print(iss)
#print([oss])

class NeuralNetwork:
    def __init__(self, learning_rate):
        self.weights = np.array([-161.850899, 14.8545939, 0.115096154, -2.06175901])
        self.bias = np.array(28.86585632087976)
        self.learning_rate = learning_rate

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def _sigmoid_deriv(self, x):
        return self._sigmoid(x) * (1 - self._sigmoid(x))

    def predict(self, input_vector):
        layer_1 = np.dot(input_vector, self.weights) + self.bias
        layer_2 = self._sigmoid(layer_1)
        prediction = layer_2
        return prediction

    def _compute_gradients(self, input_vector, target):
        layer_1 = np.dot(input_vector, self.weights) + self.bias
        layer_2 = self._sigmoid(layer_1)
        prediction = layer_2

        derror_dprediction = 2 * (prediction - target)
        dprediction_dlayer1 = self._sigmoid_deriv(layer_1)
        dlayer1_dbias = 1
        dlayer1_dweights = (0 * self.weights) + (1 * input_vector)

        derror_dbias = (
            derror_dprediction * dprediction_dlayer1 * dlayer1_dbias
        )
        derror_dweights = (
            derror_dprediction * dprediction_dlayer1 * dlayer1_dweights
        )

        return derror_dbias, derror_dweights

    def _update_parameters(self, derror_dbias, derror_dweights):
        self.bias = self.bias - (derror_dbias * self.learning_rate)
        self.weights = self.weights - (
            derror_dweights * self.learning_rate
        )
    
    def train(self, input_vectors, targets, iterations):
        cumulative_errors = []
        for current_iteration in range(iterations):
            # Pick a data instance at random
            random_data_index = np.random.randint(len(input_vectors))

            input_vector = input_vectors[random_data_index]
            target = targets[random_data_index]

            # Compute the gradients and update the weights
            derror_dbias, derror_dweights = self._compute_gradients(
                input_vector, target
            )

            self._update_parameters(derror_dbias, derror_dweights)

            # Measure the cumulative error for all the instances
            if current_iteration % 100 == 0:
                cumulative_error = 0
                # Loop through all the instances to measure the error
                for data_instance_index in range(len(input_vectors)):
                    data_point = input_vectors[data_instance_index]
                    target = targets[data_instance_index]

                    prediction = self.predict(data_point)
                    error = np.square(prediction - target)

                    cumulative_error = cumulative_error + error
                cumulative_errors.append(cumulative_error)

            if current_iteration % 10000 == 0:
                print(current_iteration / iterations * 100,"% Done")

        return cumulative_errors

NN = NeuralNetwork(0.1)
ef = NN.train(np.array(iss), np.array(oss), 100000)

plt.plot(ef)
plt.xlabel("Iterations")
plt.ylabel("Error")
plt.show()

correct = 0
for i in range(len(iss)):
    inp = iss[i]
    out = oss[i]
    output = NN.predict(np.array(inp))
    if output >= 0.5: output = 1
    else: output = 0
    if (out == output): correct += 1

print(correct / len(iss) * 100)
print(NN.weights, NN.bias)

def small_predictor(data):
    weights = [-161.850899, 14.8545939, 0.115096154, -2.06175901]
    bias = 28.86585632087976
    g = 1 / (1 + np.exp(-1 * (np.dot(data, weights) + bias)))
    if g > 0.5: return 1
    return 0

print(small_predictor(iss[-1]),oss[-1])

def index(x,y):
    i = (y / 3) * 400
    j = ((x + 0.3) / 0.6) * 400
    return i, j

data = []
for i in range(400):
    data.append([])
    for j in range(400):
        x = ((j / 100) * 0.6) - 0.3
        z = ((i / 100) * 0.6) - 0.3
        y = (i / 100) * 3

        data[-1].append(small_predictor([0,x,0,y]))

c = 0
for d in iss:
    a,b = index(d[1], d[3])
    if 0 <= a < 400 and 0 <= b < 400:
        data[int(a)][int(b)] = oss[c] + 4
    c += 1

