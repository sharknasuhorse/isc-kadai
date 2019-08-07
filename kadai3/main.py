
c = []

def put(i, n):
    if i < n:
        for j in range(n):
            print("for",c)
            if j not in c :
                print(c)
                c.append(j)
                put(i + 1, n)
                c.pop()
    else:
        if len(c) == 8:
           #input()

put(0, 8)


