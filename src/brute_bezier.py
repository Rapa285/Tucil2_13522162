def bruteforce(t0 :list ,t1 : list,t2 : list,n : int):
    x = [t0[0]]
    y = [t0[1]] 
    for i in range (1,n+1):
        t = i/n
        b0 = (1 - t) ** 2
        b1 = 2*t*(1 - t)
        b2 = t ** 2
        x.append(t0[0] * b0 + t1[0] * b1 + t2[0] * b2)
        y.append(t0[1] * b0 + t1[1] * b1 + t2[1] * b2)

    return x,y