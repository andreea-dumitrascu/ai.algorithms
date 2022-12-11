from cgitb import strong
from cmath import sqrt
from multiprocessing import managers
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import array as arr
import pandas as pd
from math import e

class Dot:
  def __init__(self, x, y):
    self.x = x
    self.y = y

def get_distanta(element):
    return element.get('distanta')

def matrix_generaton(Xmatrix, Ymatrix):
    for i in range(10):
        for j in range(10):
            Xmatrix[i][j] = -297 + (66 * j)
            Ymatrix[i][j] = 297 - (66 * i)

def draw_grid(x, y):
    for i in range(10):
            for j in range(9):
                x_values = [x[i][j], x[i][j+1]]
                y_values = [y[i][j], y[i][j+1]]
                plt.plot(x_values, y_values, color='grey')
    for i in range(9):
        for j in range(10):
            x_values = [x[i][j], x[i+1][j]]
            y_values = [y[i][j], y[i+1][j]]
            plt.plot(x_values, y_values, color='grey')

            

# imi propun 10 de epoci
N = 10
currentEpoch = 1
alfa = 0.7 * np.exp(-currentEpoch/N)
x = np.ones((10, 10))
y = np.ones((10, 10))
matrix_generaton(x, y)
# print(x)
# print(y)

file = open('dots.txt', 'r')
lines = file.readlines()

for i in range(10):
    for j in range(9):
            x_values = [x[i][j], x[i][j+1]]
            y_values = [y[i][j], y[i][j+1]]
            plt.plot(x_values, y_values, color='red')
for i in range(9):
    for j in range(10):
            x_values = [x[i][j], x[i+1][j]]
            y_values = [y[i][j], y[i+1][j]]
            plt.plot(x_values, y_values, color='red')

while alfa > 0.0001:

    for line in lines:
        words = line.split(',')
        # print(words[2])
        plt.plot(float(words[0]), float(words[1]), 'o', color='black', ms = 1)
        assign = []

        for i in range(10):
            for j in range(10):
                d=sqrt(np.power((float(words[0]) - x[i][j]), 2) + np.power((float(words[1]) - y[i][j]), 2))
                elem = {"distanta": d.real, "index_i": i, "index_j": j}
                assign.append(elem)
        
        assign.sort(key=get_distanta)
        strongest = assign[0]

        alfa = 0.7 * np.exp(-currentEpoch/N)
        vecinatate = 6.1 * np.exp(-currentEpoch/N)

        V = int(vecinatate) - 1
        i = strongest['index_i']
        j = strongest['index_j']
        # x[i][j] = x[i][j] + (alfa * (float(words[0]) - x[i][j]))
        # y[i][j] = y[i][j] + (alfa * (float(words[1]) - y[i][j]))

        for ii in range(10):
            for jj in range(10):
                if ii >= i-V and jj >= j-V and ii <= i+V and jj <= j+V:
                    x[ii][jj] = x[ii][jj] + (alfa * (float(words[0]) - x[ii][jj]))
                    y[ii][jj] = y[ii][jj] + (alfa * (float(words[1]) - y[ii][jj]))
    
    for i in range(10):
        for j in range(9):
            x_values = [x[i][j], x[i][j+1]]
            y_values = [y[i][j], y[i][j+1]]
            plt.plot(x_values, y_values, color='red')
    for i in range(9):
        for j in range(10):
            x_values = [x[i][j], x[i+1][j]]
            y_values = [y[i][j], y[i+1][j]]
            plt.plot(x_values, y_values, color='red')
    plt.xlim([-300, 300])
    plt.ylim([-300, 300])
    plt.draw()
    plt.pause(1.5)
    plt.clf()
    # print('final')
    # print(x)
    # print()
    # print(y)
    
    currentEpoch = currentEpoch + 1

print('number of epochs', currentEpoch)
    