
def get_mid(t0,t1):
    t = []
    t.append((t0[0]+t1[0])/2)
    t.append((t0[1]+t1[1])/2)
    #print("mid "+str(t0)+", "+str(t1)+" : "+str(t))
    return t

def berzier_curve_kuad(P0,P1,P2) : # t = [0,1]
    Q0 = get_mid(P0,P1)
    Q1 = get_mid(P1,P2)
    R0 = get_mid(Q0,Q1)
    return R0

def div_conquer(t0: list,t1 : list,t2 : list,n : int,x : list,y : list):
    if n <= 1:
        titik = berzier_curve_kuad(t0,t1,t2)
        x.append(titik[0])
        y.append(titik[1])
        x.append(t2[0])
        y.append(t2[1])
    else:
        x,y = div_conquer(t0,get_mid(t0,t1),berzier_curve_kuad(t0,t1,t2),n/2,x,y)
        x,y = div_conquer(berzier_curve_kuad(t0,t1,t2,),get_mid(t1,t2),t2,n/2,x,y)
        
    return x,y