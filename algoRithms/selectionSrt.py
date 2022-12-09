#This is selection sort algorithm...
def selSrt(arr,n):
    #Iterating every element in list
    for x in range(n):
        #consider 1st element of unsorted array as smallest element
        minp= x
        for i in range(x,n):
            if arr[i] < arr[x]:
                minp=i
        
        #swap smallest ele with 1st ele of unsorted
        arr[x],arr[minp]=arr[minp],arr[x]
    return arr

arr=[1,10,5,4,2]
n=len(arr)
print(selSrt(arr,n))