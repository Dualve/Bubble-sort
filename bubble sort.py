massive = list(map(int,input().split()))
print(massive)
for j in range(0, len(massive)-1): #сколько элементов в массіве
    for i in range(0, len(massive)-1-j): #выполняет сравненіе і обмен
        if massive[i] < massive[i+1]:
            massive[i], massive[i+1] = massive[i+1], massive[i]
print(massive)

