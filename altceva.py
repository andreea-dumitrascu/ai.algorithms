import numpy as np

def sigmoid(x):
    return 1.0/(1.0 + np.exp(-x))

# forward 
inputs = np.array([[0.1,0.1],[0.1,0.9],[0.9,0.1],[0.9,0.9]])
expected_output = np.array([[0],[1],[1],[0]])
E = 1 
epoch = 0
eta = 0.7

inputLayerNeurons = 2 
hiddenLayerNeurons = 2
outputLayerNeurons = 1

hidden_weights = np.random.uniform(size=(inputLayerNeurons,hiddenLayerNeurons)) 
hidden_bias =np.random.uniform(size=(1,hiddenLayerNeurons))
output_weights = np.random.uniform(size=(hiddenLayerNeurons,outputLayerNeurons))
output_bias = np.random.uniform(size=(1,outputLayerNeurons))

print(1/np.power(10,12))

while E >= 1/np.power(10,2):
    epoch = epoch + 1
    # calculul activarii
    # np.dot => [input1 * w11 + input2 * w21, input1 * w12 + input2 * w22]
    #           [0 * w11 + 0 * w21, 0 * w12 + 0 * w22]
    #           [0 * w11 + 1 * w21, 0 * w12 + 1 * w22]
    #           [1 * w11 + 0 * w21, 1 * w12 + 0 * w22]
    #           [1 * w11 + 1 * w21, 1 * w12 + 1 * w22]
    hidden_layer_activation = np.dot(inputs,hidden_weights)
    hidden_layer_activation += hidden_bias
    hidden_layer_output = sigmoid(hidden_layer_activation)

    print(hidden_layer_output)

    output_layer_activation = np.dot(hidden_layer_output,output_weights)
    output_layer_activation += output_bias
    predicted_output = sigmoid(output_layer_activation)

    E = sum(np.power(predicted_output - expected_output, 2))
    print("first", E)

    def sigmoid_derivative(x):
        return x * (1 - x)


    #Backpropagation
    #eroarea stratului de iesire (7)
    error = expected_output - predicted_output
    d_predicted_output = 2 * error * sigmoid_derivative(predicted_output)

    #weight (8) -> old weigth + (7) * output *  eta
    output_weights += hidden_layer_output.T.dot(d_predicted_output) * eta

    #eroare din hidden layer (9)
    error_hidden_layer = d_predicted_output.dot(output_weights.T)
    d_hidden_layer = 2 * error_hidden_layer * sigmoid_derivative(hidden_layer_output)

    #weight (10) -> old weigth + (9) * input *  eta
    hidden_weights += inputs.T.dot(d_hidden_layer) * eta
    # hidden_bias += np.sum(d_hidden_layer,axis=0,keepdims=True) * eta

    print("Epoca: ", epoch)
    print(d_predicted_output)
    print("Eroarea", E)
    print()
