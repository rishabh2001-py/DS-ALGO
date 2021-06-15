
def TargetSubset(arr,idx,setofn,sumofn,target):

   if  idx == len(arr):
       if sumofn == target:
           print(setofn)

       return



   TargetSubset(arr,idx+1,setofn + "-" + str(arr[idx]),sumofn+arr[idx],target)
   TargetSubset(arr,idx+1,setofn + "",sumofn,target)



if  __name__=='__main__':

    arr=[10,20,30,40,60,70,80,90]
    target=100
    TargetSubset(arr,0," ",0,target)


