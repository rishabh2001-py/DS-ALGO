

def Mazepath(src_r,src_c, dst_r,dst_c):
    if src_r == dst_r and src_c == dst_c:
        main_res=[""]
        return main_res
    return_list_V=[]
    return_list_H =[]
    if src_c < dst_c:
        return_list_H = Mazepath(src_r, src_c + 1, dst_r, dst_c)
    if src_r < dst_r:
        return_list_V = Mazepath(src_r + 1, src_c, dst_r, dst_c)

    main_res=[]

    for i in return_list_V:
        main_res.append('v'+i)
    for i in return_list_H:
        main_res.append('h'+i)

    return main_res


if __name__ == "__main__":
    a=1
    b=1
    n=3
    m=3
    res=Mazepath(a,b,n,m)
    print(res)
    print(len(res))

