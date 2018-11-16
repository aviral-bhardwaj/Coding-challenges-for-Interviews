def MaximalSquare(strArr):
    m=[]
    for i in strArr:
        l=[]
        for j in i:
            l.append(int(j))
        m.append(l)
    res=0
    for i in range(1,len(m)):
        for j in range(1,len(m[i])):
            if m[i][j]==0:
                continue
            k=min(m[i][j-1],m[i-1][j],m[i-1][j-1])
            m[i][j]+=k
            if res<m[i][j]:
                res=m[i][j]
    return res*res
    
# keep this function call here  
l=["0111", "1111", "1111", "1111"]
print(MaximalSquare(l))  
