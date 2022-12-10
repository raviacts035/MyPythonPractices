##Binary search algorithm
#Binary search alog is used to search an element inside and sorted array
#This code only works for list[int,float]
def sear(ar,n):
    pos=-1      #base case(element not found)
    l=0
    r=len(ar)-1
    mid=(r-l)//2
    while l<=r:
        mid=(r+l)//2
        if ar[mid]==n:
            return mid
            break
        else:
            if ar[mid]>n:
                r=mid-1
            elif ar[mid]<n:
                l=mid+1
    return pos

#Driving code
ar=[2,3,7,67]
n=3
print(sear(ar,n))