
import time
import numpy as np
import brute_bezier as bb
import dnc_bezier as dnc
import matplotlib.pyplot as plt

def main():
    algorithm = main_menu()

    t0 = str_to_float_list(input("titik awal (x y): ").split())
    t1 = str_to_float_list(input("titik kontrol (x y): ").split())
    t2 = str_to_float_list(input("titik akhir (x y): ").split())
    n = int(input("jumlah iterasi : "))
    
    start = time.time()
    if algorithm == "1":
        x,y = bb.bruteforce(t0,t1,t2,n+1)
    else:
        x,y = dnc.div_conquer(t0,t1,t2,n,[t0[0]],[t0[1]])
    runtime = (time.time()-start)*1000
    print("runtime : " + str(runtime)+" ms")
    show_curve(x,y,t0,t1,t2)
    return 0


def str_to_float_list(l):
    for i in range (len(l)) :
        l[i] = float(l[i])
    return l

def main_menu():
    print("Pilih algoritma yang ingin digunakan")
    print("1). Brute Force")
    print("2). Divide and Conquer")
    mode = input("(1/2) : ")
    while(mode != "1" and mode != "2"):
        print("Pilih algoritma yang ingin digunakan")
        print("1). Brute Force")
        print("2). Divide and Conquer")
        mode = input("(1/2) : ")
    return mode
    

def show_curve(x,y,t0,t1,t2):
    plt.plot(
        x,
        y,
        label = "bezier curve"
    )
    tkon_x = [t0[0], t1[0], t2[0]]
    tkon_y = [t0[1], t1[1], t2[1]]
    if len(x) < 100:
        plt.scatter(x, y, color='red')
    plt.plot([t0[0], t1[0], t2[0]], [t0[1], t1[1], t2[1]], 'k--', label='Control Points')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
