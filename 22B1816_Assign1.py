import math

ep=0.001

def f(x,c):
    if(c==1):
      return (math.atan(x)-1)
    elif(c==2):
        return (pow(x,3)+2*pow(x,2)+10*x-20)
    elif(c==3):
        return (math.cos(x)-x)
    elif(c==4):
        return (math.tan(x)-(1/(1+pow(x,2))))
    else:
        print("invalid choice")

def der(x,c):
    return (f(x+ep,c)-f(x,c))/ep
   

def nm(x,c):
    if(f(x,c)==0 or abs(f(x,c))<=ep):
        print("The root is ",x)
    else:
        while(abs(f(x,c))>ep):
            x=x-(f(x, c)/der(x, c))
        print("The root is ",x)
    return 0

def bm(x1,x2,c):
    if(x1==x2):
        print("Wrong entries.")
    elif(x1>x2):
        x=x2
        x2=x1
        x1=x
    if(f(x1,c)*f(x2,c)>0):
        print("Wrong interval")
        return 0
    elif(f(x1,c)*f(x2,c)<0):
      while(f(x1,c)*f(x2,c)<0):
          x=(x1+x2)/2
          if(abs(f(x,c))<ep):
             print("The root is ",x)
             break
          elif(f(x1,c)*f(x,c)<=0):
             x2=x
          elif(f(x1,c)*f(x,c)>=0):
             x1=x
      return 0
    else:
        if(f(x1,c)==0):
            print("The root id ",x1)
        else:
            print("The root id ",x2)
    return 0

def mfpm(a,b,c):
    count=0
    if(count==0):
        f1=f(a,c)
        f2=f(b,c)
        
    while(count<300):
             x=((a*f2-b*f1)/(f2-f1))
             
             if(abs(f(x,c))<ep):
                 print("The root is ",x)
                 count+=1
                 break
             elif(f(x,c)*f1<0):
                  b=x
                  f2=f(b,c)
                  f1=f1/2
                  count+=1
             else:
                  a=x
                  f1=f(a,c)
                  f2=f2/2
                  count+=1

               
    

def fc():
    print("Which equation you want to solve:")
    print("1 for arctan(x) = 1")
    print("2 for x^3 + 2x^2 + 10x − 20 = 0")
    print("3 for cos(x) - x = 0")
    print("4 for tan x=(1/1+x^2)")

    ec=int(input("Enter the number:"))
    return ec

def mc():
    print("Which process you want to solve in:")
    print("1 for Newton's method")
    print("2 for Bisection method")
    print("3 for Modied false position method")

    mc=int(input("Enter the number:"))
    return mc

def main():
    m=mc()
    if(m==1):
        c=fc()
        x=float(input("Enter initial guess:"))
        nm(x,c)
    elif(m==2):
        c=fc()
        x1=float(input("Enter first term of interval:"))
        x2=float(input("Enter second term of interval:"))
        bm(x1,x2,c)
    elif(m==3):
        c=fc()
        a=float(input("Enter first term of interval:"))
        b=float(input("Enter second term of interval:(if eqn id 4 pls use valuse <=1)"))
        mfpm(a,b,c)
    else:
        print("Invaild choice, run program again.")


main()
    
    
    