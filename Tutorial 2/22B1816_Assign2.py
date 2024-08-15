import numpy as np#numpy package needs to be installed
import random as rd

def f(x,n):
    x1=float(input("Enter the lower limit of interpolation set:"))
    x2=float(input("Enter the higher limit of interpolation set:"))
    if(x>x1 and x<x2):
       xd=np.linspace(x1,x2,n)
       yd=np.cos(xd)
       d=np.array([xd,yd])
       return d

def dd(d,i,j):
    if j==0:
        return d[1][i]
    else:
        return(dd(d,i+1,j-1)-dd(d,i,j-1))/(d[0][i+j]-d[0][i])

def nff(x,n,d):
   r=0
   for i in range(n):
       t=dd(d,0,i)
       for j in range (i):
           t*=(x-d[0][j])
       r+=t
   return r

def lis(x,n,d):
    r=0
    for i in range(n):
        t=1
        for j in range(n):
            if j!=i:
                t*=(x-d[0][j])/(d[0][i]-d[0][j])
        r+=d[1][i]*t
    return r


def ai(x,n,d):
    t=[[0]*n for _ in range(n)]
    for i in range(n):
        t[i][0] = d[1][i]

    for i in range(1, n):
        for j in range(n - i):
            t[j][i] = (((x-d[0][j+i])*t[j][i-1])-((x-d[0][j])*t[j+1][i-1]))/(d[0][j]-d[0][j+i])

    r=t[0][n-1]
    return r   

def mc():
    print("Which process you want to solve cosine in:")
    print("1 for Newton's Fundamental Formula")
    print("2 for Lagrange Interpolation scheme")
    print("3 for Aitken's iterative interpolation scheme")

    mc=int(input("Enter the number:"))
    nc=int(input("Enter the order of the interpolation polynomial:"))
    xc=float(input("Enter the value of interpolation:"))
    ac=[mc,nc,xc]
    return ac

def main():
    uc=mc()
    d=f(uc[2],uc[1])
    print(d)
    if(uc[0]==1):
        print("The answer is ",nff(uc[2],uc[1],d))
    elif(uc[0]==2):
        print("The answer is ",lis(uc[2],uc[1],d))
    elif(uc[0]==3):
        print("The answer is ",ai(uc[2],uc[1],d))
    else:
        print("Invalid Choice.")
    return 0

main()