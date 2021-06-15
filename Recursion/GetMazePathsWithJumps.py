

def MazePathWithJumps(srcC,srcR,dstC,dstR,str1):

    if srcC == dstC and srcR == dstR:
        print(str1,end = "--")
        return


    for i in range(dstC-srcC+1):
        MazePathWithJumps(srcC+1,srcR,dstC,dstR,str1+"h")
    for i in range(dstR - srcR+1):
        MazePathWithJumps(srcC, srcR+1, dstC, dstR, str1 + "v")
    for i in range(dstC - srcC+1 and dstR - dstC+1):
        MazePathWithJumps(srcC + 1, srcR+1, dstC, dstR, str1 + "d")



if __name__ == "__main__":
    a=1
    b=1
    n=2
    m=2
    MazePathWithJumps(a,b,n,m,"")

