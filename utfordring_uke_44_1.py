import random as ran
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

import time


global posArrUsortert
global posArr

# Initialize variables
posArrUsortert = []
inndelingerPerSide = 8
storelse_kube = 1
dt = 0.01

veggDyttMod = 1/20
kraftMultiplier = 5/1000

x_vektor = [1, 0, 0]
y_vektor = [0, 1, 0]
z_vektor = [0, 0, 1]

def fartsOppdatering(element):
    # Update positions and check for boundaries
    for i in range(3):  # For x, y, z
        if (element[i] + element[i + 3] * dt) < 0 or (element[i] + element[i + 3] * dt) > storelse_kube:
            element[i + 3] *= -1  # Reverse speed
        else:
            element[i] += element[i + 3] * dt  # Update position
    return element


#                         boksene, funker de?, fiks ved kantene

def trykkKraft(underBoks):


    underboksUtviklet = []
    for element in underBoks:
        if (type(element) != int):
            F_sum = [(abs(1-2*element[0])*(1-2*(element[0])/storelse_kube))*veggDyttMod, (abs(1-2*element[1])*(1-2*(element[1])/storelse_kube))*veggDyttMod, (abs(1-2*element[2])*(1-2*(element[2])/storelse_kube))*veggDyttMod]
            for andreElement in underBoks:

                if type(andreElement) != int:

                    if not np.array_equal(element, andreElement):  # Check for distinct elements
                        avstand = np.sqrt((element[0] - andreElement[0]) ** 2 +
                                        (element[1] - andreElement[1]) ** 2 +
                                        (element[2] - andreElement[2]) ** 2)
                        if avstand < 1:
                            enhets_vektor = [(andreElement[dim] - element[dim]) / avstand for dim in range(3)]
                            tot_F = (1 - avstand) ** 2  # Attraction when within 1 unit distance
                            F_sum = [F_sum[dim] + enhets_vektor[dim] * tot_F * -kraftMultiplier for dim in range(3)]
            
            # Update velocities
            for dim in range(3):
                element[dim + 3] += F_sum[dim]
            
        underboksUtviklet.append(element)
    
    return underboksUtviklet





# Initialize positions and speeds
for i in np.arange(0,1,0.25):
    for j in np.arange(0,1,0.25):
        for k in np.arange(0,1,0.25):
            posArrUsortert.append([
                k, j, i, 
                round((ran.random())/10 - 0.05, 4), 
                round((ran.random())/10 - 0.05, 4), 
                round((ran.random())/10 - 0.05, 4)
            ])

antallPartikler = len(posArrUsortert)

# Initialize the array for sorting
posArr = [[[[0 for _ in range(antallPartikler)] for _ in range(inndelingerPerSide)] for _ in range(inndelingerPerSide)] for _ in range(inndelingerPerSide)]

# Convert to a NumPy array
posArrUsortert = np.array(posArrUsortert)

underKubeLengde = storelse_kube / inndelingerPerSide

# Set up the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
scat = ax.scatter(posArrUsortert[:, 0], posArrUsortert[:, 1], posArrUsortert[:, 2])

# Set plot limits
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)

def update(frame):

    startHele = time.perf_counter()
    global posArrUsortert
    global posArr
    

    if frame >= 100:
        plt.close()  # Close the figure to stop the animation
        return scat,


    # Clear posArr for this frame
    for i in range(inndelingerPerSide):
        for j in range(inndelingerPerSide):
            for k in range(inndelingerPerSide):
                posArr[i][j][k] = [0 for _ in range(antallPartikler)]  # Clear previous frame data




    
    # Update particle positions and sort them
    startFartOgSortKuber = time.perf_counter()

    for element in posArrUsortert:
        # Update the position of each particle
        fartsOppdatering(element)

        # Calculate positions and clamped indices
        x_retning = int(np.clip(element[0] // underKubeLengde, 0, inndelingerPerSide - 1))
        y_retning = int(np.clip(element[1] // underKubeLengde, 0, inndelingerPerSide - 1))
        z_retning = int(np.clip(element[2] // underKubeLengde, 0, inndelingerPerSide - 1))
        
        posArr[x_retning][y_retning][z_retning][posArr[x_retning][y_retning][z_retning].index(0)] = element

    endFartOgSortKuber = time.perf_counter()


    
    startTrykkKalk = time.perf_counter()

    for i in range(inndelingerPerSide):
        for j in range(inndelingerPerSide):
            for k in range(inndelingerPerSide):
                posArr[i][j][k] = trykkKraft(posArr[i][j][k])

    endTrykkKalk = time.perf_counter()

    # Reconstruct posArrUsortert from posArr


    posArrUsortert = np.concatenate([posArr[i][j][k] for i in range(inndelingerPerSide) 
                                        for j in range(inndelingerPerSide) 
                                        for k in range(inndelingerPerSide)])
    
    

    # Update scatter plot data
    
    scat._offsets3d = (posArrUsortert[:, 0], posArrUsortert[:, 1], posArrUsortert[:, 2])

    endHele = time.perf_counter()

    plt.pause(0.0001)  # A small pause to allow for refreshing

    print(f"Execution time: {endHele - startHele:.6f} seconds")
    print(f"Execution time: {endFartOgSortKuber - startFartOgSortKuber:.6f} seconds")
    print(f"Execution time: {endTrykkKalk - startTrykkKalk:.6f} seconds", "\n\n\n")
    
    return scat,

# Create animation with a smaller interval for smoothness
ani = FuncAnimation(fig, update, frames=100, interval=30, blit=False)
plt.show()






