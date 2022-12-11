from multiprocessing import managers
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# make full screen
# plt.show(block = False)
# manager = plt.get_current_fig_manager()
# manager.full_screen_toggle()

# functia pentru normalizare
def gaussNormalization(coordonate, m, d):
    return np.exp(-((m - coordonate) ** 2) / (2 * (d ** 2)))

# functia care generaza 
def dotGeneration(zone, zoneNumber, file):
    for i in range(3000):
        xaceepted = 0
        while xaceepted == 0 :
            x = np.random.uniform(-300, 300)
            gnx = gaussNormalization(x, zone.xcenter, zone.xdistribution)
            prag = np.random.randint(0,np.power(2,15))/np.power(2,15)
            # prob = 0.1 * (1/np.power(2,2))
            if gnx > prag:
                xaceepted = 1
        yaccepted = 0
        while yaccepted == 0 : 
            y = np.random.uniform(-300, 300)
            gny = gaussNormalization(y, zone.ycenter, zone.ydistribution)
            prag = np.random.randint(0,np.power(2,15))/np.power(2,15)
            # prob = 0.1 * (1/np.power(2,2))
            if gny > prag: 
                yaccepted = 1
        if zoneNumber == 1:
            plt.scatter(x, y, c='red', s = 0.1)
            file.write(str(x) +',' + str(y) + ','+ ' zona1 \n')
        if zoneNumber == 2:
            plt.scatter(x, y, c='pink', s = 0.1)
            file.write(str(x) +',' + str(y) + ','+ ' zona2 \n')
        if zoneNumber == 3:
            plt.scatter(x, y, c='blue', s = 0.1)
            file.write(str(x) +',' + str(y) + ','+ ' zona3 \n')
        if zoneNumber == 4:
            plt.scatter(x, y, c='yellow', s = 0.1)
            file.write(str(x) +',' + str(y) + ','+ ' zona4 \n')
        if zoneNumber == 5:
            plt.scatter(x, y, c = 'orange', s = 0.1)
            file.write(str(x) +',' + str(y) + ','+ ' zona5 \n')

# clase zone
class Zone:
  def __init__(self, cx, cy, dx, dy):
    self.xcenter = cx
    self.ycenter = cy
    self.xdistribution = dx
    self.ydistribution = dy

# deschidem fisierul in care vom scrie punctele
f = open("dots.txt", "w")

# definim cele 5 zone
firstZone = Zone(10, 10, 3, 5)
secondZone = Zone(-100, -100, 20, 20)
thirdZone = Zone(200, 200, 10, 10)
forthZone = Zone(-10, 10, 5, 5)
fifthZone = Zone(45, 80, 10, 10)

# dam limite plot-ului
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.xlim([-300, 300])
plt.ylim([-300, 300])

# generam puncte pentru 3 zone
dotGeneration(firstZone, 1, f)
dotGeneration(secondZone, 2, f)
dotGeneration(thirdZone, 3, f)

plt.show()
f.close()
