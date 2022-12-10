#Quick sort
# we use two fuctions here.
# quiSrt() -> divides and applys quick sort for left and right arrays of pivot element.
# partionEr() -> sorts given sub-array and returns partition position i.

def quiSrt(arr,left,right):
    if left < right:
        partion_pos = partionEr(arr,left,right)
        quiSrt(arr,left,partion_pos-1)      #quick sort for left sub-array
        quiSrt(arr,partion_pos+1,right)     #quick sort for Right sub-array

def partionEr(arr,lef,rig):
    #assuming pivot element is arr[right] so not distrubbing that.
    i=lef
    j=rig-1
    pivot=arr[rig]
    while i < j:
        while i < rig and arr[i] < pivot:
            i+=1
        while j > lef and arr[j] > pivot:
            j-=1
        if i < j:
            arr[i],arr[j]=arr[j],arr[i]
    if arr[i]> pivot:
        arr[i],arr[rig]=arr[rig],arr[i]
    return i




#Driving code
arr=[1,10,5,6,2]
quiSrt(arr,0,len(arr)-1)
print(arr)