posArrUsortert = []
inndelingerPerSide = 2
storelse_kube = 20

for i in range(1,11):
    for j in range(1,11):
        for k in range(1,11):
            posArrUsortert.append([k,j,i])


#sorterer posArr

posArr = []
for i in range(inndelingerPerSide):
    posArr.append([])
    for j in range(inndelingerPerSide):
        posArr[i].append([])
        for k in range(inndelingerPerSide):
            posArr[i][j].append([])

print(posArr)

#for element in posArrUsortert:

