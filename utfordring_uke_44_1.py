import random as ran


    

posArrUsortert = []
inndelingerPerSide = 2
storelse_kube = 6
dt = 0.1

def fartsOppdatering(element):
    element[0] += element[3]*dt
    element[1] += element[4]*dt
    element[2] += element[5]*dt
    return element

for i in range(4):
    for j in range(4):
        for k in range(4):
            posArrUsortert.append([k,j,i,round(ran.random()-0.5, 4),round(ran.random()-0.5, 4),round(ran.random()-0.5, 4)]) #x,y,z, fart x,y,z


#sorterer posArr

posArr = [[[[] for _ in range(inndelingerPerSide)] for _ in range(inndelingerPerSide)] for _ in range(inndelingerPerSide)]

#print(posArr)

underKubeLengde = storelse_kube/inndelingerPerSide



#loop, hvor mange itterasjoner?


for ghjk in range(6):
#sorterer posArr
    for element in posArrUsortert:
        #print(element[0] // underKubeLengde)
        
        x_retning = int(element[0] // underKubeLengde)
        y_retning = int(element[1] // underKubeLengde)
        z_retning = int(element[2] // underKubeLengde)
        posArr[x_retning][y_retning][z_retning].append(element)
    
    posArrUsortert = []

    for i in range(inndelingerPerSide):
        for j in range(inndelingerPerSide):
            for k in range(inndelingerPerSide):
                for h in range(len(posArr[i][j][k])):
                    posArrUsortert.append(posArr[i][j][k][h])

    print(posArrUsortert[10])
    for i in range(len(posArrUsortert)):
        posArrUsortert[i] = fartsOppdatering(posArrUsortert[i])


""" for i in range(len(posArr[0][0])):
    print(posArr[0][0][i], "\n\n")
 """