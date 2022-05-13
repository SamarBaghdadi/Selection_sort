def selection_sort(A):
    for j in range (len(A)):
        min=j
        for i in range(j,len(A)):
            if A[i]<A[min]:
                min=i
        A[j],A[min]=A[min],A[j]
    return A


