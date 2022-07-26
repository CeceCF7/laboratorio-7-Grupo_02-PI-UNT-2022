#definiendo la lista
nums=[]
#entradas
n=int(input("¿Cuántos números enteros ingresará?  "))
for i in range (0,n) :
    print("Ingrese el número del lugar", i+1)
    elemento=int(input())
    nums.insert(i,elemento)
obj=int(input("Ingrese el número objetivo: "))
#proceso
for i in range (0, n-1) :
    for j in range (i+1,n) :
        if nums[i]+nums[j]==obj :
           num1=i
           num2=j
           break
#salida
print("Los dos números del array que dan como resultado el número objetivos son: [",nums[num1], ",",nums[num2],"]")      