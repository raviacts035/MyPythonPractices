#Merge sort has 2 parts
#There is an important condition to stop splitting
#1st one is recursive split-section splitting arr into right and left parts.
# 2nd part is ntg but merging two sorted arrays.

def mrgSrt(arr):
    if len(arr) > 1:
        mid=len(arr)//2
        lft_arr=arr[:mid]
        rigt_arr=arr[mid:]
        #split section
        mrgSrt(lft_arr)
        mrgSrt(rigt_arr)
        #Merging sorted arrays
        i=0     #left_arr indx
        j=0     #right_arr indx
        k=0     #arr indx
        while i < len(lft_arr) and j < len(rigt_arr):
            if lft_arr[i] < rigt_arr[j]:
                arr[k]=lft_arr[i]
                i+=1
            else:
                arr[k]=rigt_arr[j]
                j+=1
            k+=1
        while i < len(lft_arr):
            arr[k]=lft_arr[i]
            i+=1
            k+=1
        while j <len(rigt_arr):
            arr[k]=rigt_arr[j]
            j+=1
            k+=1

ar= [1,10,4,5,2]
mrgSrt(ar)
print(ar)