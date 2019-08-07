c=[]

def dup(x, y, u, v):
    #input()
    #print("dup", x,y,u,v)
    #print(x==u or y==v or x-u==y-v or x-u==v-y)
    #input()
    return x==u or y==v or x-u==y-v or x-u==v-y

def check(i):
    if i < 8:
        for j in range(8):
            #print(i, j,  c)
            #input()
            print([dup(i, j, p, c[p] ) for p in range(i)])
            input()
            if not any( [dup(i, j, p, c[p] ) for p in range(i)] ) :
                c.append(j)
                check(i+1)
                c.pop()
    else:
        print(c)
check(0)
