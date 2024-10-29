posArrUsortert = []
inndelingerPerSide = 2
storelse_kube = 20

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            posArrUsortert.append([k,j,i])


#sorterer posArr

posArr = [[[0 for _ in range(inndelingerPerSide)] for _ in range(inndelingerPerSide)] for _ in range(inndelingerPerSide)]

print(posArr)

underKubeLengde = storelse_kube/inndelingerPerSide

for element in posArrUsortert:
    x_retning = element[0] // underKubeLengde
