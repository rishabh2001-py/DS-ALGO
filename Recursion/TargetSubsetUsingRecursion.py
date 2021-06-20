
def TargetSubset(arr,idx,setofn,sumofn,target):

   if  idx == len(arr):
       if sumofn == target:
           print("resut found",setofn)

       return

   TargetSubset(arr,idx+1,setofn + "-" + str(arr[idx]),sumofn+arr[idx],target)
   TargetSubset(arr,idx+1,setofn + "",sumofn,target)



if  __name__=='__main__':

    arr=[10,20,30,40]
    target=60
    TargetSubset(arr,0," ",0,target)


