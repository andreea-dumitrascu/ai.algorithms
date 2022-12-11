from cmath import sqrt
from multiprocessing import managers
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import array as arr

class Dot:
  def __init__(self, x, y):
    self.x = x
    self.y = y

def get_distanta(element):
    return element.get('distanta')

k = np.random.randint(2,10)
centroizi = []
colors = ['#CC0000', '#FF007F', '#006600', '#0000CC', '#FFFF00', '#4C0099', '#00FFFF', '#CC6600', '#FF33FF', '#FFCCCC']

for i in range(k):
    x = np.random.uniform(-300, 300)
    y = np.random.uniform(-300, 300)
    dot = Dot(x,y)
    centroizi.append(dot)

# numara epocile
epoch = 0
E1=0
E=-1

while E!=E1:    
    
    #plt.figure()
    # print('Centroizii:')
    for i in centroizi:
        plt.plot(i.x, i.y, 'o', color=colors[centroizi.index(i)], ms = 7)
        # print('x='+ str(i.x) + ' y=' + str(i.y))

    E1 = E
    file = open('dots.txt', 'r')
    lines = file.readlines()
    ct = [0,0,0,0,0,0,0,0,0,0]
    centruGreutateX = [0,0,0,0,0,0,0,0,0,0]
    centruGreutateY = [0,0,0,0,0,0,0,0,0,0]
    epoch = epoch + 1
    
    for line in lines:

        words = line.split(',')
        assign = []

        for i in centroizi:

            # calculeaza distanta dintre punct si centroid
            d=sqrt((float(words[0]) - i.x)*(float(words[0]) - i.x) + (float(words[1]) - i.y)*(float(words[1]) - i.y))
            elem = {"distanta": d.real, "centroid": centroizi.index(i)}
            assign.append(elem)

        # sorteaza vector
        assign.sort(key=get_distanta)
        plt.plot(float(words[0]), float(words[1]), 'o', color=colors[assign[0]['centroid']], ms = 1)
        #plt.plot(float(words[0]), float(words[1]), c=colors[assign[0]['centroid']], s=1)

        # se aduna ct pentru centroidul la care a fost asignat nodul
        ct[assign[0]['centroid']] = ct[assign[0]['centroid']] + 1
        centruGreutateX[assign[0]['centroid']] = centruGreutateX[assign[0]['centroid']] + float(words[0])
        centruGreutateY[assign[0]['centroid']] = centruGreutateY[assign[0]['centroid']] + float(words[1])
    
    # calculeaza centrul de greutate in x
    for greutate in centruGreutateX:
        if ct[centruGreutateX.index(greutate)] != 0:
            centruGreutateX[centruGreutateX.index(greutate)] =  centruGreutateX[centruGreutateX.index(greutate)] / ct[centruGreutateX.index(greutate)]
    
    # calculeaza centrul de greutate in y
    for greutate in centruGreutateY:
        if ct[centruGreutateY.index(greutate)] != 0:
            centruGreutateY[centruGreutateY.index(greutate)] =  centruGreutateY[centruGreutateY.index(greutate)] / ct[centruGreutateY.index(greutate)]
    
    file.close()

    length = len(centroizi)
    for i in range(0, length-1):
        # print('first') 
        # print(str(centroizi[i].x) + " " + str(centroizi[i].y))
        # print(centruGreutateX[i])
        # print(centruGreutateY[i])
        centroizi[i].x = centruGreutateX[i]
        centroizi[i].y = centruGreutateY[i]
        # print('second')
        # print(str(centroizi[i].x) + " " + str(centroizi[i].y))

    file = open('dots.txt', 'r')
    lines=file.readlines()
    secondSum = 0


    # calculeaza functia de convergenta
    for line in lines:

        words = line.split(',')
        firstSum = 0

        for i in range(0,9):

            # calculeaza distanta dintre punct si centroid
            d=sqrt((float(words[0]) - centruGreutateX[i])*(float(words[0]) - centruGreutateX[i]) + (float(words[1]) - centruGreutateY[i])*(float(words[1]) - centruGreutateY[i]))
            firstSum = firstSum + d

        secondSum = secondSum + firstSum

    print('Epoch = ', epoch)
    print('E = ', secondSum)
    # print('centru de greutate x:')
    # for i in range(0,9):
    #     print(centruGreutateX[i], end =" "),
    # print()
    # print('centru de greutate y:')
    # for i in range(0,9):
    #     print(centruGreutateY[i], end =" "),
    print()

    plt.xlim([-300, 300])
    plt.ylim([-300, 300])
    plt.grid(True, which='both')
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.draw()
    plt.pause(0.5)
    plt.clf()

    E = secondSum