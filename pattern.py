n=6
d=n
for x in range(1,n+1):
    ch=0
    e=1
    for y in range(1,2*n+1):
        if(y>=d) !=0 and y<=n:
            print(chr(ch+65)+" ",end="")
            ch+=1
        elif y<=2*n-d+1 and y>n:
            print(str(e)+" ",end="")
            e+=1
        else:
            print("  ",end="")
    print()
    d-=1
    

    

    