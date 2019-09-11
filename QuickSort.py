#Lab-7 Q2
A = []
for r in range(10):
    A.append(input("Enter a number: "))
print(A)
n = len(A)
y = n-1
p=0
def Partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if(A[j]<=x):
            i=i+1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    temp2 = A[i+1]
    A[i+1] = A[r]
    A[r] = temp2
    return i+1
m=Partition(A,p,r)
print(m)

#D.
def QuickSort(A,p,r):
    if(p<=r):
        q=Partition(A,p,r)
        QuickSort(A,p,q-1)
        QuickSort(A,q+1,r)

QuickSort(A,p,y)
print("Sorted array: ")
print(A)
