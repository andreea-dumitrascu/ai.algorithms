import numpy as np

# functia sigmoid
def sigmoid(x):
    return 1.0/(1.0 + np.exp(-x))

# derivata functiei sigmoid
def sigmoid_derivative(x):
    return x * (1 - x)

class Input:
  def __init__(self, x, y, scop):
    self.x = x
    self.y = y
    self.scop = scop


# initializare input si output
inputs = np.array([Input(0,0,0.1),Input(0,1,0.9),Input(1,0,0.9),Input(0,0,0.1)])
out1 = [0,0]
out2 = [0,0]
out3 = [0]
error = [0,0,0,0]
E = 0 
epoch = 1
# coeficient de invatare
eta = 0.7

inputLayerNeurons = 2 
hiddenLayerNeurons = 2
outputLayerNeurons = 1

#initializare ponderi
w12 = np.random.uniform(size=(inputLayerNeurons,hiddenLayerNeurons)) 
prag2 =np.random.uniform(size=(1,hiddenLayerNeurons))
w23 = np.random.uniform(size=(hiddenLayerNeurons,outputLayerNeurons))
prag3 = np.random.uniform(size=(1,outputLayerNeurons))

print("Epoca", epoch)

for index in range(4):
    # FORWARD
    out1[0] = inputs[index].x
    out1[1] = inputs[index].y
    scop = inputs[index].scop
    
    # se calculeaza iesirile de pe stratul ascuns (calculul activarii de pe hidden layer)
    for h in range(hiddenLayerNeurons):
        suma = 0
        for i in range(inputLayerNeurons):
            suma = suma + (w12[h][i] * out1[i])
        suma = suma + prag2[0][h]
        out2[h] = sigmoid(suma)

    # se calculeaza iesirile de pe stratul de iesire (calculul activarii de pe output layer)
    for o in range(outputLayerNeurons):
        suma = 0
        for h in range(hiddenLayerNeurons):
            suma = suma + (w23[h][o] * out2[h])
        suma = suma + prag3[0][o]
        out3[o] = sigmoid(suma)
    
    # calculam eroarea retelei
    error[index] = np.power(out3[0] - scop, 2)

    print("Pentru: x = " + str(out1[0]) + " si y = " + str(out1[1]) + " avem output-ul " + str(out3[0]))

    # BACKWARD
    # actualizam bias din stratul de iesire
    for i in range(outputLayerNeurons):
        prag3[0][o] = prag3[0][o] - (eta * (2 * (out3[o] - scop) * sigmoid_derivative(out3[o])))
    
    # actualizam bias din stratul hidden
    for h in range(hiddenLayerNeurons):
        suma = 0
        for o in range(outputLayerNeurons):
            suma = suma + ((out3[o] - scop) * sigmoid_derivative(out3[o]) * w23[h][o])
        prag2[o] = prag2[o] - (eta * 2 * suma * sigmoid_derivative(out2[h])) 

    # actualizam ponderile
    for h in range(hiddenLayerNeurons):
        for o in range(outputLayerNeurons):
            w23[h][o] = w23[h][o] - (eta * 2 * (out3[o] - scop) * sigmoid_derivative(out3[o]) * out2[h])

    for h in range(hiddenLayerNeurons):
        for i in range(inputLayerNeurons):
            suma = 0
            for o in range(outputLayerNeurons):
                suma = suma + ((out3[o] - scop) * sigmoid_derivative(out3[o]) * w23[h][o])
            w12[h][i] = w12[h][i] - (eta * 2 * suma * sigmoid_derivative(out2[h]) * out1[i])

for i in range(4): 
    E = E + error[i]

print('Eroarea este:', E)

epoch = epoch + 1 

while (E >= 1/np.power(10,28)): 
    E = 0
    print("Epoca", epoch)

    for index in range(4):
    # FORWARD
        out1[0] = inputs[index].x
        out1[1] = inputs[index].y
        scop = inputs[index].scop
        
        # se calculeaza iesirile de pe stratul ascuns (calculul activarii de pe hidden layer)
        for h in range(hiddenLayerNeurons):
            suma = 0
            for i in range(inputLayerNeurons):
                suma = suma + (w12[h][i] * out1[i])
            suma = suma + prag2[0][h]
            out2[h] = sigmoid(suma)

        # se calculeaza iesirile de pe stratul de iesire (calculul activarii de pe output layer)
        for o in range(outputLayerNeurons):
            suma = 0
            for h in range(hiddenLayerNeurons):
                suma = suma + (w23[h][o] * out2[h])
            suma = suma + prag3[0][o]
            out3[o] = sigmoid(suma)

        # calculam eroarea retelei
        error[index] = np.power(out3[0] - scop, 2)

        print("Pentru: x = " + str(out1[0]) + " si y = " + str(out1[1]) + " avem output-ul " + str(out3[0]))

        # BACKWARD
        # actualizam bias din stratul de iesire
        for i in range(outputLayerNeurons):
            prag3[0][o] = prag3[0][o] - (eta * (2 * (out3[o] - scop) * sigmoid_derivative(out3[o])))
        
        # actualizam bias din stratul hidden
        for h in range(hiddenLayerNeurons):
            suma = 0
            for o in range(outputLayerNeurons):
                suma = suma + ((out3[o] - scop) * sigmoid_derivative(out3[o]) * w23[h][o])
            prag3[o] = prag3[o] - (eta * 2 * suma * sigmoid_derivative(out2[h])) 

        # actualizam ponderile
        for h in range(hiddenLayerNeurons):
            for i in range(inputLayerNeurons):
                suma = 0
                for o in range(outputLayerNeurons):
                    suma = suma + ((out3[o] - scop) * sigmoid_derivative(out3[o]) * w23[h][o])
                w12[h][i] = w12[h][i] - (eta * 2 * suma * sigmoid_derivative(out2[h]) * out1[i])

        for h in range(hiddenLayerNeurons):
            for o in range(outputLayerNeurons):
                w23[h][o] = w23[h][o] - (eta * 2 * (out3[o] - scop) *sigmoid_derivative(out3[o]) * out2[h])

    for i in range(4): 
        E = E + error[i]
    
    print('Eroarea este:', E)

    epoch = epoch + 1
    